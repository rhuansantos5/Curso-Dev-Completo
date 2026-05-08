# def greet(name, owner):
#     if name == owner:
#         return 'Hello boss'
#     else:
#         return 'Hello guest'
    
# # Outra maneira de fazer 

# def greet(name, owner):
#     return f"Hello boss" if name == owner else "Hello guest"

# print(greet("rhuan", "rhuan"))  


# Exercicio2
# def set_alarm(employed, vacation):
#     if employed == True and vacation == False:
#         return True
#     else:
#         return False
    
# # # Outra maneira de fazer

# def set_alarm(employed, vacation):
#     return employed and not vacation


# Exercicio3

def two_sort(array):
    array.sort()

    primeira_palavra = array[0]

    return "***".join(primeira_palavra)

print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))

# # Outra maneira de fazer

def two_sort(array):
    return "***".join(min(array))