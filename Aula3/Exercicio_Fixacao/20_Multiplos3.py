contador = 0

for i in range(1, 21):
    if i % 3 == 0:
        print(i)
        contador += 1

print(f"\nQuantidade de múltiplos de 3: {contador}")