import tkinter as tk
from tkinter import messagebox


def CriandoJanela():

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


    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


    return root


if __name__ == "__main__":
    janelaPrincipal = CriandoJanela()
    janelaPrincipal.mainloop()
