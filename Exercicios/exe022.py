nome = str(input('Digite seu nome: '))
print('Nome todo em Maiusculo: ', nome.upper())
print('Nome em Minusculo: ',nome.lower())
s = nome.split()
j = ''.join(s)
print('Quantas letras tem seu nome todo : ', len(j), 'Letras')
print('Seu primeiro nome tem: ', len(s[0]), 'Letras')
print('Seu segundo nome tem: ', len(s[1]), 'Letras')
print('Seu ultimo nome tem: ', len(s[2]), 'Letras')
#################################################################

name = str(input('Digite seu nome: ')).strip()
import time
print('Analisando seu nome...')
time.sleep(1.5)
print('Senome em Maiusculo é {}'.format(name.upper()))
print('Seu nome em Minusculo é {}'.format(name.lower()))
print('Seu nome tem ao todo {}'.format(len(name) - name.count(' ')))
#print('Seu primeiro nome tem {} letras,'format(name.count(' ')))
separa = name.split()
print(separa)


