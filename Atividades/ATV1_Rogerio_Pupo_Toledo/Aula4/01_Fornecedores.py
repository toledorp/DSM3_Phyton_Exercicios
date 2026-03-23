class Fornecedores:
    def __init__(self):
        self.nomeFornecedor = ""
        self.nomeProduto = ""
        self.descricaoProduto = ""

    def cadastrarFornecedor(self):
        self.nomeFornecedor = input("Digite o nome do fornecedor: ")
        self.nomeProduto = input("Digite o nome do produto: ")
        self.descricaoProduto = input("Digite a descrição do produto: ")

    def listarFornecedor(self):
        print("\n--- DADOS DO FORNECEDOR ---")
        print(f"Fornecedor: {self.nomeFornecedor}")
        print(f"Produto: {self.nomeProduto}")
        print(f"Descrição: {self.descricaoProduto}")


if __name__ == "__main__":
    fornecedor = Fornecedores()
    fornecedor.cadastrarFornecedor()
    fornecedor.listarFornecedor()