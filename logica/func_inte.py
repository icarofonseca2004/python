""" Crie uma função chamada criar_multiplicador que:

Receba um número inteiro fator

Retorne uma função interna

A função interna deve:

Receber um número inteiro

Retornar o valor multiplicado pelo fator

Usar o fator da função externa (closure)

Não usar variáveis globais

Não usar classes

Usar apenas funções """

def criar_multiplicador(x):
    fator = x
    def interna(y):
        return fator*y
    return interna
    
externa=criar_multiplicador(100)

print(externa(5))