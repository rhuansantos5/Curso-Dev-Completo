# # Exercicio 1 
def aluno(numero_aluno):
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    nota3 = float(input("Digite a terceira nota:"))
    media = (nota1 + nota2 + nota3) / 3
    media = round(media,1)
    print(f"A média do aluno {numero_aluno}: {media}")

aluno(1)
aluno(2)
aluno(3)

# # Exercicio 2

def calcular_velocidade_media(distacia,tempo):
    resultado = distacia / tempo
    resultado = round(resultado, 2)

    return resultado

dist = int(input("Informe a distancia (km): "))
tempo = int(input("Infome o tempo (h): "))

vel_media = calcular_velocidade_media(dist, tempo)

print(f"A velociade média: {vel_media} km/h")

# # Exercicio 3

def notas_aprovadas(lista_notas):
    lista_aprovados = []

    for nota in lista_notas:
        if nota >= 7.0:
            lista_aprovados.append(nota)

    return lista_aprovados

lista_notas_alunos = [10.0, 4.5, 9.0]
lista_resultante = notas_aprovadas(lista_notas_alunos)

print("Notas aprovadas")
print(lista_resultante)

# exercicio 4

produto = {
    "papel" : 2,
    "lapis" : 3,
    "canetas" : 2
}

nome_produto = input("Digite o nome do produto: ").lower()

if nome_produto in produto:
    quantidade = produto[nome_produto]
    print(f"Temos {quantidade} {nome_produto} no estoque")
else:
    print("Produto não cadastrado.")

# exercicio 5

estoque = {
    "mouse" : 50.0,
    "teclado" : 100.0,
}

produto = input("Informe um produto que deseja atualiza o preço? ").lower()



if produto in estoque:
    # Solicita a porcentagem de aumento
    porc_aumento = float(input(f"Infome o porcentual de aumento do {produto}: "))

    # Calcula o novo valor: valor atual + (Valor atual * porcentagem / 100)
    valor_atual = estoque[produto]
    novo_valor = valor_atual + (valor_atual * (porc_aumento / 100))

    # Atualiza o novo valor do produto
    estoque[produto] = round(novo_valor, 2)

    print(f"O novo preço do {produto} é: {estoque[produto]}")
else:
    print("Produto não encontrado no sistema")