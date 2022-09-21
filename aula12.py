n = str(input('Qual o seu nome? '))
if n == 'Lucas':
    print('\033[31mNome bonito!\033[m')
elif n == 'Pedro' or n == 'Maria' or n == 'Paulo':
    print('\033[36mSeu nome é bem popular no Brasil!\033[m')
elif n in 'Ana Cláudia Jéssica Juliana':
    print('\033[41mBelo nome feminino!\033[m')
else:
    print('\033[47mO seu nome é bem normal\033[m')
print('Prazer em te conhecer {}, tenha um bom dia!'.format(n))

