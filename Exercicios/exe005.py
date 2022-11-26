dig = int(input('Digite um valor: '))
ant = dig - 1
dep = dig + 1
print('O antecessor de {} é {}, e seu sucessor é {}.'.format(dig, ant, dep))
# segundo print outra forma de printar usando format, mais usado pra usar uma 
#vez o resultado do input
print('Oantecessor de {} é {}, e seu sucessor é {}'.format(dig, (dig-1), (dig+1)))

