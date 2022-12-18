import time
name = str(input('Digite seu nome completo: ')).strip()
n = name.split()
print('Muito prazer em te conhecer!!')
time.sleep(2)
print('Seu primeiro nome é {}'.format(n[0]))
time.sleep(3)
print('Seu último nome é {}'.format(n[len(n)-1]))