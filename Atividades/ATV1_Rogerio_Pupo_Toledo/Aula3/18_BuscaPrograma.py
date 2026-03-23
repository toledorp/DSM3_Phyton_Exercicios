linguagens = ["python","c#","Visual Basic","C++","Delphi","Cobol","Clipper","PHP","Java"]

nome = input("Digite uma linguagem: ")

for i in range(len(linguagens)):
    if linguagens[i].lower() == nome.lower():
        print("Linguagem encontrada!")
        print(f"Posição na lista: {i}")
        break
else:
    print("Linguagem não encontrada.")