import tkinter as tk

def clique():
    rotulo.config(text="Botão pressionado!")

janela = tk.Tk()
janela.title("Exemplo botão")
janela.geometry("600x600")

rotulo = tk.Label(janela, text="clique no botão!", font=("Arial", 16))
rotulo.pack(padx=10)

rotulo = tk.Button(janela, text="clique no botão!", command=imprimirInfos)
rotulo.pack(padx=10)
janela.mainloop()
