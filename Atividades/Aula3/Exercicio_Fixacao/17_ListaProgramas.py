linguagens = ["python","c#","Visual Basic","C++","Delphi","Cobol"]
total_caracteres = 0

for linguagem in linguagens:
    if len(linguagem) > 3:
        print(linguagem)
    
    total_caracteres += len(linguagem)

print(f"\nTotal de caracteres: {total_caracteres}")