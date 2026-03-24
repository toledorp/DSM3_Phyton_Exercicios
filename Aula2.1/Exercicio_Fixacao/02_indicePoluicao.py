empresa1 = float(input("Digite o índice de poluição da empresa 1: "))
empresa2 = float(input("Digite o índice de poluição da empresa 2: "))
empresa3 = float(input("Digite o índice de poluição da empresa 3: "))
media = (empresa1 + empresa2 + empresa3) / 3
if media <= 0 and media <= 2:
    print("As empresas estão dentro dos limites de poluição.")
elif media > 3 and media <= 5:
    print("A empresa 1 deve suspender suas atividades por 1 mês.")
elif media > 6 and media <= 7:
    print("As empresas 1 e 2 devem suspender suas atividades por 1 mês.")
elif media > 8:
    print("Todas as empresas devem suspender suas atividades por 1 mês.")
else:    print("Índices de poluição inválidos.")
