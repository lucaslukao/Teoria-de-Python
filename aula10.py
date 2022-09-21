n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2) / 2
print('Sua nota foi: {:.1f}'.format(m))
print('Parabéns!' if m >= 6 else 'Estude mais!')
