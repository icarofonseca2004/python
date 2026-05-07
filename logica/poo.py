""" class Pessoa :
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
p1.mostrar_dados() """


"""class Pessoa :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dados(self):
        print(f'Nome : {self.nome} \n Idade : {self.idade}')

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
    print(f'E maior de idade : {pessoa.maioridade()}') """



"""class Pessoa :

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
       return f"Meu nome e {self.nome} e tenho {self.idade} anos de idade"

pessoas_list=[]
p1=Pessoa('Icaro', 21)
p2=Pessoa('Josepha', 61)
p3=Pessoa('Gustavo', 17)

pessoas_list.append(p1)
pessoas_list.append(p2)
pessoas_list.append(p3)

for pessoa in pessoas_list:
    print(pessoa.apresentar())"""


class Conta :
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    
    #mostrar saldo
    def mostrar_saldo(self):
        return self.saldo

    #depositar
    def depositar (self, deposito):
        self.saldo += deposito
        return f"Seu saldo agora e de {self.saldo}"
    #sacar
    def sacar (self, saque):
        if saque < self.saldo:
            self.saldo -= saque
            return f"Voce sacou {saque} agora seu saldo e de {self.saldo}"

        else :
            return f"Valor maior que o saldo diponivel {self.saldo}"
        
    
c1=Conta('Icaro Ribeiro', 1800)

print(c1.mostrar_saldo())

print(c1.depositar(300))

print(c1.sacar(1000))

print(c1.mostrar_saldo())

print(c1.sacar(10000))