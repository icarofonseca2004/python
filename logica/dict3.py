cadastro=[]
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
        print('opcao invalida')
    