nomes = ["Maria", "João", "Paulo", "Magali"]
localizar = input("Digite um nome para localizar: ")

for nome in nomes:
    if nome == localizar:
        print(f"Nome encontrado: {localizar}")
        break
else:
    print("Nome não encontrado.")