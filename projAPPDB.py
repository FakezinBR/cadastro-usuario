import tkinter
from tkinter import *

class janela:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.janela.pack()

        self.titulo = Label(self.janela,text="CADASTRO")
        self.titulo["font"] = ("arial", "12")
        self.titulo.pack()

        self.usuarios = Button(self.janela)
        self.usuarios["text"] = "Usuarios"
        self.usuarios.pack(side=LEFT)


        self.cidades = Button(self.janela)
        self.cidades["text"] = "Cidades"
        self.cidades.pack(side=LEFT)

        self.clientes = Button(self.janela)
        self.clientes["text"] = "Clientes"
        self.clientes.pack(side=LEFT)

        self.sair = Button(self.janela)
        self.sair["text"] = "Fechar"
        self.sair["command"] = self.janela.quit
        self.sair.pack(side=LEFT)




root = Tk()
janela(root)
root.mainloop()