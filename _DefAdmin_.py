from agrobr import *
from datetime import date
import string
import asyncio


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

async def venda_animal(animais:list, animais_a_venda:list):
    for a in range(len(animais)):
        if animais[a]['venda'] == False:
            print(f"TIPO: {animais[a]['tipo']} | STATUS: {animais[a]['status']} | ID: {animais[a]['numero']} | PESO: {animais[a]['peso']}")
    num_anim = input('Digite o número do animal que você deseja colocar a venda: ')
    for animal in animais:
        if animal['numero'] == num_anim:
            animal['venda'] = True
            if animal['tipo'] == 'boi':
                peso_animal = animal['peso'] / 30
            else:
                peso_animal = animal['peso']
            animais_a_venda.append(animal)
            valor_animal = await cepea.indicador(animal['tipo'])
            preco_animal = valor_animal["valor"].iloc[-1]
            print(f"O animal {num_anim} foi colocado a venda por R$ {peso_animal * preco_animal:.2f}")


def calcular_media_tipo(lista_animais):
    busca_tipo = input("Digite o tipo de animal que deseja buscar:")
    soma_peso = 0.0
    qtd = 0
    for animal in lista_animais:
        if animal['tipo'] == busca_tipo:
            soma_peso += animal['peso']
            qtd += 1
    media = soma_peso / qtd
    print(f"A média do peso do tipo é: {media:.2f}Kg's")
    for a in range(len(lista_animais)):
        print(f"TIPO: {lista_animais[a]['tipo']} | STATUS: {lista_animais[a]['status']} | ID: {lista_animais[a]['numero']} | PESO: {lista_animais[a]['peso']}")
    busca_animal = input("\nDigite o numero do animal que deseja calcular: ")
    for animal in lista_animais:
        if animal['numero'] == busca_animal:
            if animal['peso'] < media:
                print("O animal está abaixo da média de peso.")
            elif animal['peso'] > media:
                print("O animal está acima da media de peso.")
            else:
                print("O animal está na média de peso.")

def adicionar_historico(acao, item, variante=int):
    if variante is int:
        log = open('log.txt', 'a')
        log.write(f'\ndata:{date.today().strftime('%d/%m/%y')} | ação:{acao} | item: {item} | qtd: {variante}')
        log.close()
    else:
        log = open('log.txt', 'a')
        log.write(f'\ndata:{date.today().strftime('%d/%m/%y')} | ação:{acao} | item: {item} | cliente: {variante}')
        log.close()


