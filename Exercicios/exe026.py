import time
fra = str(input('Digite uma frase: ')).strip().upper()
print('Á letra A aparece {} vezes na frase.'.format(fra.count('A')))
time.sleep(2)
print('A primeira letra A apareceu na posicao {}'.format(fra.count('A') + 1))
time.sleep(3)
print('A letra A apareceu na ultima vez na posicao {}'.format(fra.rfind('A') + 1))
