from random import random, randint

# função random vai gerar um numero aleatorio entre 0 e 1

# random() gera números decimais
# (float) aleatórios seguido o
# intervalo 0 - 1, onde 0 está
# incluso e 1 não

resultado_random = random()
print(resultado_random)


# randint gera numeros interiros (int) aleatorios seguindo o intervalo definido pelos parametros (incluindo cada um deles).
resultado_randint = randint(1, 10)
print(resultado_randint)