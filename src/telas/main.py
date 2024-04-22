import tkinter as tk
from tkinter import messagebox

def login():
    # Verificar se o nome de usuário e a senha estão corretos
    if entry_username.get() == "admin" and entry_password.get() == "admin":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        root.destroy()
        from telaPrincipal import tela_principal
        tela_principal()
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")

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
label_username = tk.Label(frame, text="Nome de usuário:", font=20)
label_username.pack()

entry_username = tk.Entry(frame, font=20)
entry_username.pack()

label_password = tk.Label(frame, text="Senha:", font=20)
label_password.pack()

entry_password = tk.Entry(frame, show="*", font=20)  # A senha será mostrada como asteriscos
entry_password.pack()

# Botão de login
btn_login = tk.Button(frame, text="Login", command=login, font=20)
btn_login.pack()

# Executar a interface gráfica
root.mainloop()
