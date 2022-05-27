import imp
from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main():
    menu()

def menu():
    print("Bem vindo à Lojinha!!")
    print("Selecione uma opção:\n")

    print("'1: Cadastrar produto'")
    print("'2: Listar produto'")
    print("'3: Comprar produto'")
    print("'4: Visualizar carrinho'")
    print("'5: Fechar pedido'")
    print("'6: Sair do sistema'")

    opcao = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produtos()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Até mais!!")
        sleep(2)
        exit(0)
    else:
        print("Opção Inválida!")
        sleep(1)
        menu()

def cadastrar_produto():
    print("Cadastro de Produto\n")

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    produto = Produto(nome, preco)

    produtos.append(produto)

    print(f"O produto {produto.nome} foi cadastrado com sucesso!")
    sleep(2)
    menu()

def listar_produtos():
    if len(produtos) > 0:
        print("Lista de Produtos: \n")
        for produto in produtos:
            print(produto)
            print("\n")
            sleep(1)
    else:
        print("Ainda não existem produtos cadastrados!")
    sleep(2)
    menu()

def comprar_produtos():
    if len(produtos) > 0:
        print("Informe o código do produto que vai ser comprado: \n")
        print("Produtos disponíveis: \n")

        for produto in produtos:
            print(produto)
            print('\n')
            sleep(1)
        
        codigo = int(input())

        produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
               tem_no_carrinho = False

               for item in carrinho:
                    quant = item.get(carrinho)
                    if quant:
                       item[produto] = quant + 1
                       print(f"Agora o produto {produto.nome} tem {quant + 1} unidades no seu carrinho")
                       tem_no_carrinho = True
                       sleep(2)
                       menu()
               if not tem_no_carrinho:
                   prod = {produto: 1}
                   carrinho.append(prod)
                   print(f"O produto {produto.nome} foi adicionado ao carrinho!")
                   sleep(2)
                   menu()             
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f"O produto {produto.nome} foi adicionado ao carrinho")
                sleep(2)
                menu()           
        else:
            print("O produto com código {codigo} não foi encontrado.")
            sleep(2)
            menu()

    else:
        print("Ainda não existem produtos para vender!")
    sleep(2)
    menu()

def visualizar_carrinho():
    if len(carrinho) > 0:
        print("Produtos no carrinho: \n")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                sleep(1)
    else:
        print("Ainda não existem produtos no carrinho!")
    sleep(2)
    menu()

def fechar_pedido():
    if len(produtos) > 0:
        valor_total: float = 0

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                valor_total = dados[0].preco * dados[1]
                print('\n')
                sleep(1)
        
        print(f"O valor total da sua compra é {formata_float_str_moeda(valor_total)}")
        print("Volte sempre!")
        carrinho.clear()
        sleep(2)
    else:
        print("Ainda não existem produtos no carrinho!")

    sleep(2)
    menu()

def pega_produto_por_codigo(codigo):
    p : Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    
    return p

if __name__ == '__main__':
    main()