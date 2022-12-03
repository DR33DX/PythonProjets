p = float(input('Digito o preço a ser consultado: '))
vd = p * 0.05
np = p * 0.95
print('Preço original do produto é {}R$ \nO valor do desconto é 5% \nO valor com desconto é {:.2f}R$'.format(p, np))
