""" Crie uma função chamada contar_positivos que:

Receba uma lista de números inteiros

Retorne a quantidade de números maiores que zero

Se a lista estiver vazia, retorne 0

No programa principal:

Peça ao usuário para digitar números inteiros separados por espaço

Converta a entrada para uma lista de inteiros

Chame a função contar_positivos """

def contar_positivos(lista):
    positivo=0
    for num in lista:
        
         if num > 0 :
            positivo+=1
    
    return positivo

try:
    usuario=input('Escreva numeros inteiros e retornaremos somente numeros positivos : ')  
    lista_str=usuario.split()

    numeros=[]
    for num in lista_str:
        numeros.append(int(num))

    resultado= contar_positivos(numeros)
    if len(numeros) == 0:
        print('Lista vazia')
    else:
        print(f'A quantidade de numeros positivos e de {resultado}')

    

except ValueError: 
    print('Escreva somente numeros')