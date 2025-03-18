# Lista de colaboradores
colaboradores = [
    {"nome": "Carlos Silva", "documento": "123456789",
        "cargo": "Vendedor", "salario": 3000},
    {"nome": "Ana Souza", "documento": "987654321",
        "cargo": "Gerente", "salario": 5000},
    {"nome": "Mariana Lima", "documento": "456789123",
        "cargo": "Vendedor", "salario": 3200},
    {"nome": "Rafael Costa", "documento": "789123456",
        "cargo": "Analista", "salario": 4000},
]

# lista colaboradores


def listar_colaboradores():
    print("\nLista de Colaboradores:")
    for colab in colaboradores:
        print(
            f"Nome: {colab['nome']}, Documento: {colab['documento']}, Cargo: {colab['cargo']}, Salário: R$ {colab['salario']:.2f}")

# organiza em ordem alfabetica


def listar_alfabetico():
    print("\nColaboradores em Ordem Alfabética:")
    for colab in sorted(colaboradores, key=lambda x: x["nome"]):
        print(
            f"Nome: {colab['nome']}, Cargo: {colab['cargo']}, Salário: R$ {colab['salario']:.2f}")

# lista por salarios


def listar_por_salario():
    print("\nColaboradores por Ordem de Salário:")
    for colab in sorted(colaboradores, key=lambda x: x["salario"]):
        print(
            f"Nome: {colab['nome']}, Cargo: {colab['cargo']}, Salário: R$ {colab['salario']:.2f}")

# lista por cargos


def listar_por_cargo():
    cargo = input("\nDigite o cargo que deseja filtrar: ").strip().capitalize()
    filtrados = [
        colab for colab in colaboradores if colab["cargo"].capitalize() == cargo]

    if filtrados:
        print(f"\nColaboradores com cargo de {cargo}:")
        for colab in filtrados:
            print(f"Nome: {colab['nome']}, Salário: R$ {colab['salario']:.2f}")
    else:
        print("\nNenhum colaborador encontrado com esse cargo.")
