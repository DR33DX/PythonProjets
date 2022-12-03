dd = int(input('Quantos dias alugados? '))
dkm = int(input('Qauntos KM rodados? '))
c = 60
km = 0.15
dc = dd * c
rkm = dkm * km
t = dc + rkm
print('O total a pagar é de R${:.2f}'.format(t))
