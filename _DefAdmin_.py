from agrobr import *
from datetime import date
import string


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


def relatorio_geral(animais:list, estoque:list, prod_leite:list):
    print(f'Litros de leite produzidos: {prod_leite}')
    print(f'Produtos diponíveis: {len(estoque)}')

def venda_animal(animais:list, animais_a_venda:list):
    for a in range(len(animais)):
        print(f"TIPO: {animais[a]['tipo']} | STATUS: {animais[a]['status']} | ID: {animais[a]['numero']} | PESO: {animais[a]['peso']}")
    num_anim = int(input('Digite o número do animal que você deseja colocar a venda: '))
    for animal in animais:
        if animal['numero'] == num_anim:
            animal['venda'] == True
            animais_a_venda.append(animal)
            print(f'O animal {num_anim} foi vendido por R$ {animal['peso']*cepea.indicador('boi')}')

#(Ex: {'data': '10/06', 'acao': 'venda', 'item': 'Queijo Coalho', 'qtd': 5})
def adicionar_historico(acao, item, qtdKgs, cliente=None):
    log = open('log.txt', 'a')
    if qtdKgs in string.ascii_letters:
        log.write(f'\ndata:{date.today()} | ação:{acao} | animal: {item} | cliente: {qtdKgs}')
        log.close()
    else:
        log.write(f'\ndata:{date.today()} | ação:{acao} | item: {item} | qtd: {qtdKgs}')
        log.close()




