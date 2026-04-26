def find_smallest_int(lista):
    menor = lista[0]
    
    for item in lista:
        if item < menor:
            menor = item

    return menor

input_entrada = [34, 15, 88, 2]

# Outra maneira 

def find_smallest_int(arr):
    return min(arr)

print(find_smallest_int(input_entrada))
