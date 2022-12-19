dest = str(input('Nome do destino: ')).strip()
orig = str(input('Nome da origem: ')).strip()
p = float(input('Insira a kilometragen de sua viagem em KM: '))
pkm = 0.5
pkm2 = 0.45
c = p * pkm
c2 = p * pkm2
if p>200:
    print('Sua viagem de {} para {} custará {}'.format(orig, dest, c2))
else:
    print('Sua Viagem de {} para {} custará {}'.format(orig, dest, c))
