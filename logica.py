""" Peça ao usuário para digitar três números inteiros.

Armazene esses números em uma lista.

Sem usar funções prontas como max() ou min(), determine:

O maior número

O menor número

Exiba os dois valores. """

""" user=input('Digite tres numeros inteiros separadamente : ')
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
    print('Digite 3 numeros')  """


#ex2

""" Peça ao usuário três números inteiros.
Seu programa deve ordenar esses três números em ordem crescente e imprimir o resultado.

Regras importantes:

Não pode usar sorted() nem .sort().

Você deve usar apenas comparações e trocas manuais entre variáveis. """

""" #entrada  dos numeros
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

print(numeros) """



""" Você deve escrever um programa em Python que:

Peça ao usuário um número inteiro positivo.

Verifique se o número é primo.

Exiba uma das mensagens: """

""" user0=input('Escreva um numero inteiro positivo :')


try:
    user =int(user0)
    if user==2 or user == 3 or user == 5 :
        print('Seu numero e primo')
    elif  user%5 == 0 or user%3 == 0:
        print('Seu numero nao e primo')
    else:
        print('Seu numero e primo')
except:
    print('Digite apenas um NUMERO INTEIRO POSITIVO') """



""" Peça ao usuário uma sequência de números inteiros, separados por espaço.

Percorra os números uma única vez.

Conte:

Quantos números são pares

Quantos números são ímpares

Ao final, exiba os dois contadores. """
""" try:
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
        print('Digite apenas numeros inteiros positivos' ) """



""" Peça ao usuário números inteiros separados por espaço.

Percorra a sequência uma única vez.

Calcule:

A soma de todos os números

A média dos números

Exiba os dois resultados. """

""" user=input('Escreva separadamente uma lista de numeros inteiros :')

lista=user.split()


soma=0
contador=0
for num in lista:
    numero_atual=int(num)
    contador+=1   
    soma+=numero_atual

print(f'A soma de todos os numeros e igual a {soma} e a media dos numeros e {soma/contador}') """



""" Peça ao usuário uma frase.

Conte:

Quantas vogais existem na frase

Quantas consoantes existem na frase

Considere apenas letras do alfabeto:

Ignore espaços, números e símbolos.

Não diferencie maiúsculas de minúsculas.

Regras

Não usar count()

Não usar expressões regulares

Usar apenas laço, condições e variáveis simples """

""" user=input('Escreva uma frase e descubra quantas vogais e consoanters existem na frase :')

vogais=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consoantes = [
    'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z',
    'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'
]


for letra in user:
    if letra in consoantes: 
        print(f'{letra} consoante')

    elif letra in vogais:
        print(f'{letra} vogal')

    elif letra==' ':
        print('')

    else:
        print(f'{letra} nao e letral') """


""" Peça ao usuário uma sequência de números inteiros, separados por espaço.

Ignore valores inválidos (não inteiros).

Com os números válidos:

Crie uma lista apenas com os números positivos

Crie outra lista apenas com os números negativos

Exiba:

As duas listas

A quantidade de números positivos

A quantidade de números negativos """


""" user=input("me de uma lista de numeros inteiros positivos e negativos separados por espacos : ")

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
    print('Escreva somente numeros')   """ 




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


""" try:
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
    print('Escreva somente NUMEROS INTEIROS !') """




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


""" def calcular_media(lista):
    
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
    print('ErRo : Escreva somente Numeros Inteiros ! ') """


""" Crie uma função chamada somar_numeros que:

Receba uma lista de números inteiros

Retorne a soma total

Se a lista estiver vazia, retorne 0

No programa principal:

Peça ao usuário para digitar números inteiros separados por espaço

Converta a entrada para uma lista de inteiros

Chame a função somar_numeros

Mostre o resultado """


""" def somar_numeros (lista):
    num_int=[]

    for num in lista:
        num_int.append(int(num))

    if len(num_int) == 0:
        return 0
        
    else:
        return sum(num_int)
        

usuario=input('Escreva numeros inteiros separadamente e somaremos todos : ')
lista_numeros=usuario.split()


try:
    numeros=[]
    for num in lista_numeros:
        numeros.append(int(num))

    soma=somar_numeros(lista_numeros)

    if soma > 0:
        print(f'A soma de todos os numeros disponiveis e {soma}')
    
    else:
        print(f'Esta vazia')

except ValueError: 
    print('Escreva somente numeros inteiros') """


""" Crie uma função chamada contar_positivos que:

Receba uma lista de números inteiros

Retorne a quantidade de números maiores que zero

Se a lista estiver vazia, retorne 0

No programa principal:

Peça ao usuário para digitar números inteiros separados por espaço

Converta a entrada para uma lista de inteiros

Chame a função contar_positivos """

""" def contar_positivos(lista):
    positivo=0
    for num in lista:
        
        if len(lista)==0 :
            return 0

        elif num > 0 :
            positivo+=1
    
    return positivo

try:
    usuario=input('Escreva numeros inteiros e retornaremos somente numeros positivos : ')  
    lista_str=usuario.split()

    numeros=[]
    for num in lista_str:
        numeros.append(int(num))

    resultado= contar_positivos(numeros)

    print(f'A quantidade de numeros positivos e de {resultado}')

except ValueError: 
    print('Escreva somente numeros') """


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

""" def existe_negativo (lista):
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
    print('Escreva somente numeros inteiros') """


""" Crie uma função chamada criar_multiplicador que:

Receba um número inteiro fator

Retorne uma função interna

A função interna deve:

Receber um número inteiro

Retornar o valor multiplicado pelo fator

Usar o fator da função externa (closure)

Não usar variáveis globais

Não usar classes

Usar apenas funções """

""" def criar_multiplicador(x):
    fator = x
    def interna(y):
        return fator*y
    return interna
    
externa=criar_multiplicador(100)

print(externa(5)) """


""" Crie uma função chamada criar_contador que:

Receba um número inteiro inicio

Retorne uma função interna

A função interna deve:

Não receber parâmetros

Incrementar o contador em 1 a cada chamada

Retornar o valor atualizado

Usar nonlocal para modificar a variável da função externa """

""" def criar_contador(x):
    user=x

    def interna ():
        nonlocal user
        user+=1 
        return user
    return interna


externa=criar_contador(20)

print(externa())
print(externa())
print(externa())
print(externa())
print(externa()) """


""" Crie uma função chamada criar_contador_duplo que:

Receba dois números inteiros: inicio e passo

Retorne uma função interna

A função interna deve:

Não receber parâmetros

Incrementar o valor atual usando o passo

Retornar o valor atualizado

Usar nonlocal para modificar ambos os estados, se necessário

Regras:

Não usar variáveis globais

Não usar classes

Usar apenas funções

Os estados devem ser preservados entre chamada """

""" def criar_contador_duplo(inicio, passo):
    comeco=inicio
    
    def interna():
        nonlocal comeco
        comeco+= passo
        return comeco
    return interna

externo= criar_contador_duplo(2, 3)

print(externo())
print(externo())
print(externo()) """

""" A função deve retornar outra função (closure).

A função interna deve aceitar um número inteiro por chamada.

O comportamento da função interna muda conforme o estado interno.

Regras de funcionamento

Inicialmente, o acumulador começa em 0.

Cada chamada soma o número recebido ao total interno.

A função interna deve retornar:

O total atual

E a quantidade de vezes que já foi chamada

Se o número recebido for 0, o acumulador deve:

Resetar o total para 0

Resetar o contador de chamadas

Tudo isso deve ser feito sem usar classes, sem variáveis globais. """

""" def acumulador():
    total=0
    chamadas=0
    def interna(num):
        nonlocal total, chamadas

        if num == 0:
            total= 0
            chamadas=0
            return total, chamadas
        
        total += num
        chamadas +=1 
        return total, chamadas
    return interna

externa=acumulador()

print(externa(1))
print(externa(5))
print(externa(3))
print(externa(-7)) """

""" Crie uma função chamada criar_descontador(inicio)

Essa função deve retornar uma função interna

A função interna:

Não recebe parâmetros

A cada chamada, diminui o valor em 1

Retorna o valor atual

O valor inicial deve ser definido apenas na função externa

Não usar variáveis globais

Obrigatório usar nonlocal """

""" def criar_descontador(inicio):
    num=inicio
    def subtracao():
        nonlocal num 

        num -= 1
        return num
    return subtracao

externa= criar_descontador(10)

print(externa())
print(externa())
print(externa())
print(externa())
print(externa())
print(externa())
print(externa())
print(externa())
print(externa()) """

""" Crie uma função chamada criar_controle()

Ela deve retornar uma função interna

A função interna:

Recebe um número inteiro

Se o número for positivo, soma ao total

Se o número for negativo, subtrai do total

Se o número for 0, apenas retorna o total sem alterar

O total inicial deve ser 0

Obrigatório usar nonlocal

Não usar variáveis globais """

""" def criar_controle():
    total=0
    def equacao(num):
        nonlocal total

        if num < 0:
            total += num
            return total
        
        elif num > 0:
            total += num
            return total
        
        else:
            total += num
            return total
        
    return equacao

externa= criar_controle()

print(externa(5))
print(externa(4))
print(externa(-2))
print(externa(0)) """

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

""" def criar_limites(maximo):
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
print(externa(-5)) """

""" def criar_registros ():
    total=0
    historico=[]
    def interna (num):
        nonlocal total, historico

        novo_total=total + num
        total = novo_total
        historico.append(total)

        return total
    
    return interna

externa= criar_registros()

print(externa(5))
print(externa(4))
print(externa(-2))
print(externa(0))
print(externa(10))
print(externa(9)) """

""" def criar_acumulador_travado():
    total=0
    travado= False
    def interna(num):
        nonlocal total, travado
        
        if num == 0:
            travado = True

        novo_total= total + num 

        if travado == False:
            total= novo_total 
            return total

        else :
            total= novo_total - num
            return total

        
        
            
        
    return interna """

""" Crie uma lista vazia chamada pessoas

Peça ao usuário:

nome

endereço

número

Guarde esses dados em um dicionário com as chaves:

"nome"

"endereco"

"numero"

Adicione esse dicionário à lista pessoas

Ao final, imprima a lista inteira """

""" pessoas=[]

nome=input("Informe seu nome :")
endereco=input("Informe seu endereco :")
numero=int(input("Informe seu numero :"))

dicionario={'nome': nome, 'endereco': endereco, 'numero': numero}

pessoas.append(dicionario)

print(pessoas) """

""" Comece com uma lista vazia chamada pessoas

Peça nome, endereço e número

Guarde esses dados em um dicionário

Adicione o dicionário à lista pessoas

Repita esse processo 2 vezes

No final, mostre:

o nome de todas as pessoas cadastradas

o endereço de cada uma """

""" pessoas=[]

for info in range(2):
    
    nome=input("Informe seu nome :")
    endereco=input("Informe seu endereco :")
    numero=int(input("Informe seu numero :"))

    dicionario={'nome': nome, 'endereco': endereco, 'numero': numero}
    pessoas.append(dicionario)


print("\nNomes cadastrados:")
for pessoa in pessoas:
    print(pessoa['nome'])

print("\nEnderecos cadastrados:")
for pessoa in pessoas:
    print(pessoa['endereco']) """

""" Crie uma lista vazia chamada pessoas.

Cadastre 3 pessoas, onde cada pessoa deve ter:

nome

endereço

idade

Para cada pessoa cadastrada, armazene os dados em um dicionário e adicione esse dicionário à lista pessoas.

Após o cadastro:

Mostre apenas os nomes das pessoas cadastradas.

Mostre apenas as idades.

Mostre quantas pessoas têm idade maior ou igual a 18.

Regras

Use for com range.

Use lista e dicionário.

Não use funções ainda.

Não use bibliotecas.

Entrada de dados obrigatoriamente via input. """

""" pessoas=[]
contador=0
for _ in range(3):

    nome=input("Informe seu nome :")
    endereco=input("Informe seu endereco :")
    idade=int(input("Informe sua idade :"))

    if idade >= 18:
        contador +=1

    dicionario={'nome':nome,
                'endereco': endereco, 
                'idade':idade}  

    pessoas.append(dicionario)


print(f'Nomes Cadastrados ')

for pessoa in pessoas:
    print(pessoa['nome'])

for pessoa in pessoas:
    print(pessoa['idade'])

print(f'Numero de maiores de idade  {contador} ') """

""" Cadastre 3 pessoas, armazenando:

nome

endereço

idade

Após o cadastro, o programa deve:

Pedir ao usuário um nome para buscar

Verificar se esse nome existe na lista

Se existir:

Mostrar nome, endereço e idade da pessoa

Se não existir:

Mostrar a mensagem:
"Pessoa não encontrada" """

""" pessoas=[]
for _ in range(3):

    nome=input("Informe seu nome :").lower()
    endereco=input("Informe seu endereco :")
    idade=int(input("Informe sua idade :"))


    dicionario={'nome':nome,
                'endereco': endereco, 
                'idade':idade}  

    pessoas.append(dicionario)

busca=input('Digite aqui o nome da pessoa que desija encontrar :').lower()

for nome in pessoas:
    if nome['nome'] == busca:
        print("Nome:", nome['nome'])
        print("Endereco:", nome['endereco'])
        print("Idade:", nome['idade'])
    else:
        print("Nome não encontrado") """

""" Cadastre 5 pessoas, armazenando:
nome idade
Após o cadastro, o programa deve:

Mostrar apenas os nomes das pessoas maiores de idade"""

""" pessoas=[]
contador=0
for _ in range(2):
    nome=input("Informe seu nome :").lower()
    idade=int(input("Informe sua idade :"))

    dicionario={'nome':nome,
                'idade': idade}
    
    pessoas.append(dicionario)


for registros in pessoas:
    if registros['idade'] >= 18:
        print('Nome:', registros['nome']) 
        contador += 1

print(f'Total de maiores de idade: {contador}') """

""" 1. Cadastre 4 pessoas, armazenando:

nome (em minúsculo)

idade

2. Após o cadastro:

Peça ao usuário um nome

Se o nome existir:

Peça a nova idade

Atualize a idade da pessoa """

""" pessoas=[]
for _ in range(4):
    nome=input("Informe seu nome :").lower()
    idade=int(input("Informe sua idade :"))

    dicionario={'nome': nome,
                'idade': idade}
    
    pessoas.append(dicionario)

busca=input('Escreva um nome para alterar a idade :').lower()


encontrado=False

for registro in pessoas:
    if busca == registro['nome']:
        nova_idade=int(input('Qual a nova idade ?'))
        registro['idade'] = nova_idade
        print(f"Nome : {registro['nome']}")
        print(f"Nova idade : {registro['idade']}")
        encontrado=True

if not encontrado :
    print("Pessoa não encontrada") """

""" pessoas=[]

while True:

    print('1 - Cadastrar pessoa\n 2 - Listar pessoas\n 3- Atualizar idade\n 4 - Remover pessoa\n 5 - Sair')

    user=input('Escolha um qualquer uma dessas opcoes pelo numero :')

    #adicionando a lista

    if user == '1':
        quantidade=int(input('Quantas pessoas deseija adicionar a listas ? '))

        for _ in range(quantidade):
            nome= input('Informar nome :').lower()
            idade=int(input('Informe idade :'))
            

            dicionario={'nome': nome,
                    'idade':idade}
            
            pessoas.append(dicionario)

    # listando pessoas

    if user == '2':
        for registros in pessoas:
            print('Nome :', registros['nome'])
            print('Nova idade :', registros['idade'])

    #adicionando nova idade

    encontrado= False
    if user == '3':
        busca=input('Escreva o nome de quem atualizara a idade :' ).lower()

        nova_idade=int(input('Qual a nova idade ?'))
        for registros in pessoas:
            if registros['nome'] == busca:
               registros['idade'] = nova_idade
               print(f"Nome : {registros['nome']}")
               print(f"Nova idade : {registros['idade']}")
               encontrado=True
            
        if not encontrado :
             print("Pessoa não encontrada")

    # deletando da lista

    encontrado2= False
    if user == '4':
        busca2=input('Escreva o nome de quem ira deletar da lista :' ).lower()

        for i, registros in enumerate(pessoas):
            if registros['nome'] == busca2:
               del pessoas[i]
               encontrado2=True

            
        if not encontrado2 :
            print("Pessoa não encontrada")

    #finalizando

    if user == '5':
        break """

""" cadastro=[]
nome_set=set()    
while (True):
#Menu
    ops=input('Selecione [c]adastrar, [s]air, [l]istar :').lower()

        

        
#cadastrar  
    if ops == 'c':
        user_name= input('Qual o seu nome ? ').lower()
        try:
            user_idade= int(input('Qual o sua idade ? '))
        except ValueError:
            print('Escreva somente caracteres correspondentes')
            continue

        if user_name in nome_set:
            print('Nome ja cadastrado')
            print(nome_set)

        else:
            dicionario={'nome':user_name,
            'idade':user_idade}
            cadastro.append(dicionario)
            nome_set.add(user_name)
            
#listar
    elif ops == 'l':
        for pessoa in cadastro:
            print(f'Nome :{pessoa['nome']}, Idade : {pessoa['idade']} ')
#sair

    elif ops == 's':
        break

    else:
        print('opcao invalida') """
    
""" Após cadastrar 5 pessoas:

Mostre:

Total de pessoas

Média das idades

Pessoa mais velha

Pessoa mais nova

Crie um dicionário usando dictionary comprehension no formato:

{nome: idade}

 Aqui você usa:

lista

dicionário

loop

comparação

compreensão de dicionário """

ages=[]
lista=[]
for _ in range(5):

    cad_name= input('Qual nome a cadastrar ? ')
    
    cad_age= int(input('Qual a idade da pessoa cadastrada ? '))
    ages.append(cad_age)

    dicionario={'nome': cad_name, 'idade': cad_age}
    lista.append(dicionario)
    
print(f'O total de pessoas : {len(ages)}')
print(f'A media de idades : {sum(ages)/len(ages)}')
print(f'Idade mais alta {max(ages)}')
print(f'Idade mais baixa {min(ages)}')

