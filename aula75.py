# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(numero: int):
#     return numero * 2
# def triplicar(numero):
#     return numero * 3

# def quatriplicar(numero: int):
#     return numero * 4

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
duplicar = criar_multiplicador(2)
print(duplicar(10))