# try except

# try -> tenta executar um bloco de codigo
    
# except -> executa um bloco de codigo caso o try dê erro

numero_str = input('Digite um numero que irei dobra-lo: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro do numero {numero_float} é {numero_float*2}')
except:
    print('O que você digitou não é um numero!')

