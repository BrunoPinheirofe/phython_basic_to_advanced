frase = 'aaaaaaaaaaasdfghjklssssssssssssssssssssssssssssssssssssssssssssssssssss'


i = 0
letra_atual = ''
qtd_letra_atual = 0
qtd_mais_letras = 0
letra_mais_repetida = ''
 

while i < len(frase):
    frase.lower()
    letra_atual = frase[i]
    if letra_atual.isalpha():
        qtd_letra_atual = frase.count(letra_atual)
        if i == 0 or qtd_letra_atual > qtd_mais_letras:
            qtd_mais_letras = qtd_letra_atual
            letra_mais_repetida = letra_atual
    i += 1
print(f'A letra mais repedita na frase: {frase} foi a {letra_mais_repetida} com a quantidade de {qtd_mais_letras} repetições.')
        

# codigo do professor 
# 
# 
# frase = 'aaaooo'

# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''

# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue

#     qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

#     if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
#         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
#         letra_apareceu_mais_vezes = letra_atual

#     i += 1

# print(
#     'A letra que apareceu mais vezes foi '
#     f'"{letra_apareceu_mais_vezes}" que apareceu '
#     f'{qtd_apareceu_mais_vezes}x'
# )       

        