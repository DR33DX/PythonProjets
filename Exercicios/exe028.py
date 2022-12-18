import random
from time import sleep
num = int(input('Digite um numero de 0 a 5: '))
sleep(2)
ad = random.randrange(0, 5)
print('Você digitou {}\nSera que esta certa?'.format(num))
sleep(3)
if num == ad:
    print('Você acertou Parabens!!!')
else:
    print('Você errou!!!\nNão desista!!')
    print('Tente novamente!!!')
    sleep(3)
print('Numero foi {}'.format(ad))