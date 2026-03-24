e1 = float(input("Digite a estatura da pessoa 1: "))
e2 = float(input("Digite a estatura da pessoa 2: "))
e3 = float(input("Digite a estatura da pessoa 3: "))

# verificar se existem estaturas iguais
if e1 == e2 or e2 == e3 or e1 == e3:
    print("Existem estaturas iguais")

# ordem decrescente
if e1 >= e2 and e1 >= e3:
    if e2 >= e3:
        print(e1, e2, e3)
    else:
        print(e1, e3, e2)

elif e2 >= e1 and e2 >= e3:
    if e1 >= e3:
        print(e2, e1, e3)
    else:
        print(e2, e3, e1)

else:
    if e1 >= e2:
        print(e3, e1, e2)
    else:
        print(e3, e2, e1)