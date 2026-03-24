contador = 1
pontuacao_total = 0

while contador <= 4:
    print("\nAluno {contador}")

    q1 = input("Resposta da Questão 1: ").upper()
    q2 = input("Resposta da Questão 2: ").upper()
    q3 = input("Resposta da Questão 3: ").upper()

    pontos = 0

    if q1 == "A":
        pontos += 1
    if q2 == "C":
        pontos += 1
    if q3 ==  "D":
        pontos +=1

    pontuacao_total += pontos

    print(f"Pontuação deste aluno: {pontos}")
    contador +=1

print(f"\nPontuação final: {pontuacao_total}")