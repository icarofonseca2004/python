""" Peça ao usuário para digitar três números inteiros.

Armazene esses números em uma lista.

Sem usar funções prontas como max() ou min(), determine:

O maior número

O menor número

Exiba os dois valores. """

user=input('Digite tres numeros inteiros separadamente : ')
user1=user.split()
#transformando em lista
lista=[]

for num in user1 :
    lista.append(int(num))

#Descobrindo o mair numero
if len(user1) == 3:
    if lista[0] > lista[1] and lista[0] > lista[2] :
        print(f'O maior numero e {lista[0]}')

    elif lista[1] > lista[0] and lista[1] > lista[2] :
        print(f'O maior numero e {lista[1]}')

    else:
        print(f'O maior numero e {lista[2]}')


    #descobrindo o menor numero

    if lista[0] < lista[1] and lista[0] < lista[2] :
        print(f'O menor numero e {lista[0]}')

    elif lista[1] < lista[0] and lista[1] < lista[2] :
        print(f'O menor numero e {lista[1]}')

    else:
        print(f'O menor numero e {lista[2]}')

else:
    print('Digite 3 numeros') 