# Exercicio 1 
num_lido = int(input("Indorme um número: "))
somatorio = 0 

while num_lido != 0:
    somatorio += num_lido
    num_lido = int(input("Mais um número: "))

print(f"Somatorio dos numeros: {somatorio}")

# Exercicio 2
 
limite = int(input("informe um numero limite:"))
produtorio = 1 

for i in range(1, limite + 1):
    produtorio = produtorio * i 

print(f"Resultado do produtorio: {produtorio}")


# Exercicio 3 
limite = int(input("Infome um número limite: "))

for i in range(1, limite + 1):
    print(f"Dobro de {i}: {i * 2}")

# Exercicio 4 