n = 1
p = i = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print('Você digitou {} números pares e {} ímpares'.format(p, i))
