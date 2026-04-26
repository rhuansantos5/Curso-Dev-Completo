# Calcular media de um array

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Outras maneiras

def find_average(numbers):
    sum = 0

    for num in numbers:
        sum += num
    try:
        return sum/len(numbers)
    except ZeroDivisionError:
        return 0 


def find_average(numbers):
    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return 0 
    
    