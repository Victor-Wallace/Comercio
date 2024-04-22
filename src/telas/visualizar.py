import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from bd import consultar_dados

def tela_visualizar():
    def consultar():
        # Obter datas de início e fim no formato DD/MM/AAAA
        data_inicio_str = entry_data_inicio.get()
        data_fim_str = entry_data_fim.get()

        try:
            # Converter datas para o formato YYYY-MM-DD
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y").date()
            data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y").date()
        except ValueError:
            # Lidar com entrada inválida de datas
            messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.")
            return

        # Obter o tipo selecionado
        tipo_selecionado = combo_tipo.get()

        # Consultar dados com base no filtro de período e tipo
        resultados = consultar_dados_por_periodo(data_inicio, data_fim, tipo_selecionado)

        # Exibir resultados na lista
        mostrar_resultados(resultados)

    def consultar_dados_por_periodo(data_inicio, data_fim, tipo):
        # Consultar dados no banco de dados com base no período e tipo especificados
        resultados = consultar_dados(data_inicio, data_fim, tipo)
        return resultados

    def mostrar_resultados(resultados):
        # Limpar resultados anteriores
        limpar_resultados()

        # Exibir resultados na lista
        for resultado in resultados:
            lista_resultados.insert("", "end", values=(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5]))

    def limpar_resultados():
        # Limpar resultados anteriores da lista
        for item in lista_resultados.get_children():
            lista_resultados.delete(item)

    def voltar_tela_principal():
        root.destroy()
        from telaPrincipal import tela_principal
        tela_principal()

    root = tk.Tk()
    root.title("CashFlowMaster")
    window_width = 980
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    label_data_inicio = tk.Label(frame, text="Data de Início:", font=20)
    label_data_inicio.pack()

    entry_data_inicio = tk.Entry(frame, font=20)
    entry_data_inicio.pack()

    label_data_fim = tk.Label(frame, text="Data de Fim:", font=20)
    label_data_fim.pack()

    entry_data_fim = tk.Entry(frame, font=20)
    entry_data_fim.pack()

    label_tipo = tk.Label(frame, text="Tipo:", font=20)
    label_tipo.pack()

    tipos = ["Pagar", "Receber"]
    combo_tipo = ttk.Combobox(frame, values=tipos, font=20, state="readonly")
    combo_tipo.pack()

    btn_consultar = tk.Button(
        frame,
        text="Consultar",
        font=20,
        command=consultar,
    )
    btn_consultar.pack(pady=10)

    # Criar a lista para exibir os resultados
    lista_resultados = ttk.Treeview(frame, columns=("Valor", "Vencimento", "Descrição", "Tipo", "Data do Registro"),show="headings")
    lista_resultados.heading("Valor", text="Valor")
    lista_resultados.heading("Vencimento", text="Vencimento")
    lista_resultados.heading("Descrição", text="Descrição")
    lista_resultados.heading("Tipo", text="Tipo")
    lista_resultados.heading("Data do Registro", text="Data do Registro")
    lista_resultados.pack(pady=10, fill="both", expand=True)

    btn_voltar = tk.Button(frame, text="Voltar", font=20,command=voltar_tela_principal)
    btn_voltar.pack()

    root.mainloop()

