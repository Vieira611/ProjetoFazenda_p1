admins = []
clientes = []

op = -99
while op != 3:
    print('---------MENU---------')
    print('1 - Cadastrar-se')
    print('2 - Fazer login')
    print('3 - Encerrar programa')
    op = int(input('Digite a opção desejada:\n'))
    if op == 1:
        existe = False
        usr = input('Digite o nome de usuário que você deseja utilizar:\n')
        senha = input('Digite sua senha:\n')
        for cliente in clientes:
            if usr == cliente[1]:
                existe = True
        if existe:
            print("Erro! Nome de usuário já existente.")
        else:
            clientes.append([usr,senha])
            print("Cadastro realizado com sucesso!")
    if op == 2:
        op2 = 0
        print("1 - Logar como adm")
        print("2 - Logar como cliente")
        op2 = int(input("\n ->"))
        if op2 == 1:
            login_adm = input('Digite o seu nome de usuário:\n')
            senha_adm = input('Digite sua senha:\n')
            busca = ([login_adm, senha_adm])
            for u in range(len(admins)):
                if busca == admins[u]:
                    print('Login como administrador efetuado com sucesso!')
                    while True:
                        print('----MENU ADM----')
                        print('1 - Gerenciar rebanho')
                        print('2 - Gerenciar produção e derivados')
                        ma = int(input('Escolha uma das opções mostradas acima:\n'))
                        if ma == 1:
                            print('1 - Cadastrar animal')
                            print('2 - Buscar animal')
                            print('3 - Atualizar cadastro de animal')
                            print('4 - Remover animal')
                            print('5 - <- Voltar.')
                            gr = int(input('Escolha uma das opções:\n'))
                            if gr != 1 and gr != 2 and gr != 3 and gr != 4:
                                print('A opção que você digitou não existe. Digite uma opção válida!')
                                continue
                            if gr == 1:
                                tp = input('Insira o tipo de animal:\n')
                                num = int(input('Insira o número do animal:\n'))
                                st = input('Informe o status do animal:\n')

                        else:
                            print("Erro! Tente novamente...")
                            break
                else:
                    print("Erro! Usuário e/ou senha incorretos.")
        if op2 == 2:
            login_cli = input("Usuário:")
            senha_cli = input("Senha:")
            for u in range(len(clientes)):
                if busca == clientes[u]:
                    print('Login como cliente efetuado com sucesso!')
                else:
                    print("Erro! Tente novamente...")


