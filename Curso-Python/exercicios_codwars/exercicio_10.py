def partlist(list_entrada):
    lista_resultante = []
    tam_lista = len(list_entrada)
    espaco = " "

    for limite in range(1, tam_lista):
        primeiro_pedaco_sublista = list_entrada[:limite]
        segundo_pedaco_sublista = list_entrada[limite:]

        primeiro_pedaco_str = espaco.join(primeiro_pedaco_sublista)
        segundo_pedaco_pedaco_str = espaco.join(segundo_pedaco_sublista)

        tupla = (primeiro_pedaco_str, segundo_pedaco_pedaco_str)

        lista_resultante.append(tupla)
    
    return lista_resultante


lista =  ["az", "toto", "picaro", "zone", "kiwi"]

print(partlist(lista))


