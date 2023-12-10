# operadores in e not in


nome = input('Digite um nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} enstá em {nome}')
elif encontrar not in nome:
    print(f'{encontrar} não está em {nome}')