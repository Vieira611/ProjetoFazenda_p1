admins = [['f','123'], ['c', '123']]
clientes = []
animais = []
num_anim = 0

op = -99
while op != 3:
    print('---------MENU---------')
    print('1 - Cadastrar-se como cliente')
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
                    op_adm = 0

                    while op_adm != 4:
                        print('----MENU ADM----')
                        print('1 - Gerenciar rebanho')
                        print('2 - Gerenciar produção e derivados')
                        print('3 - Cadastrar novo administrador.')
                        print('4 - <- Sair')
                        op_adm = int(input('Escolha uma das opções mostradas acima:\n'))

                        if op_adm == 1:
                            print('1 - Cadastrar animal')
                            print('2 - Buscar animal')
                            print('3 - Atualizar cadastro de animal')
                            print('4 - Remover animal')
                            print('5 - <- Voltar.')
                            op_rebanho = int(input('Escolha uma das opções:\n'))
                            if op_rebanho != 1 and op_rebanho != 2 and op_rebanho != 3 and op_rebanho != 4 and op_rebanho != 5:
                                print('A opção que você digitou não existe. Digite uma opção válida!')
                                continue

                            if op_rebanho == 1:
                                tipo_anim = input('Insira o tipo de animal:\n')
                                status_anim = input('Informe o status do animal:\n')
                                num_anim += 1
                                animais.append([tipo_anim, status_anim, num_anim])
                                print(f'Seu animal foi cadastrado com sucesso! O número dele é {num_anim}')

                            if op_rebanho == 2:
                                busca = int(input('Informe o número do animal que você deseja buscar:\n'))
                                retorno = []
                                for n in animais:
                                    if busca == n[0]:
                                        retorno.append(n)
                                    print(f'Animal encontrado! {retorno}')




                        if op_adm == 3:
                            novo_nome_adm = input("Digite o nome:")
                            nova_senha_adm = input("Digite a senha: ")
                            if novo_nome_adm in admins:
                                print("Administrador já existente, tente novamente.")
                            else:
                                admins.append([novo_nome_adm, nova_senha_adm])
                                print("Administrador cadastrado com sucesso!")

                        if op_adm == 4:
                            print("Saindo...")

        if op2 == 2:
            login_cli = input("Usuário:")
            senha_cli = input("Senha:")
            busca = ([login_cli, senha_cli])
            for u in range(len(clientes)):
                if busca == clientes[u]:
                    print('Login como cliente efetuado com sucesso!')
                else:
                    print("Erro! Tente novamente...")


