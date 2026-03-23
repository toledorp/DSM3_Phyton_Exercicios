nomes = []

for i in range(7):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("\nNomes armazenados:")
for i in range(len(nomes)):
    print(f"Posição {i}: {nomes[i]}")