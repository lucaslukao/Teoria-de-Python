# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)
# galera = [['João', 34], ['Marta', 58], ['Roberto', 21], ['Sebastian', 23]]
# #filhosj = [['Arthur', 10], ['Ana', 3]]
# #galera.insert(1, filhosj)
# print(galera)
# print(galera[3][0])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dado = list()
maior = menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Ao total {maior} são maoires e {menor} são menores')
# print(galera)
# for i in galera:
#     print(i)
#     print(f'{i[0]} tem {i[1]} anos de idade.')
