def make_negative( number ):
    if number > 0:
        return number * -1
    return number 
    

print(make_negative(10))

# Outra maneira

def make_negative( number ):
    return -number if number>0 else number

print(make_negative(10))

# Outra maneira

def make_negative( number ):
    return -abs(number)  # abs retorna o valor absoluto, como tem um (-) antes do abs ele sempre vai retornar um - antes dos numeros 