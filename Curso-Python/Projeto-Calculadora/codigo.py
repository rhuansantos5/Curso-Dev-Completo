from math import sqrt, log2

def soma(a, b):
    return a + b 

def sobtracao(a, b):
    return a - b 

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b 

def raizQuadrada(a):
    return sqrt(a)

def logaritmo(a):
    return log2(a)


def exibir_menu():
    print("\n=== CAlCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada (do resultado atual)")
    print("6 - Logaritmo base 2 (do resultado atual)")
    print("0 - Sair\n")

def formatar_resultado(resultado):
    if resultado.is_integer():
        resultado_convertido = int(resultado)
        return resultado_convertido
    return resultado

def main():
    opcoes_validas = {"1", "2", "3", "4", "5", "6", "0"}

    try:
        resultado_atual = float(input("Informe o valor inicial: "))
    except ValueError:
        return 


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

        if opcao_escolhida in {"1", "2", "3", "4"}:
            try:
                valor_operando = float(input("Digite o próximo valor: ")) 
            except ValueError:
                print("Número inválido")
                continue

        if opcao_escolhida == "1":
            resultado_atual = soma(resultado_atual, valor_operando)
        elif opcao_escolhida == "2":
            resultado_atual = sobtracao(resultado_atual, valor_operando)
        elif opcao_escolhida == "3":
            resultado_atual = multiplicacao(resultado_atual, valor_operando)
        elif opcao_escolhida == "4":
            try:
                resultado_atual = divisao(resultado_atual, valor_operando)
            except ZeroDivisionError:
                print("Não se pode dividir por 0")
        elif opcao_escolhida == "5":
            try:
                resultado_atual = raizQuadrada(resultado_atual)
            except ValueError:
                print("Não é possivel calcular raiz quadrada de um numero negativo.")    
        elif opcao_escolhida == "6":
            try:
                resultado_atual = logaritmo(resultado_atual)    
            except ValueError:
                print("Logaritmo só é definido para número positivo e diferente de zero.")
main()
