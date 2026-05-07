""" Comece com uma lista vazia chamada pessoas

Peça nome, endereço e número

Guarde esses dados em um dicionário

Adicione o dicionário à lista pessoas

Repita esse processo 2 vezes

No final, mostre:

o nome de todas as pessoas cadastradas

o endereço de cada uma """

pessoas=[]

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
    print(pessoa['endereco'])