import math

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    quadrado = pow(numero, 2)
    print(f"O número é par. O quadrado do número é: {quadrado}")
else:
    cubo = pow(numero, 3)
    print(f"O número é ímpar. O cubo do número é: {cubo}")


