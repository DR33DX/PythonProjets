larg = float(input('Digite a largurada parede: '))
altu = float(input('Digite a altura da parede: '))
quad = larg * altu
tint = quad / 2
print('{}mts de altura \n{}mts de largura \nequivale a {:.2f}m² \nnecessario {:.2f}lts de tinta para pintar.'.format(larg, altu, quad, tint))
