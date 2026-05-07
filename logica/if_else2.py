""" Peça ao usuário três números inteiros.
Seu programa deve ordenar esses três números em ordem crescente e imprimir o resultado.

Regras importantes:

Não pode usar sorted() nem .sort().

Você deve usar apenas comparações e trocas manuais entre variáveis. """

#entrada  dos numeros
entrada=input('Escreva tres numeros separados por espaco e vou coloca-los em ordem crescente : ')

separacao= entrada.split()

#adicionando-os a lista
numeros=[]
for num in separacao:
    numeros.append(int(num))

#anti erro
if len(numeros) < 3 or len(numeros) > 3 or numeros[0] == numeros[1] == numeros[2] :
    print('Algo esta errado digite tres numeros diferentes corretamente !!')
else :
    for num in numeros:
        i=numeros[0]
        if numeros[0] > numeros[1]:
            numeros.pop(0)
            numeros.append(i)

print(numeros) 