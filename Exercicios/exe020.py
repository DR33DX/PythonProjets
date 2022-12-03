import random
n1 = str(input('Digite o Primeiro nome: '))
n2 = str(input('Digite o Segundo nome: '))
n3 = str(input('Digite o Terceiro nome: '))
n4 = str(input('Digite o Quarto e ultimo nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("Ordem de Apresentação")
print(lista)
