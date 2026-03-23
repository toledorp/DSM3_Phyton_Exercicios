class Loja:
    def __init__(self):
        self.razaoSocial = ""
        self.cpfCliente = ""
        self.valorCompra = 0.0
        self.qtdItensComp = 0
        self.valorTotalCompra = 0.0

    def inserirDadosLoja(self):
        self.razaoSocial = input("Digite a razão social da loja: ")
        self.cpfCliente = input("Digite o CPF do cliente: ")
        self.valorCompra = float(input("Digite o valor de cada item: "))
        self.qtdItensComp = int(input("Digite a quantidade de itens comprados: "))

    def calcularCompraLoja(self):
        self.valorTotalCompra = self.valorCompra * self.qtdItensComp
        return self.valorTotalCompra

    def mostrarDadosLoja(self):
        return (
            f"\n--- DADOS DA LOJA ---\n"
            f"Razão Social: {self.razaoSocial}\n"
            f"CPF do Cliente: {self.cpfCliente}\n"
            f"Valor por item: R$ {self.valorCompra:.2f}\n"
            f"Quantidade de itens: {self.qtdItensComp}\n"
            f"Valor total da compra: R$ {self.valorTotalCompra:.2f}"
        )


if __name__ == "__main__":
    loja = Loja()
    loja.inserirDadosLoja()
    loja.calcularCompraLoja()
    print(loja.mostrarDadosLoja())