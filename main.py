import random

while True:
    try:
            print("Bem vindo ao gerador de Dados de testes, Para finalizar o programa, digite 'Parar' ")
            print('--------------------------------')

            nomes = ['Gabriel', 'Fernando', 'Isabela', 'Bottano', 'Dalo']
            emails = ['gabrielbottan@gmail.com', 'fernando@gmail.com', 'otavio@gmail.com', 'junior@gmail.com', 'isabela@gmail.com']
            telefones = ['238283823','283823847','923829347','999888765','09129837673']
            cidades = ['Três lagoas','São Paulo','Rio de janeiro','Ilha bela','Ubatuba']
            estados = ['MS','SP','RJ','MA','PR']
            
            escolha = input('Escolha uma ou mais opções a serem geradas aleatariamente:\n [1] - Nome \n [2] - E-mail \n [3] - Telefone \n [4] - Cidade \n [5] - Estado \n Digite uma ou mais das opções (separados por virgula): ')
            
            if escolha.lower() == 'parar':
                print("Você saiu do terminal")
                break

            
            def escolher_opcao(opcao):
                gerador = []
                opcoes = [int(o.strip()) for o in opcao.split(',')]
                for op in opcoes:
                    if op == 1:
                        gerador.append(random.choice(nomes))
                    elif op == 2:
                        gerador.append(random.choice(emails))
                    elif op == 3:
                        gerador.append(random.choice(telefones))
                    elif op == 4:
                        gerador.append(random.choice(cidades))
                    elif op == 5:
                        gerador.append(random.choice(estados))
                    
                    else:
                        print('Por favor escolha um número válido')
            
                return gerador
            
            
            def salvar():
                salvar_ou_nao = input("Você deseja salvar os arqvivos que vão ser gerados? (sim) ou (nao)").lower()
                if salvar_ou_nao == "sim":
                    with open('resultados.txt', 'a') as arquivo:
                        for item in resultado:
                            arquivo.write(str(item) + '\n')
                
            
            resultado = escolher_opcao(escolha)
        
            print(resultado)
            salvar()


    except:
        print("Erro inesperado, por favor tente de novo")         
            
    
          
        
            