s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 1000:
        break
    s += n
print(f'A soma dos números foi {s}')