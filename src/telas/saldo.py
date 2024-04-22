import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from bd import consultar_saldo

def tela_saldo():
    def consultar():
        tipo_selecionado = combo_tipo.get()
        saldo = consultar_saldo(tipo_selecionado)
        if saldo is not None:
            lbl_saldo["text"] = f"Saldo: R$ {saldo:.2f}"
        else:
            messagebox.showerror("Erro", "Falha ao consultar saldo.")
    
    def voltar_tela_principal():
        root.destroy()
        from telaPrincipal import tela_principal
        tela_principal()        

    # Criar a janela principal
    root = tk.Tk()
    root.title("CashFlowMaster")
    window_width = 300
    window_height = 200

    # Obter as dimensões da tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular a posição para centralizar a janela
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Definir a geometria da janela com base nas dimensões e posição calculadas
    root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

    frame = tk.Frame(root)
    frame.pack(expand=True)

    lbl_tipo = tk.Label(frame, text="Selecione o tipo:", font=("Arial", 12))
    lbl_tipo.pack(pady=(10, 0))

    tipos = ["Pagar", "Receber"]
    combo_tipo = ttk.Combobox(frame, values=tipos, font=("Arial", 12), state="readonly")
    combo_tipo.pack(pady=(0, 10))

    btn_consultar = tk.Button(frame, text="Consultar", font=("Arial", 12), command=consultar)
    btn_consultar.pack()

    lbl_saldo = tk.Label(frame, text="", font=("Arial", 12))
    lbl_saldo.pack(pady=(10, 0))

    btn_voltar = tk.Button(frame, text="Voltar", font=20, command=voltar_tela_principal)
    btn_voltar.pack()

    root.mainloop()

