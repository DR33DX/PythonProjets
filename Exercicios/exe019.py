import random
a = input('Digite o 1°nome: ')
b = input('Digite o 2°nome: ')
c = input('Digite o 3°nome: ')
d = input('Digite o 4°nome: ')
lista = [a, b, c, d]
print("O Nome sorteado hoje foi", random.choice(lista))

