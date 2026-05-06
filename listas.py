""" lista= ['Icaro', 'Larissa', 'Samuel', 'Filipe']
print(lista[3])

lista[1]='Debora'

del lista[0]


#add ultimo
lista.append('Icaro')
lista.append('Nei')
lista.append('Larissa')

#retira ultimo
lista.pop()

#indice e inserir

lista.insert(0, 'Larissa')
print(lista)

#extendendo
lis_a=[1,2,3]
lis_b=[4,5,6]

lis_a.extend(lis_b)

print(lis_a) """

""" nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']

print(nome3)

_, nome5, *_= ['Mario', 'Helenio', 'Luiza']

print(nome3, _) """
""" compras=[]
while True :
    
    pedido=input('[a]dicionar, [r]emover, [l]istar : ')

    if pedido == 'a':
        item=input('Qual item vai adicionar as compras ? :')
        compras.append(item)
        print('Item adicionado')
        continue

    elif pedido== 'r':
        item_removido=int(input('Qual o indicie do item que deseja retirar ? :'))
        del compras[item_removido]
        print('Item removido')
        continue

    elif pedido=='l':
        for indice, item in enumerate(compras):
            print(indice, item)
        
    
    else:
        print('Escolha apenas entre as opcoes entregues') """
        


""" cliente=input('Qual sao os primeiro 9 digitos do seu CPF ? :')
# transformando string em lista e verificando se tem digitos o suficiente

cpf0=[]
if len(cliente) == 11 :
    for num in cliente:
        cpf0.append(int(num))

      
else:
    print('Digite somente 11 digitos') 


#tirando os 2 ultimas digitos para verificacao

cpf_original = cpf0[:]  # cria cópia

cpf0.pop()
cpf0.pop() 

#fazendo os calculos de verificacao

mult=[]
i=10
for num in cpf0:
        
        num=num*i
        mult.append(num)
        i-=1



#calculo para se obter o penultimo digito
calculo= (sum(mult)*10)%11

if calculo > 9:
     cpf0.append(0)
else:
     cpf0.append(calculo)

#gerando ultimo digito

mult1=[]
i=11
for num in cpf0:
        
        num=num*i
        mult1.append(num)
        i-=1

#ultimo numero

calculo1= (sum(mult1)*10)%11

if calculo1 > 9:
     cpf0.append(0)
else:
     cpf0.append(calculo1)

print(cpf0)


if cpf0 == cpf_original:
     print('CPF valido !!')
else:
     print('CPF invalido >:(') """ 



# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

""" def mult (*args):
    total=1
    for num in args:
        total*=num
    return total

        

res=mult(1, 2, 1)
print(res)



# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

try:
    def im_par (x):
        if x % 2 == 0:
            print(f'{x} e par')

        elif x % 2 != 0:
            print(f'{x} e impar')

    user=float(input('Escreva um numero e decubra se par ou impar :'))

    im_par(user)

except ValueError:
    print('Escreva somente numeros') """