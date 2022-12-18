# ................../PROGRAMA QUE LÊ VELOCIDADE DE UM CARA E APLICA MULTA, SE ESTIVER ACIMA DA VELOCIDADE
from time import sleep
v = float(input('Insira aqui sua velocidade em km: '))
sleep(1.5)
kmp = 80.0
m = 7.0
r = (v - 80.0)
tm = r * m
sleep(1.5)
if v>kmp:
    print('Você passou no radar á {}KM!!! {}KM acima do permitido!!!'.format(v, r))
    sleep(1.5)
    print('Calculando kilometragem...')
    sleep(1.5)
    print('Calculando valores...')
    sleep(1.5)
    print('Valor total á pagar R${}'.format(tm))
else:
    print('Esta dentro da velocidade permitida, Boa viagem!!!')
