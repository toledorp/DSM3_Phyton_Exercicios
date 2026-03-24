class Matematica:
    def __init__(self):
        self.nota1 = 0.0
        self.nota2 = 0.0
        self.media = 0.0
        self.nomeAluno = ""

    def inserirNotas(self):
        self.nomeAluno = input("Digite o nome do aluno: ")
        self.nota1 = float(input("Digite a primeira nota: "))
        self.nota2 = float(input("Digite a segunda nota: "))

    def calcularMedia(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def mostrarNomeMedia(self):
        return f"Aluno: {self.nomeAluno} | Média: {self.media:.2f}"


if __name__ == "__main__":
    aluno = Matematica()
    aluno.inserirNotas()
    aluno.calcularMedia()
    print(aluno.mostrarNomeMedia())