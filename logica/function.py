""" Crie uma função chamada analisar_numeros que:

Receba uma lista de números inteiros como parâmetro

Retorne três valores:

quantidade de números positivos

quantidade de números negativos

quantidade de zeros

No programa principal:

Peça ao usuário para digitar números inteiros separados por espaço

Converta a entrada para uma lista de inteiros

Chame a função analisar_numeros

Mostre o resultado de forma clara """


try:
    user=input('Escreva uma lista de NUMEROS e veja quantos positivos, negativos e zeros tem :')
    lista=user.split()

   
    def analisar_numeros(numeros):
        pos=0
        neg=0
        zeros=0

        for num in numeros:
            num=int(num)

            if num > 0 :
                pos +=1
            
            elif num < 0 :
                 neg+=1

            elif num == 0 :
                 zeros+=1
        return pos, neg, zeros

    positivos, negativos, zeros = analisar_numeros(lista) 

    print(f'Positivos: {positivos}')
    print(f'Negativos: {negativos}')
    print(f'Zeros: {zeros}')
    
    

except ValueError:
    print('Escreva somente NUMEROS INTEIROS !')