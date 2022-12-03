from time import sleep

num = int(input('Digite um valor de 0 a 9999: '))
u = num // 1 % 10
d = num // 1 % 100
c = num // 1 % 1000
m = num // 1 % 10000
print('Analisando o numero {}'.format(num))
sleep(1)
print('Unidade: {}'.format(u))
sleep(1)
print('Dezena: {}'.format(d))
sleep(1)
print('Centena: {}'.format(c))
sleep(1)
print('Milhar: {}'.format(m))
sleep(1)
print('#######################################################################')
sleep(10)
num1 = str(input('Digite um valor entre 0 a 9999: '))
n1 = str(num)
print('Analisando o numero {}'.format(num1))
sleep(1)
print('Unidade: {}'.format(n1[3]))
sleep(1)
print('Dezena: {}'.format(n1[2]))
sleep(1)
print('Centena: {}'.format(n1[1]))
sleep(1)
print('Milhar: {}'.format(n1[0]))

