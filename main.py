admins = [['f','123'], ['c', '123']]
clientes = [['BOB', '123']]
animais = [['BOI', 'VENDA', 1],['PORCO', 'VENDA', 2]]
estoque = [['quejo coalho', 50]]
prod_diaria = [estoque, 10]
produtos_a_venda = []
num_anim = 2
id_prod = 0

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
                            op_rebanho = 99
                            while op_rebanho != 6:
                                print('1 - Cadastrar animal')
                                print('2 - Buscar animal')
                                print('3 - Atualizar status de animal')
                                print('4 - Remover animal')
                                print('5 - Listar animais cadastrados')
                                print('6 - <- Voltar.')
                                op_rebanho = int(input('Escolha uma das opções:\n'))
                                if op_rebanho != 1 and op_rebanho != 2 and op_rebanho != 3 and op_rebanho != 4 and op_rebanho != 5 and op_rebanho != 6:
                                    print('A opção que você digitou não existe. Digite uma opção válida!')
                                    continue

                                if op_rebanho == 1:
                                    tipo_anim = input('Insira o tipo de animal:\n')
                                    status_anim = input('Informe o status do animal:\n')
                                    num_anim += 1
                                    animais.append([tipo_anim.upper(), status_anim.upper(), num_anim])
                                    print(f'Seu animal foi cadastrado com sucesso! O número dele é {num_anim}')

                                if op_rebanho == 2:
                                    busca = int(input('Informe o número do animal que você deseja buscar:\n'))
                                    retorno = []
                                    for n in animais:
                                        if busca == int(n[2]):
                                            retorno.append(n)
                                            print(f'Animal encontrado! {retorno}')
                                        if busca != int(n[2]):
                                            print('Erro! Não existe nenhum animal cadastrado com esse número! Tente novamente.')
                                            continue

                                if op_rebanho == 3:
                                    busca = int(input('Informe o número do animal que você deseja atualizar o cadastro:\n'))
                                    for n in animais:
                                        if busca == int(n[2]):
                                            novo_status = input('Informe o status atualizado do animal:\n')
                                            n[1] = novo_status
                                            print('Status do animal atualizado com sucesso!')
                                        else:
                                            print('Erro! Não existe nenhum animal cadastrado com esse número! Tente novamente.')
                                            continue

                                if op_rebanho == 4:
                                    busca = int(input('Informe o número do animal que você deseja remover:\n'))
                                    for n in range(len(animais)):
                                        if busca == animais[n][2]:
                                            index = n
                                            animais.pop(index)

                                if op_rebanho == 5:
                                    for i in range(len(animais)):
                                        print(f"TIPO: {animais[i][0]} | STATUS: {animais[i][1]} | ID: {animais[i][2]}")
                                    print("\n")

                        if op_adm == 2:
                            op_rebanho2 = 0
                            while op_rebanho2 != 4:
                                print("1 - Cadastrar produção diária.")
                                print("2 - Estoque")
                                print("3 - Adicionar produto à venda")
                                print("4 - <- Voltar")
                                op_rebanho2 = int(input())
                                if op_rebanho2 == 1:
                                    op_produtos = 0
                                    while op != 3:
                                        print("1 - Informar litros de leite ordenhados")
                                        print("2 - Adicionar produtos fabricados")
                                        print("3 - Listar estoque")
                                        print("4 - <- Voltar")
                                        op_produtos = int(input())
                                        if op_produtos == 1:
                                            prod_diaria[1] = float(input("Informe a quantidade de litros ordenhados hoje:"))
                                        if op_produtos == 2:
                                            op_produtos2 = 0
                                            print("1 - Queijos")
                                            print("2 - Carnes")
                                            op_produtos2 = int(input())
                                            if op_produtos2 == 1:
                                                op_queijos = 0
                                                print("1 - Queijo coalho | R$50,00/kg")
                                                print("2 - Queijo mussarela | R$45,00/kg")
                                                print("3 - Queijo manteiga | R$35,00/kg")
                                                op_queijos = int(input())
                                                if op_queijos == 1:
                                                    peso_coalho_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                    valor_coalho_quilo = 50
                                                    produto = ["Queijo coalho", peso_coalho_disponivel, valor_coalho_quilo]
                                                    estoque.append(produto)
                                                    escolher_venda = input("Quer colocar o produto à venda?: S/N").upper()
                                                    if escolher_venda == "S":
                                                        produtos_a_venda.append(produto)
                                                        print("Item adicionado à venda!")

                                                elif op_queijos == 2:
                                                    peso_mussarela_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                    valor_mussarela_quilo = 45
                                                    produto = ["Queijo mussarela", peso_mussarela_disponivel]
                                                    estoque.append(produto)
                                                    escolher_venda = input("Quer colocar o produto à venda?: S/N").upper()
                                                    if escolher_venda == "S":
                                                        produtos_a_venda.append(produto)
                                                        print("Item adicionado à venda!")

                                                elif op_queijos == 3:
                                                    peso_manteiga_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                    valor_manteiga_quilo = 35
                                                    produto = ["Queijo manteiga", peso_manteiga_disponivel]
                                                    estoque.append(produto)
                                                    escolher_venda = input("Quer colocar o produto à venda?: S/N").upper()
                                                    if escolher_venda == "S":
                                                        produtos_a_venda.append(produto)
                                                        print("Item adicionado à venda!")

                                            if op_produtos2 == 2:
                                                print("1 - Carne bovina | R$ 58,00")
                                                print("2 - Carne suína | R$39,00 ")
                                                print("3 - Carne de carneiro | R$32,00 ")
                                                print("4 - Frango | R$23,00")
                                                op_carnes = int(input())
                                                if op_carnes == 1:
                                                    peso_bovino_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                    valor_bovino_quilo = 58
                                                    produto = ["Carne bovina", peso_bovino_disponivel]
                                                    estoque.append(produto)
                                                    escolher_venda = input("Quer colocar o produto à venda?: S/N").upper()
                                                    if escolher_venda == "S":
                                                        produtos_a_venda.append(produto)
                                                        print("Item adicionado à venda!")

                                                if op_carnes == 2:
                                                    peso_suino_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                    valor_suino_quilo = 39
                                                    produto = ["Carne suína", peso_suino_disponivel]
                                                    estoque.append(produto)
                                                    escolher_venda = input("Quer colocar o produto à venda?: S/N").upper()
                                                    if escolher_venda == "S":
                                                        produtos_a_venda.append(produto)
                                                        print("Item adicionado à venda!")

                                                if op_carnes == 3:
                                                    peso_carneiro_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                    valor_carneiro_quilo = 32
                                                    produto = ["Carne carneiro", peso_carneiro_disponivel]
                                                    estoque.append(produto)
                                                    escolher_venda = input("Quer colocar o produto à venda?: S/N").upper()
                                                    if escolher_venda == "S":
                                                        produtos_a_venda.append(produto)
                                                        print("Item adicionado à venda!")

                                                if op_carnes == 4:
                                                    peso_frango_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                    valor_frango_quilo = 23
                                                    produto = ["Frango", peso_frango_disponivel]
                                                    estoque.append(produto)
                                                    escolher_venda = input("Quer colocar o produto à venda?: S/N").upper()
                                                    if escolher_venda == "S":
                                                        produtos_a_venda.append(produto)
                                                        print("Item adicionado à venda!")

                                        if op_produtos == 3:
                                            print(f"LITROS DE LEITE: {prod_diaria[1]}")
                                            for i in range(len(estoque)):
                                                print(f"PRODUTO: {estoque[i][0]} | KG's DISPONÍVEIS: {estoque[i][1]}")

                                        if op_produtos == 4:
                                            break






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
                    op_cli = 0
                    while op_cli != 3:
                        print("1 - Efetuar compra")
                        print("2 - Agendar Retirada/Transporte")
                        print("3 - <- Sair")
                        op_cli = int(input())
                        while op_cli == 1:
                            print("1 - Comprar animais")
                            print("2 - Comprar produtos")
                            op_compra = int(input("Informe a opção desejada:\n"))
                            if op_compra == 1:
                                busca_venda = 'VENDA'
                                print("Animais disponíveis: ")
                                for v in range(len(animais)):
                                    if busca_venda == animais[v][1].upper():
                                        print(f"TIPO: {animais[v][0]} | STATUS: {animais[v][1]} | ID: {animais[v][2]}")
                                compra = int(input("Digite o número do animal que você deseja comprar:\n"))
                                busca_compra = compra
                                for n in range(len(animais)):
                                    if busca_compra == animais[n][2]:
                                        print("Compra efetuada com sucesso!")
                                        break
                                    else:
                                        print("Esse animal não está disponível para venda! Escolha um que esteja disponível!")
                                        continue

                            if op_compra == 2:
                                for i in range(len(estoque)):
                                    print(f"PRODUTO: {produtos_a_venda[i][0]} | KG's DISPONÍVEIS: {produtos_a_venda[i][1]} | PREÇO POR KG: {produtos_a_venda[i][2]}")
                                op_compra2 = input("Informe qual produto você deseja comprar:\n").upper()
                                for p in estoque:
                                    if op_compra2 in produtos_a_venda[0]:
                                        peso_compra = float(input("Informe a quantidade em KG's que você deseja comprar:\n"))
                                    else:
                                        print("Erro! Tente novamente...")




                        if op_cli == 3:
                            print("Saindo...")


                else:
                    print("Erro! Tente novamente...")


