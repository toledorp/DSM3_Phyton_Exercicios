valor1, valor2 = map(float, input("Digite dois valores separados por espaço: ").split())
# valor1 = float(input("Digite o primeiro valor: "))
# valor2 = float(input("Digite o segundo valor: "))
soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
if valor2 != 0:
    divisao = valor1 / valor2 
else:
    divisao = "Não é possível dividir por zero"
print(f"A soma é: {soma:.2f}")
print(f"A subtração é: {subtracao:.2f}")
print(f"A multiplicação é: {multiplicacao:.2f}")
print(f"A divisão é: {divisao}")
