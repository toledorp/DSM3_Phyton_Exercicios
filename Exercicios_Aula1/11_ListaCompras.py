produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))   
preco = float(input("Digite o preço do produto: "))
total = quantidade * preco
print(f"O total a pagar por {quantidade} unidades de {produto} é: R$ {total:.2f}")