# # Exercicio 1
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem vindo")

# Exercicio 2
num1 = int(input("Digite o um numero inteiro: "))
num2 = int(input("Digite o primeiro outro numero inteiro: "))

resultado = num1 + num2

print(f"O resultado é {resultado}")

# Exercicio 3

nota1 = float(input("Digite a primeria nota: ")) 
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
media_round = round(media, 1)

print(f"A media das notas é: {media_round}")

# Exercicio 4

nome = input("Infome seu nome: ")
idade = int(input("Infome sua idade: "))
estado = input("Infome seu estado: ")

print(f"{nome} tem {idade} anos e mora no estado {estado}")

# Exercicio Estrutura condicionais 
# Exerciciod 1

temp = float(input("Digite a temperatura em Celsius: "))

if temp >= 30: 
    print("Está muito quente!")
elif temp >= 20 and temp < 30:
    print("Está agradável!")
else:
    print("Está muito frio!")    

# Exercicio 2

age = int(input("Infome a idade: "))

if age < 6:
    tarifa = 0.00
elif age >=6 and age < 18:
    tarifa = 5.00
elif age >= 18 and age < 60: 
    tarifa = 10.00
else:
    tarifa = 0.00

print(f"O valor da tarifa: {tarifa}")

# Exercicio 3 

username = input("Informe o seu username: ")
senha = input("Informe a sua senha: ")

if username == "admin" and senha == "python2025":
    print("Login bem sucedido!")
else:
    print("Credenciais estão incorretas.")

username_correto = "admin" 
senha_correta = "python2025"


# Exercicio 3 outra maneira de fazer

username = input("username:")
senha = input("senha: ")

if (username == username_correto) and (senha == senha_correta):
    print("Login bem sucedido!")
else:
    print("Credenciais estão incorretas.")