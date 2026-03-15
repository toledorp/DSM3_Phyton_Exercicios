votos_branco = int(input("Digite o número de votos em branco: "))
votos_nulo = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))
total_votos = votos_branco + votos_nulo + votos_validos
percentual_branco = (votos_branco * 100) / total_votos
percentual_nulo = (votos_nulo * 100) / total_votos
percentual_validos = (votos_validos * 100) / total_votos
print(f"Total de votos: {total_votos}")
print(f"Percentual de votos em branco: {percentual_branco:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulo:.2f}%")
print(f"Percentual de votos válidos: {percentual_validos:.2f}%")