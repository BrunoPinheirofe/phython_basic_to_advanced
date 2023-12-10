# metodo format()

a = 1
b = False
c = 'arroz'

string = 'b = {} a = {} c = {}'
formato = string.format(b, a, c) # passando pela ordem

string = 'b = {1} a = {0} c = {2}'
formato = string.format(a, b, c) #passando pelo indice

string = 'b = {nome2} a = {nome1} c = {nome3}'
formato = string.format(nome2 = b, nome1 = a, nome3 = c) # passando por parametro nomeado
print(formato)