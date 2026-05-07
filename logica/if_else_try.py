""" Peça ao usuário uma sequência de números inteiros, separados por espaço.

Percorra os números uma única vez.

Conte:

Quantos números são pares

Quantos números são ímpares

Ao final, exiba os dois contadores. """
try:
    impar=0
    par=0
    num_str=[]
    while True:
        user=input('Digite um numeros inteiros para saber se sao impares ou pares, quando nao quiser mais adicionar digite [s]:')
        
        num_str.append(user)
        print(num_str)
        
        if user == 's' or user == 'S':
                num_str.pop()

                numeros=[]
                for str in num_str:
                    numeros.append(int(str))

                for num in numeros:
                    if num %2 == 0:
                        print(f'{num} e par')
                        par+=1
                       
                    else:
                        print(f'{num} e impar')
                        impar+=1
                            
                            
        print(f'Ao todo sao {par} numeros pares e {impar} numeros impares !')  

except ValueError:
        print('Digite apenas numeros inteiros positivos' )