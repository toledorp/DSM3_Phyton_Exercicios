compra = float(input("Informe o valor da compra: "))

print("| Código | Condição de pagamento | Desconto % |")
print("-----------------------------------------------")
print("|    1   | À Vista (Espécie)     | 15         |")
print("|    2   | Cartão de Débito      | 10         |")
print("|    3   | Cartão de Crédito     | 5          |")
print("-----------------------------------------------")
opcao = int(input("\nDigite a opção desejada: "))

match opcao:
  case 1:
    vista = compra - ((15/100) * compra)
    print(f"O valor total da compra foi R$ ${compra}")
    print(f"O valor com o desconto é de R$ ${vista:.2f}")
  case 2:
    debito = compra - ((10/100) * compra)
    print(f"O valor total da compra foi R$ ${compra}")
    print(f"O valor com o desconto é de R$ ${debito:.2f}")
  case 3:
    credito = compra - ((5/100) * compra)
    print(f"O valor total da compra foi R$ ${compra}")
    print(f"O valor com o desconto é de R$ ${credito:.2f}")
  case _:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

