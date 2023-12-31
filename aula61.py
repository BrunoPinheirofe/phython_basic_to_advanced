"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70'.replace('.', '')
*nove_primeiros_numeros, primeiro_digito, segundo_digito = cpf 
nove_primeiros_numeros.pop()
cont = 10
soma = 0

for num in nove_primeiros_numeros:
    
    soma += int(num) * cont
    cont -= 1
soma *= 10
resto = soma % 11 
decimo_digito = 0 if resto > 9 else resto

dez_digitos = nove_primeiros_numeros
dez_digitos.append(decimo_digito)


cont = 11
soma = 0
for num in dez_digitos:
    soma += int(num) * cont
    cont -= 1
resultado = (soma * 10) % 11
ultimo_digito = 0 if resultado > 9 else resultado

if str(decimo_digito) == primeiro_digito and str(ultimo_digito) == segundo_digito:
    print('cpf valido')
else:
    print('cpf invalido')


