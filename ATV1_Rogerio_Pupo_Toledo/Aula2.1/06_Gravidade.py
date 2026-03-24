pesoT = float(input("Informe seu peso: "))

print("----------------------------------")
print("| Viagens Interstelares          |")
print("|Escolha o planeta a ser visitado|")
print("| 1 - Marcurio                   |")
print("| 2 - Vênus                      |")
print("| 3 - Marte                      |")
print("| 4 - Júpiter                    |")
print("| 5 - Saturno                    |")
print("----------------------------------")

opcao = int(input("Digite a opção: "))

match opcao:
    case 1:
        pesoP = pesoT * 0.37
        print(f"O seu peso no planeta Mercurios será de: {pesoP} kg")
    case 2:
        pesoP = pesoT * 0.88
        print(f"O seu peso no planeta Mercurios será de: {pesoP} kg")
    case 3:
        pesoP = pesoT * 0.38
        print(f"O seu peso no planeta Mercurios será de: {pesoP} kg")
    case 4:
        pesoP = pesoT * 2.64
        print(f"O seu peso no planeta Mercurios será de: {pesoP} kg")
    case 5:
        pesoP = pesoT * 1.15
        print(f"O seu peso no planeta Mercurios será de: {pesoP} kg")
    case _:
        print("Opção invalida.")
