nome = 'Lucas'
cores = {'limpa' : '\033[m',
         'cinza': '\033[34m',
         'rosa' : '\033[35m',
         'pretoebranco' : '\033[7;30m'}
print('Prazer em te conhecer {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
