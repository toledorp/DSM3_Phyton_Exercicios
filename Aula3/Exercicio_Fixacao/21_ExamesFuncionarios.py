contador = 1

while contador <= 15:
    nome = input("Digite o nome do funcionário: ")
    sexo = input("Digite o sexo (M/F): ").upper()

    if sexo == "M":
        print(f"{nome} deve fazer o exame.")
    elif sexo == "F":
        print(f"{nome} não precisa fazer o exame.")
    else:
        print("Sexo digitado incorretamente.")

    contador += 1