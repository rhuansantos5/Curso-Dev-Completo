def century(year):
    parte_inteira = year // 100
    parte_decimal = year % 100

    if parte_decimal > 0: 
        parte_inteira += 1
 
    return parte_inteira


# Outra maneira de fazer o mesmo codigo 

def century(year):
    return (year + 99) // 100


print(century(2000))