from random import choice

a = str(input('Digite o 1°nome: '))
b = str(input('Digite o 2°nome: '))
c = str(input('Digite o 3°nome: '))
d = str(input('Digite o 4°nome: '))
lista = [a, b, c, d]
escolhido = choice(lista)
print("O Nome sorteado hoje foi", choice(lista))
