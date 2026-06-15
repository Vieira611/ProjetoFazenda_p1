import  _DefMain_, _DefAdmin_, _DefCli_, asyncio
from fpdf import FPDF, XPos, YPos
from agrobr import *

clientes = []
arquivo_cli = open('clientes.txt', 'r')
linhas_adm = arquivo_cli.readlines()
for linha in linhas_adm:
    clientes.append(linha.replace('\n', '').split(','))
arquivo_cli.close()

admins = []
arquivo_adm = open('admin.txt', 'r')
linhas_adm = arquivo_adm.readlines()
for linha in linhas_adm:
    admins.append(linha.replace('\n', '').split(','))
arquivo_adm.close()

animais = [{'numero': '1', 'tipo': 'boi', 'status': 'engorda', 'peso': 500, 'venda': False}]
animais_a_venda = []
estoque = [['Queijo coalho', 50, 50.0], ['Carne bovina', 100, 58.0]]
prod_leite = 10
produtos_a_venda = []
transporte = []
avaliacao = []
vendidos = []
num_anim = len(animais)
id_prod = 0
op = -99
while op != '3':
    _DefMain_.menu()
    op = input("Digite a opção desejada:")

    if op == '1':
        existe = False
        usr = input('Digite o nome de usuário que você deseja utilizar:\n').lower()
        senha = input('Digite sua senha:\n')
        _DefMain_.verificar_usuario(clientes, usr)

        if existe:
            print("Erro! Nome de usuário já existente.")
        else:
            arquivo_cli = open('clientes.txt', 'a')
            arquivo_cli.write('\n' + usr + ',' + senha)
            arquivo_cli.close()
            print("Cadastro realizado com sucesso!")

    if op == '2':
        print("1 - Logar como adm")
        print("2 - Logar como cliente")
        op2 = input("\n ->")

        if op2 != '1' and op2 != '2':
            print('Erro! Tente novamente...')

        if op2 == '1':
            usuario = _DefMain_.verificar_login(admins)
            if True in usuario:
                print('Login como administrador efetuado com sucesso!')
                op_adm = 0

                while op_adm != '8':
                    print('\n----MENU ADM----')
                    print('1 - Gerenciar rebanho')
                    print('2 - Gerenciar produção e derivados')
                    print('3 - Cadastrar novo administrador.')
                    print('4 - Listar Agendamentos de retirada/transporte')
                    print('5 - Listar Produtos avaliados')
                    print('6 - Ranking de produtos mais vendidos')
                    print('7 - Histórico')
                    print('8 - <- Sair')
                    op_adm = input('Escolha uma das opções mostradas acima:\n')

                    if op_adm != '1' and op_adm != '2' and op_adm != '3' and op_adm != '4' and op_adm != '5' and op_adm != '6' and op_adm != '7' and op_adm != '8':
                        print('Erro! Tente novamente...')

                    if op_adm == '1':
                        op_rebanho = 99
                        while op_rebanho != 0:
                            print('1 - Cadastrar animal')
                            print('2 - Buscar animal')
                            print('3 - Colocar animal para venda')
                            print('4 - Atualizar status de animal')
                            print('5 - Remover animal')
                            print('6 - Listar animais cadastrados')
                            print('7 - Calcular média de peso de animal')
                            print('0 - <- Voltar.')
                            op_rebanho = int(input('Escolha uma das opções:\n'))
                            if op_rebanho != 1 and op_rebanho != 2 and op_rebanho != 3 and op_rebanho != 4 and op_rebanho != 5 and op_rebanho != 6 and op_rebanho != 7:
                                print('A opção que você digitou não existe. Digite uma opção válida!')
                                continue

                            if op_rebanho == 1:
                                _DefAdmin_.cadastrar_animais(animais)

                            if op_rebanho == 2:
                                busca = int(input('Informe o número do animal que você deseja buscar:\n'))
                                retorno = []
                                achou = False
                                for n in animais:
                                    if busca == int(n[2]):
                                        achou == True
                                        retorno.append(n)
                                        print(f'Animal encontrado! {retorno}')

                                    if not achou:
                                        print("Animal não encontrado.")

                            if op_rebanho == 3:
                                asyncio.run(_DefAdmin_.venda_animal(animais, animais_a_venda))

                            if op_rebanho == 4:
                                busca = int(input('Informe o número do animal que você deseja atualizar o cadastro:\n'))
                                achou == False
                                for n in animais:
                                    if busca == int(n[2]):
                                        achou == True
                                        novo_status = input('Informe o status atualizado do animal:\n')
                                        n[1] = novo_status
                                        print('Status do animal atualizado com sucesso!')

                                    if not achou:
                                        print("Animal não encontrado.")


                            if op_rebanho == 5:
                                busca = int(input('Informe o número do animal que você deseja remover:\n'))
                                for n in range(len(animais)):
                                    if busca == animais[n][2]:
                                        index = n
                                        animais.pop(index)

                            if op_rebanho == 6:
                                for animal in animais:
                                    print(f"TIPO: {animal['tipo']} | STATUS: {animal['status']} | ID: {animal['numero']} | PESO: {animal['peso']}")
                                print("\n")

                            if op_rebanho == 7:
                                _DefAdmin_.calcular_media_tipo(animais)

                    if op_adm == '2':
                        op_rebanho2 = 0
                        while op_rebanho2 != 4:
                            print("1 - Cadastrar produção diária / Estoque.")
                            print("2 - Adicionar produto à venda")
                            print("3 - Listar produtos à venda")
                            print("4 - <- Voltar")
                            op_rebanho2 = int(input())
                            if op_rebanho2 == 1:
                                acao = 'cadastro'
                                op_produtos = 0
                                while op != 3:
                                    print("1 - Informar litros de leite ordenhados")
                                    print("2 - Adicionar produtos fabricados")
                                    print("3 - Listar estoque")
                                    print("4 - <- Voltar")
                                    op_produtos = int(input())
                                    if op_produtos == 1:
                                        leite_prod = int(input("Informe a quantidade de litros ordenhados hoje:"))
                                        prod_leite += leite_prod
                                        print("Sua produção foi atualizada!")
                                    if op_produtos == 2:
                                        print("1 - Queijos")
                                        print("2 - Carnes")
                                        op_produtos2 = int(input())
                                        if op_produtos2 == 1:
                                            print("1 - Queijo coalho | R$50,00/kg")
                                            print("2 - Queijo mussarela | R$45,00/kg")
                                            print("3 - Queijo manteiga | R$35,00/kg")
                                            print("4 - <- Voltar")
                                            op_queijos = int(input())
                                            if op_queijos == 1:
                                                peso_coalho_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                valor_coalho_quilo = 32
                                                produto = ["Queijo coalho", peso_coalho_disponivel, valor_coalho_quilo]
                                                _DefAdmin_.cadastrar_produto(estoque, produto, produtos_a_venda)
                                                _DefAdmin_.adicionar_historico(acao, produto[0], peso_coalho_disponivel)


                                            elif op_queijos == 2:
                                                peso_mussarela_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                valor_mussarela_quilo = 32
                                                produto = ["Queijo mussarela", peso_mussarela_disponivel, valor_mussarela_quilo]
                                                _DefAdmin_.cadastrar_produto(estoque, produto, produtos_a_venda)
                                                _DefAdmin_.adicionar_historico(acao, produto[0], peso_mussarela_disponivel)

                                            elif op_queijos == 3:
                                                peso_manteiga_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                valor_manteiga_quilo = 32
                                                produto = ["Queijo manteiga", peso_manteiga_disponivel, valor_manteiga_quilo]
                                                _DefAdmin_.cadastrar_produto(estoque, produto, produtos_a_venda)
                                                _DefAdmin_.adicionar_historico(acao, produto[0], peso_manteiga_disponivel)

                                            elif op_queijos == 4:
                                                break

                                        if op_produtos2 == 2:
                                            print("1 - Carne bovina | R$ 58,00")
                                            print("2 - Carne suína | R$39,00 ")
                                            print("3 - Carne de carneiro | R$32,00 ")
                                            print("4 - Frango | R$23,00")
                                            op_carnes = int(input())
                                            if op_carnes == 1:
                                                peso_bovino_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                valor_bovino_quilo = 32
                                                produto = ["Carne bovina", peso_bovino_disponivel, valor_bovino_quilo]
                                                _DefAdmin_.cadastrar_produto(estoque, produto, produtos_a_venda)
                                                _DefAdmin_.adicionar_historico(acao, produto[0], peso_bovino_disponivel)


                                            if op_carnes == 2:
                                                peso_suino_disponivel = int(
                                                    input("Quantos quilos irão pro estoque?: "))
                                                valor_suino_quilo = 32
                                                produto = ["Carne suina", peso_suino_disponivel, valor_suino_quilo]
                                                _DefAdmin_.cadastrar_produto(estoque, produto, produtos_a_venda)
                                                _DefAdmin_.adicionar_historico(acao, produto[0], peso_suino_disponivel)

                                            if op_carnes == 3:
                                                peso_carneiro_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                valor_carneiro_quilo = 32
                                                produto = ["Carne carneiro", peso_carneiro_disponivel, valor_carneiro_quilo]
                                                _DefAdmin_.cadastrar_produto(estoque, produto, produtos_a_venda)
                                                _DefAdmin_.adicionar_historico(acao, produto[0], peso_carneiro_disponivel)

                                            if op_carnes == 4:
                                                peso_frango_disponivel = int(input("Quantos quilos irão pro estoque?: "))
                                                valor_frango_quilo = 32
                                                produto = ["Frango", peso_frango_disponivel, valor_frango_quilo]
                                                _DefAdmin_.cadastrar_produto(estoque, produto, produtos_a_venda)
                                                _DefAdmin_.adicionar_historico(acao, produto[0], peso_frango_disponivel)

                                    if op_produtos == 3:
                                        print(f"LITROS DE LEITE: {prod_leite}")
                                        for i in range(len(estoque)):
                                            print(f"PRODUTO: {estoque[i][0]} | KG's DISPONÍVEIS: {estoque[i][1]}")

                                    if op_produtos == 4:
                                        break

                            if op_rebanho2 == 2:
                                for i in range(len(estoque)):
                                    print(f"PRODUTO: {estoque[i][0]} | KG's DISPONÍVEIS: {estoque[i][1]} | VALOR KG:")

                                escolha_venda = input("Digite o nome do produto que quer adicionar a venda: ")
                                for i in range(len(estoque)):
                                    if escolha_venda == estoque[i][0]:
                                        indice = i
                                        print("1 - Vender parte")
                                        print("2 - Vender tudo")
                                        op_venda = int(input())
                                        if op_venda == 2:
                                            produtos_a_venda.append(estoque[i])
                                            estoque.pop(i)
                                            break

                                        if op_venda == 1:
                                            quilos_vendidos = int(input("KG's - "))
                                            if quilos_vendidos > estoque[i][1] or quilos_vendidos <= 0:
                                                print("Erro! Digite uma quantidade válida!")
                                                break

                                            else:
                                                for v in range(len(produtos_a_venda)):
                                                    achou = False
                                                    if escolha_venda == produtos_a_venda[i][0]:
                                                        achou = True

                                                    if achou:
                                                        produtos_a_venda[i][1] += quilos_vendidos
                                                        estoque[indice][1] -= quilos_vendidos

                                                    if estoque[indice][1] == 0:
                                                        estoque.pop(indice)
                                                        break

                                                    if not achou:
                                                        produtos_a_venda.append([escolha_venda, quilos_vendidos])
                                                        break

                            if op_rebanho2 == 3:
                                for i in range(len(produtos_a_venda)):
                                    print(
                                        f"PRODUTO: {produtos_a_venda[i][0]} | KG's DISPONÍVEIS: {produtos_a_venda[i][1]}")

                    if op_adm == '3':
                        novo_nome_adm = input("Digite o nome:")
                        nova_senha_adm = input("Digite a senha: ")
                        if novo_nome_adm in admins:
                            print("Administrador já existente, tente novamente.")
                        else:
                            admins.append([novo_nome_adm, nova_senha_adm])
                            arquivo_adm = open('admin.txt', 'a')
                            arquivo_adm.write('\n' + novo_nome_adm + ',' + nova_senha_adm)
                            arquivo_adm.close()
                            print("Administrador cadastrado com sucesso!")

                    if op_adm == '4':
                        for t in range(len(transporte)):
                            print(f"CLIENTE: {transporte[t][0]} | DIA AGENDADO: {transporte[t][1]}")

                    if op_adm == '5':
                        for av in range(len(avaliacao)):
                            print(f"PRODUTO: {avaliacao[av][0]} | NOTA: {avaliacao[av][1]/avaliacao[av][2]} | QTD DE AVALIAÇÕES: {avaliacao[av][2]}")

                    if op_adm == '6':
                        for r in range(len(vendidos)):
                            for i in range(r + 1, len(vendidos)):
                                if vendidos[i][1] > vendidos[r][1]:
                                    armazenar = vendidos[r]
                                    vendidos[r] = vendidos[i]
                                    vendidos[i] = armazenar
                        print('Produtos mais vendidos')
                        posicao = 1
                        for v in vendidos:
                            print(f"{posicao}° - PRODUTO: {v[0]} | QUANTIDADE DE VENDAS: {v[1]}")
                            posicao += 1
                        print('\n')

                    if op_adm == '7':
                        print("1 - Consultar Histórico")
                        print("2 - Limpar Histórico")
                        op_hist = input('\n')
                        if op_hist == '1':
                            log = open('log.txt', 'r')
                            linhas_log = log.readlines()
                            for linha in linhas_log:
                                print(linha, end='')
                        if op_hist == '2':
                            log = open('log.txt', 'w')
                            log.write('')
                            log.close()

                    if op_adm == '8':
                        print("Saindo...")

        if op2 == '2':
            usuario = _DefMain_.verificar_login(clientes)
            if True in usuario:
                    print('Login como cliente efetuado com sucesso!')
                    op_cli = 0
                    venda = []
                    while op_cli != 3:
                        print("1 - Efetuar compra")
                        print("2 - Agendar Retirada/Transporte")
                        print("3 - <- Sair")
                        op_cli = int(input())
                        while op_cli == 1:
                            acao = 'compra'
                            print("1 - Comprar animais")
                            print("2 - Comprar produtos")
                            print("3 - Comprar leite")
                            print("4 - Finalizar compra")
                            op_compra = int(input("Informe a opção desejada:\n"))
                            if op_compra == 1:
                                print("Animais disponíveis: ")
                                for animal in animais:
                                    if True == animal['venda']:
                                        print(f"TIPO: {animal['tipo']} | STATUS: {animal['status']} | ID: {animal['numero']}")
                                busca_compra = input("Digite o ID do animal que você deseja comprar:\n")
                                for animal in animais:
                                    if busca_compra == animal['numero']:
                                        print("Compra efetuada com sucesso!")
                                        _DefAdmin_.adicionar_historico(acao, animal['tipo'], usuario[1])
                                        venda.append({'produto':animal['tipo'], 'quantidade':1, 'unidade':''})
                                        del animal
                                        break
                                    else:
                                        print("Esse animal não está disponível para venda! Escolha um que esteja disponível!")
                                        continue

                            if op_compra == 2:
                                for i in range(len(estoque)):
                                    print(f"PRODUTO: {produtos_a_venda[i][0]} | KG's DISPONÍVEIS: {produtos_a_venda[i][1]} | PREÇO POR KG: R${produtos_a_venda[i][2]:.2f}")
                                op_compra2 = input("Informe qual produto você deseja comprar:\n")
                                for p in produtos_a_venda:
                                    if op_compra2 in produtos_a_venda[0]:
                                        peso_compra = float(input("Informe a quantidade em KG's que você deseja comprar:\n"))
                                        print(f'Valor total da compra: R$ {peso_compra * p[2]}')
                                        p[1] -= peso_compra
                                        venda.append({"produto":op_compra2, "quantidade":peso_compra, "unidade":"KG's"})
                                        print('Compra Efetuada com sucesso!\n')
                                        achou = False
                                        for v in range(len(vendidos)):
                                            if op_compra2 == vendidos[v][0]:
                                                vendidos[v][1] += peso_compra
                                                achou = True
                                                break
                                        if not achou:
                                            vendidos.append([op_compra2, peso_compra])

                                    else:
                                        print("Erro! Tente novamente...")

                            if op_compra == 3:
                                print(f"Litros de leite disponíveis a venda: {prod_leite}")
                                compra_leite = float(input("Informe quantos litros deseja comprar:\n"))
                                if compra_leite <= prod_leite:
                                    valor_leite = cepea.indicador('leite')
                                    preco_leite = valor_leite["valor"].iloc[-1]
                                    print(f"Compra efetuada com sucesso! Valor total da compra: R${compra_leite * preco_leite}")
                                    venda.append({'produto':'Leite', 'quantidade':compra_leite, 'unidade': 'L'})
                                else:
                                    print("A quantidade digitada não está disponível em estoque.")

                            if op_compra == 4:
                                op_av = input("Deseja avaliar os produtos comprados? S/N\n")
                                if op_av == "S":
                                    prod_av = input("Informe qual produto você deseja avaliar:\n")
                                    for prod in produtos_a_venda:
                                        if prod_av in prod:
                                            nota = int(input("Dê uma nota de 0 a 5 para o produto:\n"))
                                            if nota < 0 or nota > 5:
                                                print("A nota deve ser de 0 a 5! Tente novamente...")
                                            else:
                                                achou = False
                                                for av in range(len(avaliacao)):
                                                    if prod_av == avaliacao[av][0]:
                                                        avaliacao[av][1] += nota
                                                        avaliacao[av][2] += 1
                                                        achou = True
                                                        break
                                                if not achou:
                                                    contador = 1
                                                    avaliacao.append([prod_av, nota, contador])
                                                print("Obrigado por avaliar!")
                                            break
                                        else:
                                            print("Erro! Tente novamente...")
                                else:
                                    print("Obrigado pela preferência!")
                                    break

                        if op_cli == 2:
                            data = input("Informe a data que deseja retirar os produtos:\n")
                            dados = _DefCli_.buscar_cep()
                            transporte.append([clientes[0][0][0], data])
                            print("Transporte agendado com sucesso!")
                            arquivo_cli = open('clientes.txt', 'r')
                            pdf = FPDF()
                            pdf.add_page()
                            pdf.set_font("Helvetica", size=12)
                            pdf.cell(0, 10, "RECIBO DE COMPRA", new_x=XPos.LMARGIN,new_y=YPos.NEXT)
                            pdf.cell(0, 10, f"Cliente: {clientes[0][0]}", new_x=XPos.LMARGIN,new_y=YPos.NEXT)
                            pdf.cell(0, 10, f"Data de retirada: {data}", new_x=XPos.LMARGIN,new_y=YPos.NEXT)
                            pdf.cell(0, 10, "Itens comprados:", new_x=XPos.LMARGIN,new_y=YPos.NEXT)
                            for item in venda:
                                    pdf.cell(0, 10, f"{item['produto']}, Quantidade: {item['quantidade']} {item['unidade']}", new_x=XPos.LMARGIN,new_y=YPos.NEXT)
                            pdf.cell(0, 10, "ENDEREÇO PARA RETIRADA:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                            pdf.cell(0, 10, f"Rua:{dados['logradouro']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                            pdf.cell(0, 10, f"Bairro:{dados['bairro']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                            pdf.cell(0, 10, f"Cidade:{dados['cidade']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                            pdf.cell(0, 10, f"Estado:{dados['estado']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                            pdf.output("recibo.pdf")
                            print("Recibo gerado com sucesso!")

                        elif op_cli == 3:
                            print("Saindo...")

print('Saindo...')