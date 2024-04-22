import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Importar messagebox para caixa de diálogo
from datetime import datetime
from bd import inserir_dados

def tela_registrar():
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

    def registrar():
        valor = entry_valor.get()
        vencimento = converter_para_data(entry_vencimento.get())
        descricao = entry_descricao.get()
        tipo = combo_tipo.get()
        dataSistema = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        # Caixa de diálogo de confirmação
        if messagebox.askokcancel("Confirmação", "Deseja registrar os dados?"):
            # Inserir os dados no banco de dados
            inserir_dados(valor, vencimento, descricao, tipo, dataSistema)
            # Limpar os campos após o registro
            limpar_campos()

    def converter_para_data(data_texto):
        try:
            data_vencimento = datetime.strptime(data_texto, "%d/%m/%y").date()
            data_vencimento = data_vencimento.strftime("%y/%m/%d")
            return data_vencimento
        except ValueError:
            return None

    def limpar_campos():
        entry_valor.delete(0, tk.END)
        entry_vencimento.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        combo_tipo.set("")

    def voltar_tela_principal():
        root.destroy()
        from telaPrincipal import tela_principal
        tela_principal()
        
    label_valor = tk.Label(frame, text="Digite o valor:", font=20)
    label_valor.pack()

    entry_valor = tk.Entry(frame, font=20)
    entry_valor.pack()

    label_vencimento = tk.Label(
        frame, text="Digite o vencimento no formato DD/MM/AA:", font=20
    )
    label_vencimento.pack()

    entry_vencimento = tk.Entry(frame, font=20)
    entry_vencimento.pack()

    label_descricao = tk.Label(frame, text="Digite a descrição:", font=20)
    label_descricao.pack()

    entry_descricao = tk.Entry(frame, font=20)
    entry_descricao.pack()

    label_tipo = tk.Label(frame, text="Selecione o tipo:", font=20)
    label_tipo.pack()

    tipos = ["Pagar", "Receber"]
    combo_tipo = ttk.Combobox(frame, values=tipos, font=20, state="readonly")
    combo_tipo.pack()

    btn_registrar = tk.Button(
        frame,
        text="Registrar",
        font=20,
        command=registrar,
    )
    btn_registrar.pack(pady=10)

    btn_voltar = tk.Button(frame, text="Voltar", font=20, command=voltar_tela_principal)
    btn_voltar.pack()

    root.mainloop()

