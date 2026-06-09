from agrobr import *

async def cadastrar_produto(estoque:list, produto:list, produtosvenda:list):
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

def relatorio_geral(animais:list, estoque:list, prod_leite:list):
    print(f'Litros de leite produzidos: {prod_leite}')
    print(f'Produtos diponíveis: {len(estoque)}')

def venda_animal(animais:list):
    for animal in animais:
        print(f"TIPO: {animais[animal['tipo']]} | STATUS: {animais[animal['status']]} | ID: {animais[animal['numero']]} | PESO: {animais[animal['peso']]}")
    num_anim = int(input('Digite o número do animal que você deseja colocar a venda: '))
    print(f'O animal {num_anim} está a venda por R$ {animal['peso']*cepea.indicador('boi')}')

