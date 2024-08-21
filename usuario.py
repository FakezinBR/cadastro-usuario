import tkinter
from tkinter import *

class janelausu:
    def __init__(self, master):
        self.janela = Frame(master)
        self.janela.pack()

        self.idusu = Label(self.janela,text="idUsuario")
        self.idusu["font"] = ("verdana", "10")
        self.idusu.pack(side=LEFT)

        self.idusu = Entry(self.janela)
        self.idusu["text"] = "CODIGO"
        self.idusu.pack(side=LEFT)

        self.buscar = Button(self.janela)
        self.buscar["text"] = "Buscar"
        self.buscar.pack(side=LEFT)

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.nomes = Label(self.janela2,text="Nome:")
        self.nomes["font"] = ("verdana", "10")
        self.nomes.pack(side=LEFT)

        self.nomes = Entry(self.janela2)
        self.nomes.pack(side=LEFT)

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.telefone = Label(self.janela3, text="Telefone:")
        self.telefone["font"] = ("verdana", "10")
        self.telefone.pack(side=LEFT)

        self.telefone = Entry(self.janela3)
        self.telefone.pack(side=LEFT)

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.email = Label(self.janela4, text="E-mail:")
        self.email["font"] = ("verdana", "10")
        self.email.pack(side=LEFT)

        self.email = Entry(self.janela4)
        self.email.pack(side=LEFT)

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.usuario = Label(self.janela5, text="usuario:")
        self.usuario["font"] = ("verdana", "10")
        self.usuario.pack(side=LEFT)

        self.usuario = Entry(self.janela5)
        self.usuario.pack(side=LEFT)

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.senha = Label(self.janela6, text="senha:")
        self.senha["font"] = ("verdana", "10")
        self.senha.pack(side=LEFT)

        self.senha = Entry(self.janela6)
        self.senha.pack(side=LEFT)

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.inserir = Button(self.janela7)
        self.inserir["text"] = "Inserir"
        self.inserir.pack(side=LEFT)

        self.alterar = Button(self.janela7)
        self.alterar["text"] = "Alterar"
        self.alterar.pack(side=LEFT)

        self.excluir = Button(self.janela7)
        self.excluir["text"] = "Excluir"
        self.excluir.pack(side=LEFT)


root = Tk()
janelausu(root)
root.mainloop()