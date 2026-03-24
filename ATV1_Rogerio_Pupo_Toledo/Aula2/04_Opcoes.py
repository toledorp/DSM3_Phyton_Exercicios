n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
         
print("Escolha uma opção:")
print("1 - Média Ponderada")
print("2 - Quadrado da soma dos 2 numeros")
print("3 - Cubo do menor número")
opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    media_ponderada = (n1 *2 + n2 * 3) / (2+3)
    print("A média ponderada é:", media_ponderada)
elif opcao == 2:
    quadrado_soma = pow(n1 + n2,2)
    print("O quadrado da soma dos dois números é:", quadrado_soma)
elif opcao == 3:
    menor_numero = min(n1, n2)
    cubo_menor = menor_numero ** 3
    print("O cubo do menor número é:", cubo_menor)
else:
    print("Opção inválida.")
