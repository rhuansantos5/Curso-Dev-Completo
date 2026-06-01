def bmi(weight, height):
    imc = weight / height ** 2

    if imc <= 18.5:
        return "Underweight"
    elif imc <= 25.0:
        return "Normal"
    elif imc <= 30.0:
        return "Overweight"
    else:
        return "Obese"


print(bmi(50,1.80))
