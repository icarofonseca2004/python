class Pessoa :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados (self):
        print(f'Nome : {self.nome} Idade : {self.idade}')

    def aniversario (self):
        self.idade += 1 

p1= Pessoa('Icaro', 21)
p2= Pessoa('Kawn', 22)

p1.mostrar_dados()

p2.mostrar_dados()

print('\n')

p1.aniversario()
p1.mostrar_dados()