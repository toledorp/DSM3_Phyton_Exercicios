nomes = ["Luiz", "Ana", "Cristina", "Fernanda", "Maria Alice", "Joaquina"]

opcao = 1

while opcao != 0:
    opcao = int(input("\nDigite 1 para buscar um nome ou 0 para sair: "))

    if opcao == 1:
        procurar = input("Digite um nome para localizar: ")

        for nome in nomes:
            if nome == procurar:
                print(f"Nome encontrado: {procurar}")
                break
        else:
            print("Nome não encontrado.")

    elif opcao == 0:
        print("Aplicação encerrada.")
    else:
        print("Opção inválida.")