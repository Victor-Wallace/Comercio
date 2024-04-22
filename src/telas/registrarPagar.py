import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("CashFlowMaster")
window_width = 980
window_height = 500

# Obter as dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular a posição para centralizar a janela
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Definir a geometria da janela com base nas dimensões e posição calculadas
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# Criar um frame para conter todos os elementos
frame = tk.Frame(root)
frame.pack(expand=True)


# Criar e posicionar os rótulos e campos de entrada dentro do frame
label_valor = tk.Label(frame, text="Digite o valor a pagar", font=20)
label_valor.pack()

entry_valor = tk.Entry(frame,font=20)
entry_valor.pack()


label_vencimento = tk.Label(frame, text="Digite o vencimento a pagar", font=20)
label_vencimento.pack()

entry_vencimento = tk.Entry(frame,font=20)
entry_vencimento.pack()

label_descricao = tk.Label(frame, text="Digite o descricao a pagar", font=20)
label_descricao.pack()

entry_descricao = tk.Entry(frame,font=20)
entry_descricao.pack()

btn_registrar=tk.Button(frame,text="Registrar", font=20,
                        # command=Registrar 
                        )
btn_registrar.pack()














root.mainloop()

