preco_pao = float(input("Digite o preço do pão: R$ "))

print("\nPanificadora Pão de Ontem - Tabela de preços")
for i in range(2, 51, 2):   # somente pares
    total = i * preco_pao
    print(f"{i} pães = R$ {total:.2f}")