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
        if saque <= self.saldo:
            self.saldo -= saque
            return f"Voce sacou {saque} agora seu saldo e de {self.saldo}"

        else :
            return f"Valor maior que o saldo disponivel {self.saldo}"
        
    
c1=Conta('Icaro Ribeiro', 1800)

print(c1.mostrar_saldo())

print(c1.depositar(300))

print(c1.sacar(1000))

print(c1.mostrar_saldo())

print(c1.sacar(10000))