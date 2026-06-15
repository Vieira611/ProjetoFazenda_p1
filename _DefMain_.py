def menu():
    print('---------MENU---------')
    print('1 - Cadastrar-se como cliente')
    print('2 - Fazer login')
    print('3 - Encerrar programa')


def verificar_usuario(lista:list, usr):
    existe = False
    for cliente in lista:
        if usr == cliente[1]:
            existe = True

    return  existe


def verificar_login(lista:list):
    usuario = input('Digite o seu nome de usuário:\n')
    senha = input('Digite sua senha:\n')
    busca = ([usuario, senha])
    for u in range(len(lista)):
        if busca == lista[u]:
            return [True, usuario]