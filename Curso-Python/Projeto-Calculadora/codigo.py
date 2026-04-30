def soma(a, b):
    return a + b 

def sobtracao(a, b):
    return a - b 

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b 

def exibir_menu():
    print("\n=== CAlCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair\n")

def formatar_resultado(resultado):
    if resultado.is_integer():
        resultado_convertido = int(resultado)
        return resultado_convertido
    return resultado

opcoes_validas = {"1", "2", "3", "4", "0"}

resultado_atual = float(input("Informe o valor inicial: "))

while True:
    resultado_formatado = formatar_resultado(resultado_atual)
    print(f"Resultado atual: {resultado_formatado}")
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ")

    if opcao_escolhida == "0":
        print("Encerrando a calculadora.")
        break

    if opcao_escolhida not in opcoes_validas:
        print("Opção inválida.\n")
        continue

    valor_operando = float(input("Digite o próximo valor: ")) 

    if opcao_escolhida == "1":
        resultado_atual = soma(resultado_atual, valor_operando)
    elif opcao_escolhida == "2":
        resultado_atual = sobtracao(resultado_atual, valor_operando)
    elif opcao_escolhida == "3":
        resultado_atual = multiplicacao(resultado_atual, valor_operando)
    elif opcao_escolhida == "4":
        resultado_atual = divisao(resultado_atual, valor_operando)


