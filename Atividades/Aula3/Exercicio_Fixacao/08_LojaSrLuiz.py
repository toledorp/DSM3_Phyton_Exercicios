total = 0

while True:
    preco = float(input("Digite o preço da mercadoria (0 para encerrar): R$ "))

    if preco == 0:
        break

    if preco > 0:
        total += preco

print(f"\nTotal da compra: R$ {total:.2f}")

dinheiro = float(input("Valor em dinheiro recebido: R$ "))

if dinheiro >= total:
    troco = dinheiro - total
    print(f"Troco: R$ {troco:.2f}")
else:
    print("Valor insuficiente para pagar a compra.")