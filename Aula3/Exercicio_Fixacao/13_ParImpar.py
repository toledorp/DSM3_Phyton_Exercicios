pares = []
impares = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("\nNúmeros pares:", pares)
print("Números ímpares:", impares)