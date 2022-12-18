'''import math
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hi = math.pow(ca, co)
print("o valor do Cateto Oposto é: {}".format(co))
print("o valor do Cateto Adjacente é: {}".format(ca))
print("o valor da hipotenusa é: ", math.pow(co, ca))'''
#FORMA SIMPLES SEM MODULOS
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjascente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))
########################################################
#FORMA AVANÇADA USANDO MODULO MATH
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto Adjascente'))
hi = math.hypot(co, ca)
print('A ipotenusa vai medir {:.2f}'.format(hi))

