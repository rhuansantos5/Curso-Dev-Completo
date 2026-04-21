# Exercicio 1 

paises = ["Brasil", "Eua", "Japao"]

print(paises)

paises.append("China")
print(f"Países depois de adicionar a China: {paises}")

paises.insert(1, "Russia")
print(f"Países depois de adicionar a Russia: {paises}")

paises.remove("Brasil")
print(f"Países depois de remover o Brasil: {paises}")

paises.pop(1)
print(f"Países depois de remover o Eua: {paises}")

print(f"Países totais depois das modificações: {paises}")


# Exercicio 2

carro = {
    "marca": "Fiat",
    "modelo": "Uno",
    "ano": 2012
}

print(f"O carro é um {carro['marca']} {carro['modelo']} do ano {carro['ano']}")


# Exercicio 3

lista = [1, 2, 3, 4, 4, 3, 2, 1]

conjunto_convertido = set(lista)
lista = list(conjunto_convertido)

print(lista)

# Exercicio 4 
