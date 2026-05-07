class Pessoa :

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome e {self.nome} e tenho {self.idade} anos de idade")

pessoas_list=[]
p1=Pessoa('Icaro', 21)
p2=Pessoa('Josepha', 61)
p3=Pessoa('Gustavo', 17)

pessoas_list.append(p1)
pessoas_list.append(p2)
pessoas_list.append(p3)

for pessoa in pessoas_list:
    pessoa.apresentar()