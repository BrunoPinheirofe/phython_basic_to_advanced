string = 'Bruno Pinheiro'
nova_string = ''
tamanho_string = len(string)
contador = 0


while contador < tamanho_string:
    if contador == 0:
        nova_string += '*'
    nova_string += f'{string[contador]}*'
    contador += 1

print(nova_string)



# codigo do professor 

# nome = 'Maria Helena'  # Iteráveis

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)
