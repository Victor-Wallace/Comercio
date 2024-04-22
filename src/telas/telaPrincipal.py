import tkinter as tk



def tela_principal():
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



    frame = tk.Frame(root)
    frame.pack(expand=True)

    def sair():
        #Fechar a janela atual
        root.destroy()

    def ir_tela_registrar():
        #Fechar a janela atual
        root.destroy()
        #Iniciar a tela registrar
        from registrar import tela_registrar
        tela_registrar()
    
    def ir_tela_visualizar():
        #Fechar a janela atual
        root.destroy()
        #Iniciar a tela visualizar
        from visualizar import tela_visualizar
        tela_visualizar()

    def ir_tela_saldo():
        #Fechar a janela atual
        root.destroy()
        #Iniciar a tela saldo
        from saldo import tela_saldo
        tela_saldo()

    btn_registrar = tk.Button(frame, text="Registrar",
                            command=ir_tela_registrar,
                            font=20, width=12 )
    btn_registrar.pack()


    btn_visualizar = tk.Button(frame, text="Visualizar",
                            command=ir_tela_visualizar,
                            font=20, width=12 )
                            
    btn_visualizar.pack()

    btn_saldo = tk.Button(frame, text="Saldo",
                            command=ir_tela_saldo,
                            font=20, width=12 )

    btn_saldo.pack()

    btn_voltar = tk.Button(frame, text="Sair",
                            command=sair,
                            font=20, width=12)
    btn_voltar.pack()



    # Posicionar os botões usando pack()
    btn_registrar.pack(side="left", padx=10)
    btn_visualizar.pack(side="left", padx=10)
    btn_saldo.pack(side="left", padx=10)
    btn_voltar.pack(side="left",pady=10)


    root.mainloop()
