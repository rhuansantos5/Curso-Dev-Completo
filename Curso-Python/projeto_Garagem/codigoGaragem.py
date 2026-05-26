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

def encontrar_carro(placa):
    carro_encontrado = None

    for carro in lista_Carros:
        if carro["placa"].lower() == placa.lower():
            carro_encontrado = carro
            break

    return carro_encontrado

def cadastrar_carros():
    placa = input("Infome a placa do carro: ").strip()

    if len(placa) == 0:
        print("\nO campo placa não pode ser vazio")
        return

    carro_existente = encontrar_carro(placa)
    if carro_existente != None:
        print(f"\nJá existe um carro cadastrado com a placa {placa}")
        return

    cor = input("Infome a cor do carro: ").strip()
    if len(cor) == 0:
        print("\nO campo cor não pode ser vazio")
        return
    
    modelo = input("Infome o modelo do carro: ").strip()
    if len(modelo) == 0:
        print("\nO campo modelo não pode ser vazio")
        return
    
    try:
        ano = int(input("Infome o ano do carro: "))
    except ValueError:
        print("\nAno inválido. Digite apenas números.")
        return

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

    if len(lista_Carros) == 0:
        print("\nNenhum carro cadastrado.")
        return

    for carro in lista_Carros:
        print(f"Placa: {carro["placa"]} | Modelo:{carro["modelo"]} | Cor:{carro["cor"]} | Ano:{carro["ano"]}")
    
    print("---------------------------------------------------------")    

def editar_carro():
    placa = input("Informe a placa do carro que deseja editar: ").strip()

    carro_existente = encontrar_carro(placa)

    if carro_existente == None:
        print("\nCarro não encontrado com essa placa")
        return

    dicionario_atualizacao = {
        "placa": carro_existente["placa"],
        "cor": carro_existente["cor"],
        "modelo": carro_existente["modelo"],
        "ano":  carro_existente["ano"]
    }

    print("\nPressione ENTER para manter o valor atual.")

    nova_placa = input(f"Nova Placa (Atual: {carro_existente["placa"]}): ").strip()
    if len(nova_placa) > 0:
        if encontrar_carro(nova_placa) != None:
            print("Já existe um carro com essa placa")
            return
        
        dicionario_atualizacao["placa"] = nova_placa

    nova_cor = input(f"Nova cor (Atual: {carro_existente["cor"]}):").strip()
    if len(nova_cor) > 0: 
        dicionario_atualizacao["cor"] = nova_cor

    novo_modelo = input(f"Novo modelo (Atual: {carro_existente["modelo"]}):").strip()
    if len(novo_modelo) > 0: 
        dicionario_atualizacao["modelo"] = novo_modelo

    novo_ano = input(f"Novo ano (Atual: {carro_existente["ano"]}):")
    if len(novo_ano) > 0: 
        try:
            dicionario_atualizacao["ano"] = int(novo_ano)
        except ValueError:
            print("\nAno inválido. Alterações ignoradas.")
            return
        
    carro_existente["placa"] = dicionario_atualizacao["placa"]
    carro_existente["cor"] = dicionario_atualizacao["cor"]
    carro_existente["modelo"] = dicionario_atualizacao["modelo"]
    carro_existente["ano"] = dicionario_atualizacao["ano"]         

    print("\nCarro editado com sucesso!!")   

def deletar_carro():
    placa = input("Informe a placa do carro que deseja deletar: ").strip()

    for carro in lista_Carros:
        if carro["placa"].lower() == placa.lower():
            lista_Carros.remove(carro)
            print("\nCarro deletado")
            return

    print("\nNão encontramos esse carro")    

def exibir_menu():
    print("\n=== GERENCIADOR DE GARAGEM ===")
    print("1 - Cadastrar um novo carro")
    print("2 - Listar carros")
    print("3 - Editar um carro")
    print("4 - Deletar um carro")
    print("5 - Sair")

while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_carros()   
    elif opcao == "2":
        listar_carros()   
    elif opcao == "3":
        editar_carro()
    elif opcao == "4":
        deletar_carro()
    elif opcao == "5":
        print("\nEncerrando o gerenciador de garagem.")    
        break
    else:
        print("\nOpção inválida. Escolha novamente")
        continue