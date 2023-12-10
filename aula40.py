while True:
    try:
        numero_1 = input('Digite um numero: ')
        numero_1_int = int(numero_1)
        numero_2 = input('Digite o outro numero: ')
        numero_2_int = int(numero_2)
        operação = input('[+]  - somar \
                     \n[-] - subtrair \
                     \n[*] multiplicar \
                     \n[/] - dividir \
                     \nQual é a operação que deseja fazer?: ').lower()
        
        if operação == '+':
            print(f'{numero_1_int} + {numero_2_int} = {numero_1_int + numero_2_int}')
        elif operação == '-':
            print(f'{numero_1_int} - {numero_2_int} = {numero_1_int - numero_2_int}')
        elif operação == '*': 
            print(f'{numero_1_int} x {numero_2_int} = {numero_1_int * numero_2_int}')
        elif operação == '/':
            print(f'{numero_1_int} / {numero_2_int} = {numero_1_int / numero_2_int}')
        else:
            print('Operação ensolhida não é valida')
        sair = input('Deseja sair? [s]sim: ').lower().startswith('s')
        if sair:
            break
    except:
        print('O que você escolheu não é um numero!')
print('Saindo...')

#codigo do professor
# 
# while True:
    # numero_1 = input('Digite um número: ')
    # numero_2 = input('Digite outro número: ')
    # operador = input('Digite o operador (+-/*): ')
# 
    # numeros_validos = None
# 
    # try:
        # num_1_float = float(numero_1)
        # num_2_float = float(numero_2)
        # numeros_validos = True
    # except:
        # numeros_validos = None
# 
    # if numeros_validos is None:
        # print('Um ou ambos os números digitados são inválidos.')
        # continue
# 
    # operadores_permitidos = '+-/*'
# 
    # if operador not in operadores_permitidos:
        # print('Operador inválido.')
        # continue
# 
    # if len(operador) > 1:
        # print('Digite apenas um operador.')
        # continue
# 
    ##
# 
    # sair = input('Quer sair? [s]im: ').lower().startswith('s')
# 
    # if sair is True:
        # break
#    