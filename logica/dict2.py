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