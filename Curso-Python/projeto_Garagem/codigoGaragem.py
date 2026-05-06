lista_Carros = [
    {
        "placa": "CSD-2023",
        "cor": "preto",
        "modelo": "Mob",
        "ano": 2021
    },
    {
        "placa": "JDS-2043",
        "cor": "azul",
        "modelo": "Kwid",
        "ano": 2026
    },
    {
        "placa": "CFG-2109",
        "cor": "Amarelo",
        "modelo": "HB20",
        "ano": 2021
    }
]

def cadastrar_carros():
    placa = input("Infome a placa do carro: ")
    cor = input("Infome a cor do carro: ")
    modelo = input("Infome o modelo do carro: ")
    ano = int(input("Infome o ano do carro: "))

    carro = {
        "placa" : placa,
        "cor" : cor,
        "modelo" : modelo,
        "ano" : ano
    }

    lista_Carros.append(carro)
    print("\nCarro cadastrado!")

def listar_carros():
    print("\n-------------------- Lista de carros --------------------")
    for carro in lista_Carros:
        print(f"Placa: {carro["placa"]} | Modelo:{carro["modelo"]} | Cor:{carro["cor"]} | Ano:{carro["ano"]}")
    
    print("---------------------------------------------------------")    

def exibir_menu():
    print("\n=== GERENCIADOR DE GARAGEM ===")
    print("1 - Cadastrar um novo carro")
    print("2 - Listar carros")
    print("3 - Editar um carro")
    print("4 - Deletar um carro")
    print("5 - Sair")

while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_carros()   
    elif opcao == "2":
        listar_carros()   
    elif opcao == "3":
        print("\nAinda vamos implementar essa funcionalidade")
    elif opcao == "4":
        print("\nAinda vamos implementar essa funcionalidade")
    elif opcao == "5":
        print("\nEncerrando o gerenciador de garagem.")    
        break
    else:
        print("\nOpção inválida. Escolha novamente")
        continue