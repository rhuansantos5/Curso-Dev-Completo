# animais = ["Cão", "Gato", "Coelho"]


# print(animais)
# print(animais[0])


# lista_mista = [10, "teclado", 2.60]
# print(lista_mista[-2])

#        0   1   2   3 
# lista = [10, 11, 12, 13]

# print(lista) # [10, 11, 12, 13]

# lista.append(15)
# print(f"lista apos o append {lista}") # [10, 11, 12, 13, 15]

# lista.insert(4,14)
# print(f"Lista apos o insert {lista}") #[10, 11, 12, 13, 14, 15]

# lista.remove(10)
# print(f"Valor depois do remove {lista}") #[11, 12, 13, 14, 15]

# lista.pop(4)
# print(f"Lispa apos o POP {lista}") #[11, 12, 13, 14]

# tam = len(lista) 
# print(f"Tamanho da lista {tam}")  #Tamanho da lista 4

# Tuplas 

# tupla = (10, 20, 30)
# print(f"Tipos de tupla: {type(tupla)}")

# lista_convertida = list(tupla)
# lista_convertida.append(400)

# print(f"Tipo de lista convertida: {type(lista_convertida)}")  #List
# print(lista_convertida)      #[10, 20, 30, 400]

# tupla = tuple(lista_convertida)
# print(f"Tipo de tupla convertida: {type(tupla)}")  #Tuple
# print(tupla)    #(10, 20, 30, 400)

# # Conjuntos 
# a = {1, 2, 3}
# b = {3, 2, 4, 5}

# print(a | b)  # {1, 2, 3, 4, 5} | vai fazer a junção de A e B, mas como é um conjuto ele não repete item 
# print(a & b)  # {2, 3}   & vai pegar os itens que se repetem em A e B
# print(a - b)  # {1}     - vai pegar o que é direfente no elemento A 

# Dicionario 
# dicionario = {
#     "nome": "Rhuan",
#     "estado": "Minas Gerais",
#     "altura": 1.69 
# }

# print(f"Tipo do meu dicionario {type(dicionario)}") #Tipo do meu dicionario <class 'dict'>
# print(dicionario) # {'nome': 'Rhuan', 'estado': 'Minas Gerais', 'altura': 1.69}

# dicionario["linguagem"] = "Python"

# print(f"Dicionario depois da modificacao: {dicionario}") #{'nome': 'Rhuan', 'estado': 'Minas Gerais', 'altura': 1.69, 'linguagem': 'Python'}
