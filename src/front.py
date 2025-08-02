from tkinter import *
from conexaob import conecta
import pymysql
from pymysql import Error
from PIL import Image, ImageTk
import customtkinter


class front:
    def __init__(self):
        self.janela = Tk()
        self.escfull=None
        self.escfull=False
        self.cur=None
        self.pedido=[]
        self.datas = ["2025-07-28"]
        self.lista=[]

        ##IMAGENS
        self.expresso = PhotoImage(file='img/expresso.png')
        self.cappuccino = PhotoImage(file='img/cappuccino.png')
        self.latte = PhotoImage(file='img/latte.png')
        self.mocca = PhotoImage(file='img/mocca.png')
        self.pdq = PhotoImage(file='img/paodequeijo.png')
        self.torta = PhotoImage(file='img/torta.png')
        self.pastel = PhotoImage(file='img/pastel.png')
        self.concluido = PhotoImage(file='img/botaoconcluido.png')
        self.confirmar = PhotoImage(file='img/botaoconfirmar.png')
        self.retorno = PhotoImage(file='img/return.png')
        self.lixeira = PhotoImage(file='img/lixeira.png')
        self.voltf5=PhotoImage(file="img/f5.png")
        self.mais = PhotoImage(file="img/mais.png")

    def mysqlconnect(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user='root', 
                password = '',
                db='cafeteria',
                )
            
            self.cur = self.conn.cursor()
            
            # self.conn.close()
        except pymysql.MySQLError as e:
            print(f"Deu erro porra {e}")

    def telacheia(self, event):
        self.escfull = not self.escfull
        self.janela.attributes("-fullscreen", self.escfull)
        
    def window(self, event):
        self.escfull = False
        self.janela.attributes("-fullscreen", False)

    ##FUNÇOES BOTOES
    def confirmardata(self):    
        self.datan = self.dtnova.get()
        self.datas.append(self.datan)
        self.atend.destroy()
        self.telaatend()

    def incompleto(self):
        self.listaorg=", ".join(self.lista)
        self.cur.execute('INSERT INTO barista (pedidocompl) VALUES (%s)',(self.listaorg,))
        self.lista.clear()
        self.garcom.destroy()
        self.telagarcom()

    def Outro(self):
        self.opção1.config(bg="#38312D");self.opção1.config(state=NORMAL)
        self.opção2.config(bg="#38312D");self.opção2.config(state=NORMAL)
        self.opção3.config(bg="#38312D");self.opção3.config(state=NORMAL)
        self.opção4.config(bg="#38312D");self.opção4.config(state=NORMAL)
        self.opção5.config(bg="#38312D");self.opção5.config(state=NORMAL)
        self.opção6.config(bg="#38312D");self.opção6.config(state=NORMAL)
        self.opção7.config(bg="#38312D");self.opção7.config(state=NORMAL)

    def Expresso(self):
        self.produto = "Expresso"
        self.Outro()
        self.opção1.config(state=DISABLED)

    def Cappuccino(self):
        self.produto = "Cappuccino"
        self.Outro()
        self.opção2.config(state=DISABLED)
    def Latte(self):
        self.produto = "Latte"
        self.Outro()
        self.opção3.config(state=DISABLED)
    def Mocca(self):
        self.produto = 'Mocca'
        self.Outro()
        self.opção4.config(state=DISABLED)
    def Torta(self):
        self.produto = "Torta"
        self.Outro()
        self.opção5.config(state=DISABLED)
    def Pdq(self):
        self.produto = 'Pao de Queijo'
        self.Outro()
        self.opção6.config(state=DISABLED)
    def Pastel(self):
        self.produto = "Pastel"
        self.Outro()
        self.opção7.config(state=DISABLED)

    def quantidade(self):
        self.qtns = self.qtn.get()
        self.nnmesa = self.nmesa.get()
        self.feito = (f'{self.nnmesa} - {self.qtns}x {self.produto}')
        self.lista.append (self.feito)
        self.itens.insert(END,self.feito)
        self.qtn.delete(0,END)
        print(self.lista)

    def botoes(self):       
        # frame para botoes
        self.cardapio = Frame(self.garcom)
        self.cardapio.place(x=20,y=120)
        self.digitas = Frame(self.garcom,bg='white',bd=1)
        self.digitas.place(x=860,y=425)

        self.mesaf = Frame(self.garcom,bg='#38312D')
        self.mesaf.place(x=860,y=425)
        self.qtnf = Frame(self.garcom,bg='#38312D')
        self.qtnf.place(x=860,y=450)
        self.botoesf = Frame(self.garcom)
        self.botoesf.place(x=860,y=500)
        # Botoes do cardapio
        self.opção1 = Button(self.cardapio, image=self.expresso, command=self.Expresso,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção1.pack(side='top')
        self.opção2 = Button(self.cardapio, image=self.cappuccino, command=self.Cappuccino,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção2.pack(side='top')
        self.opção3 = Button(self.cardapio, image=self.latte, command=self.Latte,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção3.pack(side='top')
        self.opção4 = Button(self.cardapio, image=self.mocca, command=self.Mocca,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção4.pack(side='top')
        self.opção5 = Button(self.cardapio, image=self.torta, command=self.Torta,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção5.pack(side='top')
        self.opção6 = Button(self.cardapio, image=self.pdq, command=self.Pdq,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção6.pack(side='top')
        self.opção7 = Button(self.cardapio, image=self.pastel, command=self.Pastel,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção7.pack(side='top')

        #Botoes de Controle
        #quantidade:
        self.qtnt = Label(self.qtnf, text="Quantidade ",font=('arial',15, 'bold'),fg="#D9D9D9",bg='#38312D')
        self.qtnt.pack(side='left')
        self.qtn = Entry(self.qtnf, font=100, width=15,bd =0)
        self.qtn.pack(side='right')
        #Mesa
        self.mesa = Label(self.mesaf, text="Mesa ",font=('arial',15, 'bold'),fg="#D9D9D9",bg='#38312D')
        self.mesa.pack(side='left')
        self.nmesa = Entry(self.mesaf, font=100, width=15,bd = 0)
        self.nmesa.pack(side='right')
        #deletar,retornar e adicionar
        self.delete = Button(self.botoesf,image=self.lixeira,bg='#38312D',bd=0,command=self.botaoX)
        self.delete.pack(side='right')
        self.returne = Button(self.botoesf,image=self.retorno,bg='#38312D',bd=0,command=self.botaoReturne)
        self.returne.pack(side='right')
        self.add = Button(self.botoesf,image=self.mais,command=self.quantidade,bg='#38312D',bd=0,)
        self.add.pack(side='left')
        #Lista do q estas a adicionar
        self.itens = Listbox(self.garcom,bg='#38312D',fg="#D9D9D9",font=("Inknut Antiqua", 12), width=30, height=6)
        self.itens.place(x=875, y=75)
        #Concluir
        self.Concluido = Button(self.garcom,image=self.concluido,command=self.incompleto,bg='#38312D',bd=0,)
        self.Concluido.place(x=900,y=575)

    def botaoReturne(self):
        self.Selecionar=self.itens.size()
        if self.Selecionar  >0:
            self.itens.delete(self.Selecionar-1)
            self.lista.pop()
        else:
            print("deu erro irmão")

    def botaoX(self):
        if self.lista:
            self.itens.delete(0,END)
            self.lista.clear()
        else:
            print("X?")


    def mostrar_info(self,data):
        info = Toplevel()
        info.title("Informações do dia")
        info.geometry("800x600")
        info.configure(bg="#38312D")

        titulo = Label(info, text="Detalhes do dia " + data, font=("Inknut Antiqua", 20, "bold"), fg="white", bg="#38312D")
        titulo.pack(pady=30)
        self.cur.execute('SELECT pedido FROM ordem WHERE hora like %s', (f"%{data}%",))
        inter=self.cur.fetchall()
        self.pedbon=[]
        for item in inter:
            self.pedbon.append(item[0])
        pedidobonito="\n".join(self.pedbon)


        texto = Label(info, text=pedidobonito, font=("Inknut Antiqua", 14), fg="#D9D9D9", bg="#38312D")
        texto.pack()

        fechar = customtkinter.CTkButton(
            info, 
            text="Fechar", 
            font=("Inknut Antiqua", 20),
            fg_color="#D9D9D9", 
            text_color="#38312D", 
            width=100, 
            height=40, 
            command=info.destroy,
            corner_radius=30,
            )
        fechar.pack(pady=20)

    def f5(self):
        self.atend.withdraw()
        self.janelabarista.withdraw()
        self.garcom.withdraw()
        self.janela.deiconify()

    def confirmbar(self):
        
        self.confmesa=self.qualmesa.get() 
        self.cur.execute('SELECT pedidocompl FROM barista WHERE pedidocompl LIKE %s',(f"{self.confmesa}%"))
        pedmesa=self.cur.fetchall()
        self.pedmesabonito="\n".join(str(p[0]) for p in pedmesa)
        self.cur.execute('INSERT INTO ordem (pedido) VALUES (%s)',(self.pedmesabonito))
        if self.confmesa == "":
            print("Não selecionaste a mesa")
        else:
            self.cur.execute('DELETE FROM barista where pedidocompl LIKE %s', (f"{self.confmesa}%",))

        self.pedido=[]
        self.janelabarista.destroy()
        self.telabarista()

    def voltar(self):
        try:
            self.janelabarista.withdraw()
        except:
            pass
        try:
            self.garcom.withdraw()
        except:
            pass
        try:
            self.atend.withdraw()
        except:
            pass
        self.janela.deiconify()



    ## OUTRAS TELAS
    def telagarcom(self):
        self.garcom = Toplevel(self.janela)
        if self.janela.attributes("-fullscreen"):
            self.garcom.attributes("-fullscreen", True)
        self.garcom.bind("<F11>", self.telacheia)
        self.garcom.bind("<Escape>", self.window)
        self.garcom.geometry('1280x720')
        self.garcom.title("Garçom")
        self.garcom.config(background='#38312D')
        self.botoes()
        self.back=Button(self.garcom, image=self.st, command=self.voltar, bg="#38312D", borderwidth=0)
        self.back.place(x=0, y=1)
        self.nmenu = Label(self.garcom,text="GARÇOM",font=('Inknut Antiqua', 40,),fg="#D9D9D9",bg='#38312D',)
        self.nmenu.place(x=50,y=-45)
        self.Itens = Label(self.garcom, text="Itens selecionados", font=('Inknut Antiqua', 12,),fg="#D9D9D9",bg='#38312D',)
        self.Itens.place(x=875, y=40)
        linha1= Frame(self.garcom, bg="#D9D9D9", height=1, width=360)        
        linha1.place(x=15,y=100)
        linha2= Frame(self.garcom, bg="#D9D9D9", height=650, width=1)        
        linha2.place(x=850,y=50)

        self.janela.withdraw()

    def telabarista(self):

        # self.janelabarista.withdraw
        self.janelabarista = Toplevel(self.janela)
        if self.janela.attributes("-fullscreen"):
            self.janelabarista.attributes("-fullscreen", True)
        self.janelabarista.bind("<F11>", self.telacheia)
        self.janelabarista.bind("<Escape>", self.window)
        self.janela.withdraw()
        self.janelabarista.title("BARISTA")
        self.st=PhotoImage(file="img/seta.png")
        self.ref=PhotoImage(file="img/f5.png")

        self.janelabarista.configure(bg="#38312D")
        self.janelabarista.title("BARISTA")
        self.janelabarista.bind("<F11>", self.telacheia)
        self.janelabarista.bind("<Escape>", self.window)
        self.janelabarista.geometry("1280x720")
        ped=[]
        self.pedido=[]
        self.cur.execute('SELECT pedidocompl FROM barista')
        ped=self.cur.fetchall()
        for item in ped:
            self.pedido.append(item[0])
        self.mostpedido="\n".join(self.pedido)

        self.fbc=PhotoImage(file="img/botaoconfirmar.png")

        mostrarpedido=Label(self.janelabarista, text=self.mostpedido, font=("Inknut Antiqua Regular", 20), fg="#D9D9D9", bg="#38312D")
        mostrarpedido.grid(row=4, column=0,padx=4,pady=3)

        textoconf=Label(self.janelabarista, text="QUAL MESA DESEJA CONFIRMAR", font=("Inknut Antiqua", 23), fg="#D9D9D9", bg="#38312D")
        textoconf.grid(row=4, column=5, padx=3)

        self.qualmesa=Entry(self.janelabarista, font=30, width=5)
        self.qualmesa.grid(row=5, column=5, pady=2,padx=4)   

        confirmarpedido=Button(self.janelabarista, image=self.fbc, borderwidth=0, cursor="hand2", command=self.confirmbar, bg="#38312D")
        confirmarpedido.grid(row=6, column=5, padx=3, pady=3)


        seta=Button(self.janelabarista, image=self.st,borderwidth=0,bg="#38312D", command=self.voltar)
        seta.grid(row=0, column=0, pady=2, padx=2, sticky="w")

        jan=Label(self.janelabarista, text="BARISTA", font=("Inknut Antiqua", 24), fg="#D9D9D9", bg="#38312D")
        jan.grid(row=1, column=0, pady=3)

        linhab= Frame(self.janelabarista, bg="#D9D9D9", height=1, width=500)        
        linhab.grid(row=3, column=0, pady=3)


    def telaatend(self):
        self.atend=Toplevel(self.janela)
        if self.janela.attributes("-fullscreen"):
            self.atend.attributes("-fullscreen", True)
        self.atend.bind("<F11>", self.telacheia)
        self.atend.bind("<Escape>", self.window)
        self.janela.withdraw()
        self.atend.title("Atendimentos")
        self.atend.geometry("1280x720")
        self.atend.configure(bg="#38312D")

        titulo = Label(self.atend, text="ATENDIMENTOS", font=("Inknut Antiqua", 24, "bold"), fg="white", bg="#38312D")
        titulo.place(x=85,y=10)
        #linhas
        linha01 = Frame(self.atend, bg="#D9D9D9", height=3, width=750)
        linha01.place(x=35,y=100)
        linha02 = Frame(self.atend, bg = '#D9D9D9',height=685, width=3)
        linha02.place(x=785,y=10)

        #listbox
        self.notinhas = Listbox(self.atend,bg='#38312D',fg="#D9D9D9",font=("Inknut Antiqua", 12), width=60, height=12,highlightthickness=0,bd=0)
        self.notinhas.place(x=50,y=110)

        #texto para botoes de data
        self.dia = "        Dia"
        self.mes = "        Mês"
        self.ano = "        Ano"
        self.ate = Label(self.atend,text="ATÉ",font=("Inknut Antiqua", 24, "bold"), fg="white", bg="#38312D")
        self.ate.place(x=975,y=130)
        #Botoes para data minima
        self.dia1 = Entry(self.atend,bd=1, font=(175), width=10)
        self.dia1.place(x=825,y=110,)
        self.dia1.insert(0,self.dia)
        self.dia1.bind("<FocusIn>", self.retirar1)
        self.dia1.bind("<FocusOut>", self.colocar1)

        self.mes1 = Entry(self.atend,bd=1, font=(175), width=10)
        self.mes1.place(x=975,y=110)
        self.mes1.insert(0,self.mes)
        self.mes1.bind("<FocusIn>", self.retirar2)
        self.mes1.bind("<FocusOut>", self.colocar2)

        self.ano1 = Entry(self.atend,bd=1, font=(175), width=10)
        self.ano1.place(x=1125,y=110)
        self.ano1.insert(0,self.ano)
        self.ano1.bind("<FocusIn>", self.retirar3)
        self.ano1.bind("<FocusOut>", self.colocar3)

        #Botoes para data maxima
        self.dia2 = Entry(self.atend,bd=1, font=(175), width=10)
        self.dia2.place(x=825,y=210)
        self.dia2.insert(0,self.dia)
        self.dia2.bind("<FocusIn>", self.retirar4)
        self.dia2.bind("<FocusOut>", self.colocar4)

        self.mes2 = Entry(self.atend,bd=1, font=(175), width=10)
        self.mes2.place(x=975,y=210)
        self.mes2.insert(0,self.mes)
        self.mes2.bind("<FocusIn>", self.retirar5)
        self.mes2.bind("<FocusOut>", self.colocar5)

        self.ano2 = Entry(self.atend,bd=1, font=(175), width=10)
        self.ano2.place(x=1125,y=210)
        self.ano2.insert(0,self.ano)
        self.ano2.bind("<FocusIn>", self.retirar6)
        self.ano2.bind("<FocusOut>", self.colocar6)

        #Buscar
        Busca = Button(self.atend, image=self.concluido,borderwidth=0,bg="#38312D", command=self.busca)
        Busca.place(x=863,y=350)
        #voltar
        seta=Button(self.atend, image=self.st,borderwidth=0,bg="#38312D", command=self.voltar)
        seta.place(x=1,y=1)
    #buscar
    def busca(self):
        self.idia = self.dia1.get();self.imes = self.mes1.get(); self.iano = self.ano1.get()
        self.mdia = self.dia2.get();self.mmes = self.mes2.get(); self.mano = self.ano2.get()
        self.cur.execute(f"select pedido from ordem where hora between '{self.iano}-{self.imes}-{self.idia} 00:00:00' and '{self.mano}-{self.mmes}-{self.mdia} 23:59:59'")
        self.Tudo = self.cur.fetchall()
        self.notinhas.delete(0,END)
        y=1
        for x in self.Tudo:
            itens = "".join(x)
            self.notinhas.insert(y,itens)
            y=y+1

    #textinho dos botoes
    def retirar1(self,event):
        if self.dia1.get() == self.dia:
            self.dia1.delete(0,END)
    def colocar1(self,event):
        if self.dia1.get() == "":
            self.dia1.insert(0,self.dia)

    def retirar2(self,event):
        if self.mes1.get() == self.mes:
            self.mes1.delete(0,END)
    def colocar2(self,event):
        if self.mes1.get() == "":
            self.mes1.insert(0,self.mes)

    def retirar3(self,event):
        if self.ano1.get() == self.ano:
            self.ano1.delete(0,END)
    def colocar3(self,event):
        if self.ano1.get() == "":
            self.ano1.insert(0,self.ano)

    def retirar4(self,event):
        if self.dia2.get() == self.dia:
            self.dia2.delete(0,END)
    def colocar4(self,event):
        if self.dia2.get() == "":
            self.dia2.insert(0,self.dia)

    def retirar5(self,event):
        if self.mes2.get() == self.mes:
            self.mes2.delete(0,END)
    def colocar5(self,event):
        if self.mes2.get() == "":
            self.mes2.insert(0,self.mes)

    def retirar6(self,event):
        if self.ano2.get() == self.ano:
            self.ano2.delete(0,END)
    def colocar6(self,event):
        if self.ano2.get() == "":
            self.ano2.insert(0,self.ano)

    ##TELA INCIAL
    def telainicial(self):
        self.janela.configure(bg="#38312D")
        self.janela.title("STEAMCOFFEE")
        self.janela.bind("<F11>", self.telacheia)
        self.janela.bind("<Escape>", self.window)
        self.icon = PhotoImage(file='img/engrenagem.png')
        self.janela.iconphoto(True, self.icon)
        self.janela.geometry("1280x720")
        # self.janela.resizable(False,False)

        ## TEXTOS
        logo = Label (self.janela, text= "STEAMCOFFEE", font=("Inknut Antiqua Regular", 54), fg="#D9D9D9", bg="#38312D")        
        logo.pack(anchor=CENTER)

        linha= Frame(self.janela, bg="#D9D9D9", height=1, width=500)        
        linha.pack(pady=3)

        subtitulo=Label(self.janela, text="A sua cafeteria dos sonhos!", font=("Inknut Antiqua Regular", 20), fg="#D9D9D9",bg="#38312D")
        subtitulo.pack(pady=3)

        ##FUNDO BOTAO
        self.fbg=PhotoImage(file="img/botaogarcom.png")
        self.fbb=PhotoImage(file="img/botaobarista.png")
        self.fbn=PhotoImage(file="img/botaoatendimentos.png")
        self.st=PhotoImage(file="img/seta.png")

        # BOTOES
        gar=Button(self.janela, image=self.fbg, bg="#38312D",borderwidth=0,cursor="hand2", command=self.telagarcom)
        gar.pack(pady=5)

        bar=Button(self.janela, image=self.fbb, bg="#38312D",borderwidth=0,cursor="hand2", command=self.telabarista)
        bar.pack(pady=5)

        nota=Button(self.janela, image=self.fbn,bg="#38312D",borderwidth=0,cursor="hand2", command=self.telaatend)
        nota.pack(pady=5)

    def ativar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    apli=front()
    apli.mysqlconnect()
    apli.telainicial()
    apli.ativar()   
     