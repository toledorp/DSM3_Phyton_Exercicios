class Passagem:
    def __init__(self):
        self.nomePassageiro = ""
        self.telefone = ""
        self.RG = ""
        self.localViagem = ""
        self.data = ""
        self.horario = ""
        self.numpoltrona = ""

    def cadastrarDadosPassageiros(self):
        self.nomePassageiro = input("Digite o nome do passageiro: ")
        self.telefone = input("Digite o telefone: ")
        self.RG = input("Digite o RG: ")

    def cadastrarDadosPassagem(self):
        self.localViagem = input("Digite o local da viagem: ")
        self.data = input("Digite a data da viagem: ")
        self.horario = input("Digite o horário da viagem: ")
        self.numpoltrona = input("Digite o número da poltrona: ")

    def mostrarDadosPassageiro(self):
        print("\n--- DADOS DO PASSAGEIRO ---")
        print(f"Nome: {self.nomePassageiro}")
        print(f"Telefone: {self.telefone}")
        print(f"RG: {self.RG}")

    def mostrarDadosPassagem(self):
        print("\n--- DADOS DA PASSAGEM ---")
        print(f"Local da viagem: {self.localViagem}")
        print(f"Data: {self.data}")
        print(f"Horário: {self.horario}")
        print(f"Poltrona: {self.numpoltrona}")


if __name__ == "__main__":
    passagem = Passagem()
    passagem.cadastrarDadosPassageiros()
    passagem.cadastrarDadosPassagem()
    passagem.mostrarDadosPassageiro()
    passagem.mostrarDadosPassagem()