""" Peça ao usuário uma sequência de números inteiros, separados por espaço.

Ignore valores inválidos (não inteiros).

Com os números válidos:

Crie uma lista apenas com os números positivos

Crie outra lista apenas com os números negativos

Exiba:

As duas listas

A quantidade de números positivos

A quantidade de números negativos """


user=input("me de uma lista de numeros inteiros positivos e negativos separados por espacos : ")

lista=user.split()
contagem_pos=0
contagem_neg=0
positivos=[]
negativos=[]

try:
    for num in lista:
        i =int(num)
        if i > 0 :
            positivos.append(i)
            contagem_pos+=1

        elif i < 0 :
            negativos.append(i) 
            contagem_neg+=1

        else :
            print(f'{i} nao e inteiro ou nao compativel ou neutro')

    print(positivos)
    print(f'Contem {contagem_pos} numeros positivos')
    print(negativos)
    print(f'Contem {contagem_neg} numeros negativos')

except ValueError:
    print('Escreva somente numeros')