# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 4)
# if 4 in num:
#     num.remove(4)
# else:
#     print('Não tem o valor 4 na lista')
# print(num)
# print(f'Essa lista tem {len(num)} valores.')
valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

# for c, v in enumerate(valores):
#     print(f'Na posição {c + 1} encontrei o valor {v}.')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
