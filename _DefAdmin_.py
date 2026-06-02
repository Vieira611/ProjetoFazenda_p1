def cadastrar_produto(estoque:list, produto:list, produtosvenda:list):
    achou = False
    for i in range(len(estoque)):
        if produto[1] == estoque[i][0]:
            estoque[i][1] += produto[1]
            break
        else:
            achou = False
    if not achou:
        estoque.append(produto)

    escolher_venda = input("Quer colocar o produto à venda?: S/N").upper()
    if escolher_venda == "S":
        produtosvenda.append(produto)
        print("Item adicionado à venda!")

def cadastrar_animais(animais:list):
    animal = {
        "numero": int(input("Número do animal: ")),
        "tipo": input("Tipo do animal: "),
        "status": input("Status do animal: "),
        "peso": float(input("Peso do animal: ")),
        "venda": False
    }
    animais.append(animal)

def relatorio_geral(animais:list, estoque:list):

