class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def mostrar_dados(self):
        return f"Titulo:{self.titulo}\nAutor:{self.autor}\nEmprestado:{self.emprestado}"
    
    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
            return f'{self.titulo} emprestimo feito com exito'
        else:
            return f"{self.titulo} Ja esta emprestado"
        
    def devolver(self):
        if self.emprestado == True:
            self.emprestado = False
            return f'{self.titulo} devolucao feita com exito'
        else:
            return f"{self.titulo} ja esta disponivel"

        






armario = {'livro1':Livro('Biblia','Deus'),

'livro2':Livro('Diario de um banana','Greg'),

'livro3':Livro('Do mil ao milhao','Thiago')}


for livro in armario.values():
    print(f'{livro.mostrar_dados()}\n')

print(armario['livro2'].emprestar())   

for livro in armario.values():
    print(f'{livro.mostrar_dados()}\n')