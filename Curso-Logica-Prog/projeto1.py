numero_secreto = 10

tentativa = 0 

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinha o número de 0 a 10: "))

    if tentativa < numero_secreto:
        print("O numero secreto é Maior!")
    elif tentativa > numero_secreto:
        print("O numero secreto é Menor!")
    else:
        print("Acertou!!")

