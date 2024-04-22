from base import CriandoJanela
import tkinter as tk

janelaPrincipal = CriandoJanela()


def botao():
    from tkinter import messagebox

    messagebox.showinfo("Botão Clicado", "Você clicou no botão!")

button = tk.Button(janelaPrincipal, text="Clique aqui", command=botao)
button.pack()

button = tk.Button(janelaPrincipal, text="Clique aqui 2", command=botao)
button.pack()


janelaPrincipal.mainloop()