salario_atual = float(input("Digite o salário atual: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))
aumento = salario_atual * (percentual_aumento / 100)
salario_novo = salario_atual + aumento
print(f"O salário novo é: {salario_novo:.2f}")
