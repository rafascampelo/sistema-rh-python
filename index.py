from funcoes import listar_colaboradores, listar_alfabetico, listar_por_cargo, listar_por_salario

while True:
    print("\n=== MENU ===")
    print("1 - Listar Colaboradores")
    print("2 - Relatório Alfabético")
    print("3 - Relatório por Salário")
    print("4 - Listar por Cargo")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_colaboradores()
    elif opcao == "2":
        listar_alfabetico()
    elif opcao == "3":
        listar_por_salario()
    elif opcao == "4":
        listar_por_cargo()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
