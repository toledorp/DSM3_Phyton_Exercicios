from tkinter import *

class Soma_Numeros:
  def __init__(self):
    self.tela = Tk()
    self.configurar_tela()
    self.criar_componentes()

    #Atributos Privados
    self.__n1 = 0
    self.__n2 = 0
    self.__soma = 0

    @property
    def _n1(self):
        return self.__n1

    @_n1.setter
    def _n1(self, value):
        self.__n1 = value

    @property
    def _n2(self):
        return self.__n2

    @_n2.setter
    def _n2(self, value):
        self.__n2 = value

    @property
    def _soma(self):
        return self.__soma

    @_soma.setter
    def _soma(self, value):
        self.__soma = value

  
  def configurar_tela(self):
    self.tela.title("Aplicação O.O.")
    self.tela.configure(background= "#1e3743")

    largura = 800
    altura = 300

    #PEGA A LARGURA E ALTURA DA TELA DO WINDOWS  
    largura_screen = self.tela.winfo_screenwidth()
    altura_Screen = self.tela.winfo_screenheight()

    #DEFINE O POSICIONAMENTO CENTRALIZADO
    posx = largura_screen / 2 - largura /2
    posy = altura_Screen / 2 - altura / 2

    #CONSTROI A TELA DE ACORDO COM AS DIMENSÕES DA TELA DO WINDONS
    #%d SUBSTIUI CADA NUMERO %CONCATENA CADA VARIAVEL
    self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

  def criar_componentes(self):
    #Criar Frame / padx e pady é espaçamento padding
    self.frame = Frame(self.tela, bg= "#34495e", padx = 20, pady = 20 )
    #pack posiciona de acordo com a tela expand => ocupa espaço na tela ao dedimensionar
    self.frame.pack(expand = True)

    #TITULO
    self.titulo = Label(self.frame, text="Cadastro de Clientes: ")
    self.titulo.grid(row= 0, column= 0, columnspan= 2, pady= 10)

    #NOME - Sticky = alinhamento texto a esquerda
    Label(self.frame, text="Digite o nome: ").grid(row= 1, column= 0, sticky="w", pady= 5)
    self.txt_nome = Entry(self.frame)
    self.txt_nome.grid(row= 1, column= 1, pady= 5)

    #EMAIL - Sticky = alinhamento texto a esquerda
    Label(self.frame, text="Digite o e-mail: ").grid(row= 3, column= 0, sticky="w", pady= 5)
    self.txt_email = Entry(self.frame)
    self.txt_email.grid(row= 3, column= 1, pady= 5)

    #TELEFONE
    #Sticky = alinhamento texto a esquerda
    Label(self.frame, text="Digite o telefone: ").grid(row= 5, column= 0, sticky="w", pady= 5)
    self.txt_fone = Entry(self.frame)
    self.txt_fone.grid(row= 5, column= 1, pady= 5)

    #ENDERECO
    #Sticky = alinhamento texto a esquerda
    Label(self.frame, text="Digite o endereço: ").grid(row= 7, column= 0, sticky="w", pady= 5)
    self.txt_end = Entry(self.frame)
    self.txt_end.grid(row= 7, column= 1, pady= 5)

    #BOTAO
    self.btn_botao = Button(self.frame, text= "MOstrar Dados", command= self.mostrar)
    self.btn_botao.grid(row= 7, column= 0, columnspan= 2, pady= 15)
  
  def mostrar(self):
    #recebendo os valores das caixinhas de texto
    self.__nome = float(self.txt_n1.get())
    self.__n2 = float(self.txt_n2.get())
    self.__soma = self.__n1 + self.__n2

    self.txt_resul.insert(0, self.__soma)
  
  def executar(self):
    self.tela.mainloop()



