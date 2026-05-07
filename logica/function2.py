""" Crie uma função chamada calcular_media que:

Receba uma lista de números inteiros

Retorne a média aritmética dos números

Se a lista estiver vazia, retorne None

No programa principal:

Peça ao usuário para digitar números inteiros separados por espaço

Converta a entrada para uma lista de inteiros

Chame a função calcular_media

Se o retorno for None, informe erro

Caso contrário, mostre a média

Regras

A função não pode usar input()

A função não pode usar print()

Não usar variáveis globais

Código claro e organizado

Tratamento de erro obrigatório """


def calcular_media(lista):
    
    lista_inteira=[]

    for num in lista:
        lista_inteira.append(int(num))

    if len(lista_inteira)==0:
        return None
    else:
        return sum(lista_inteira)/len(lista_inteira)
    

usuario=input('Escreva uma lista de numeros separadamente para descobrir a media : ')
lista_str=usuario.split()
teste=[]
try:
    for num in lista_str:
        teste.append(int(num))

    valor= calcular_media(lista_str)

    print(f'A media dos numeros disponiveis e {valor}')

except ValueError:
    print('ErRo : Escreva somente Numeros Inteiros ! ')