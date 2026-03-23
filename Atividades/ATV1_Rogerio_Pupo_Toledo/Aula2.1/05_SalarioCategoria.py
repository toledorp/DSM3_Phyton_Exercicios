salario = float(input("Digite o salário: "))

print("|------ Calculo de Reajuster -------")
print("|Escolha a categoria do funcionário|")
print("------------------------------------")
print("|1 - Categoria A - 10% Aumento     |")
print("|2 - Categoria B - 15% Aumento     |")
print("|3 - Categoria C - 25% Aumento     |")
print("------------------------------------")
opcao = int(input("Digite a opção: "))

match opcao:
    case 1:
        catA = salario + ((salario *10)/100)
        print(f"O Salario atual e de R$ ${salario}")
        print(f"O Salario com reajuste é de R$ ${catA}")
    case 2:
        catB = salario + ((salario *15)/100)
        print(f"O Salario atual e de R$ ${salario}")
        print(f"O Salario com reajuste é de R$ ${catB}")
    case 3:
        catC = salario + ((salario *25)/100)
        print(f"O Salario atual e de R$ ${salario}")
        print(f"O Salario com reajuste é de R$ ${catC}")
    case _:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
