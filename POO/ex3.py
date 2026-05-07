class Pessoa :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dados(self):
        print(f'Nome : {self.nome} Idade : {self.idade}')

    def maioridade(self):
        if self.idade >= 18 :
            return  True
        else:
            return  False
        

p3=Pessoa('Icaro', 21 )
p4=Pessoa('Pedao', 17)
p5=Pessoa('Joao', 31)

pessoas=[]

pessoas.append(p3)
pessoas.append(p4)
pessoas.append(p5)



for pessoa in pessoas:
    pessoa.dados()
    print(pessoa.maioridade())