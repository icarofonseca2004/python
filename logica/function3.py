""" Crie uma função chamada existe_negativo que:

Receba uma lista de números inteiros

Retorne True se existir pelo menos um número negativo

Retorne False caso contrário

Se a lista estiver vazia, retorne False

No programa principal:

Peça ao usuário para digitar números inteiros separados por espaço

Converta a entrada para uma lista de inteiros

Chame a função existe_negativo

Mostre o resultado de forma clara """

def existe_negativo (lista):
    if len(lista)==0:
        return False
    
    for num in lista:
        if num < 0 :
            return True
    
        return False

usuario=input('Escreva numeros inteiros e retornaremos se houver negativos : ')
lista_str=usuario.split()
try:
    numeros=[]
    for num in lista_str:
        numeros.append(int(num))

    resultado=existe_negativo(numeros)
    print(f'Existe número negativo: {resultado}')
   
except ValueError:
    print('Escreva somente numeros inteiros')