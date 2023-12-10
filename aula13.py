# formatação de strings
# f-string

nome = 'Bruno'
peso_em_Kg = 70
altura_em_M = 1.85
imc = peso_em_Kg / altura_em_M ** 2

linha_1 = f'{nome} tem {altura_em_M:.2f} de altura,'
linha_2 = f'pesa {peso_em_Kg:.2f} quilos.'
linha_3 = f'Seu IMC é de {imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

