admins = []
clientes = []

op = -99
while op != 3:
    print('---------MENU---------')
    print('1 - Cadastrar usuário')
    print('2 - Fazer login')
    print('3 - Encerrar programa')
    op = int(input('Digite a opção desejada:\n'))
    if op == 1:
        print('1 - Cadastrar administrador')
        print('2 - Cadastrar cliente')
        ac = int(input('Escolha uma das opções mostradas acima:\n'))
        if ac != 1 and ac != 2:
            print('A opção que você digitou não existe. Digite uma opção válida!')
            continue
        if ac == 1:
            usr = input('Digite o nome de usuário que você deseja utilizar:\n')
            senha = input('Digite sua senha:\n')
            admins.append([usr,senha])
        if ac == 2:
            usr = input('Digite o nome de usuário que você deseja utilizar:\n')
            senha = input('Digite sua senha:\n')
            clientes.append([usr,senha])
    if op == 2:
        usr = input('Digite o seu nome de usuário:\n')
        senha = input('Digite sua senha:\n')
        busca = ([usr,senha])
        for u in range(len(admins)):
            if busca == admins[u]:
                print('Login como administrador efetuado com sucesso!')
                break
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
                    gr = int(input('Escolha uma das opções:\n'))
                    if gr != 1 and gr != 2 and gr != 3 and gr != 4:
                        print('A opção que você digitou não existe. Digite uma opção válida!')
                        continue
                    if gr == 1:
                        tp = input('Insira o tipo de animal:\n')
                        num = int(input('Insira o número do animal:\n'))
                        st = input('Informe o status do animal:\n')
        for u in range(len(clientes)):
            if busca == clientes[u]:
                print('Login como cliente efetuado com sucesso!')