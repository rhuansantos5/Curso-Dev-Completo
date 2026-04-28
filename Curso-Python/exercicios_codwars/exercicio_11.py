# def difference_in_ages(ages):
#     mais_velho = max(ages)
#     mais_novo = min(ages)

#     tuple = (mais_novo, mais_velho, (mais_velho - mais_novo))
#     return tuple


# Outra maneira de fazer 
def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))



idades = [16, 22, 31, 44, 3, 38, 27, 41, 88]


print(difference_in_ages(idades))