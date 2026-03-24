vogais = ["a", "e", "i", "o", "u"]

for i in range(10):
    letra = input("Digite uma letra: ").lower()

    if letra in vogais:
        print("É vogal")
    else:
        print("Não é vogal")