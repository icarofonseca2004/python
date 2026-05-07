""" Crie uma função chamada criar_limite(maximo)

Ela deve retornar uma função interna

A função interna:

Recebe um número inteiro

Soma esse número a um total interno

Se o total ultrapassar maximo, o total não muda

Retorna o total atual

O total inicial deve ser 0

Obrigatório usar nonlocal

Não usar variáveis globais """

def criar_limites(maximo):
    total=0
    def interna(num):
        nonlocal total

        total += num

        if total > maximo :
            total -= num
            return total

        return total
    return interna


externa= criar_limites(20)

print(externa(5))
print(externa(3))
print(externa(12))
print(externa(3))
print(externa(-5)) 