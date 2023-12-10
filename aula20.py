primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O {primeiro_valor=} é maior que o {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'O {primeiro_valor=} é menor que o {segundo_valor=}')
else:
    print(f'Os valores {primeiro_valor=} e {segundo_valor=} são iguais')