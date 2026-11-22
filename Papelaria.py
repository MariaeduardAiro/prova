import csv
import math

#serve para formatar o produto e o preço de forma organizada
def formatar_produto(nome, preco):
    return f"{nome}.......... R$ {preco:.2f}"
#serve para buscar o produto na lista de produtos cadastrados
def buscar_produto(produtos, nome):
    nome_busca = nome.strip().casefold()
    for produto in produtos:
        if produto[0].casefold() == nome_busca:
            return produto
    return None
#serve para validar o preço do produto, garantindo que seja um número válido e maior que zero
def validar_preco(texto):
    try:
        preco = float(texto)
    except ValueError:
        return None

    if not math.isfinite(preco) or preco < 0:
        return None
    return preco
#Serve para mostrar o menu de opções para o usuário
def mostraromenu():
    print("----------Menu--------------")
    print("Opções:")
    print("cadastrar produto(digite 1)")
    print("Consultar produto(digite 2)")
    print("Listar produtos cadastrados(digite 3)")
    print("Remover produto(digite 4)")
    print("Consultar desempenho de vendas(digite 5)")
    print("Ranking de produtos(digite 6)")
    print("Alterar produto(digite 7)")
    print("Registrar venda(digite 8)")
    print("Cancelar venda(digite 9)")
    print("sair(digite 10)")
#Serve para cadastrar um novo produto, garantindo que o nome não esteja vazio e que o preço seja válido
def cadastrar_produto(produtos):
    nome = input("nome do produto: ").strip()
    if not nome:
        print("O nome do produto não pode ficar vazio.")
        return

    if buscar_produto(produtos, nome) is not None:
        print("Já existe um produto cadastrado com esse nome.")
        return

    preco = None
    while preco is None or preco <= 0:
        preco = validar_preco(input("Preço do produto (maior que zero): "))
        if preco is None or preco <= 0:
            print("Preço inválido. Digite um valor maior que zero.")
    produtos.insert(0, (nome, preco))
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!")
    print(f"Total de produtos: {len(produtos)}")
#Produto se inicia vazio
produtos = []
#Salva os produtos em um arquivoCsv
def salvar_produtos(produtos):
    with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(produtos)
#Carrega os produtos do arquivoCsv, caso o arquivo não exista, retornanone
def carregar_produtos():
    try:
        with open("produtos.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            return [(linha[0], float(linha[1])) for linha in leitor if linha]
    except FileNotFoundError:
        return None
#Serve para consultar um produto pelo nome, exibindo suas informações caso seja encontrado
def consultar_produto(produtos):
    nome_busca = input("Digite o nome do produto: ")
    produto = buscar_produto(produtos, nome_busca)
    if produto is None:
        print("Produto não encontrado.")
        return
    print(f"Produto encontrado: {formatar_produto(produto[0], produto[1])}")
#Serve para remover um produto da lista de produtos cadastrados
def remover_produto(produtos):
    nome_busca = input("Digite o nome do produto que deseja remover: ").strip()
    produto = buscar_produto(produtos, nome_busca)
    if produto is None:
        print("Produto não encontrado.")
        return
    produtos.remove(produto)
    salvar_produtos(produtos)
    print(f"Produto '{produto[0]}' removido.")
#Serve para alterar informações de um produto existente
def alterar_produto(produtos):
    nome_atual = input("Digite o nome do produto que deseja alterar: ").strip()
    produto_atual = buscar_produto(produtos, nome_atual)
    if produto_atual is None:
        print("Produto não encontrado.")
        return

    nome_novo = input("Novo nome (Enter para manter o atual): ").strip()
    if not nome_novo:
        nome_novo = produto_atual[0]

    produto_com_nome = buscar_produto(produtos, nome_novo)
    if produto_com_nome is not None and produto_com_nome != produto_atual:
        print("Já existe outro produto com esse nome.")
        return

    preco_novo = validar_preco(input("Novo preço: "))
    if preco_novo is None:
        print("Preço inválido. Digite um valor igual ou maior que zero.")
        return

    indice = produtos.index(produto_atual)
    produtos[indice] = (nome_novo, preco_novo)
    salvar_produtos(produtos)
    print("Produto alterado com sucesso!")
#Serve para listar todos os produtos cadastrados, exibindo-os em ordem de cadastro
def listar_produtos(produtos):
     print("--------------Produtos Cadastrados----------------")
     if not produtos:
         print("Nenhum produto cadastrado.")
         return

     produtos.sort(key=lambda produto: produto[0].casefold())
     i = 1
     for produto in produtos:
         print(f"{i}. {formatar_produto(produto[0], produto[1])}")
         i += 1
     print(f"Total de produtos: {len(produtos)}")

#dados
vendas = [

["Caderno", 10, "2026-01-15"],

["Caderno", 12, "2026-02-10"],

["Caderno", 8, "2026-03-05"],

["Caderno", 14, "2026-04-05"],

["Caderno", 16, "2026-05-01"],

["Caderno", 18, "2026-06-15"],

["Caderno", 20, "2026-07-10"],

["Caneta", 40, "2026-02-20"],

["Caneta", 30, "2026-03-10"],

["Caneta", 20, "2026-04-05"],

["Caneta", 10, "2026-05-01"],

["Caneta", 5, "2026-06-15"],

["Caneta", 15, "2026-07-10"],


["Mochila", 35, "2026-02-05"],

["Mochila", 42, "2026-03-12"],

["Mochila", 38, "2026-04-18"],

["Mochila", 45, "2026-05-20"],


["Borracha", 3, "2026-02-08"],

["Borracha", 5, "2026-03-15"],

["Borracha", 4, "2026-04-10"],

["Borracha", 6, "2026-05-14"],

]
#Salva vendas em um arquivoCsv
def salvar_vendas(vendas):
    with open("vendas.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(vendas)
#Carrega vendas do arquivoCsv, caso o arquivo não exista, retornanone
def carregar_vendas():
    try:
        with open("vendas.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            return [[linha[0], int(linha[1]), linha[2]] for linha in leitor if linha]
    except FileNotFoundError:
        return None
#Serve para registrar uma venda, verificando se o produto existe e se a quantidade é válida
def registrar_venda(produtos, vendas):
    nome_informado = input("Digite o nome do produto: ").strip()
    produto = buscar_produto(produtos, nome_informado)
    if produto is None:
        print("Produto não encontrado no catálogo.")
        return

    try:
        quantidade = int(input("Digite a quantidade vendida: "))
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro positivo.")
        return

    if quantidade <= 0:
        print("Quantidade inválida. Digite um número inteiro positivo.")
        return

    data = input("Digite a data da venda: ").strip()
    vendas.append([produto[0], quantidade, data])
    salvar_vendas(vendas)
    print("Venda registrada com sucesso!")
#Serve para cancelar uma venda, exibindo vendas registradas e permitindo ao usuário escolher qual deseja cancelar
def cancelar_venda(vendas):
    if not vendas:
        print("Não há vendas para cancelar.")
        return

    print("----------Vendas registradas----------")
    i = 1
    for venda in vendas:
        print(f"{i}. {venda[0]} - {venda[1]} - {venda[2]}")
        i += 1

    try:
        numero = int(input("Digite o número da venda que deseja cancelar: "))
    except ValueError:
        print("Número inválido.")
        return

    if numero < 1 or numero > len(vendas):
        print("Número inválido.")
        return

    venda_cancelada = vendas.pop(numero - 1)
    salvar_vendas(vendas)
    print(f"Venda de '{venda_cancelada[0]}' cancelada.")
#Serve para calcular a média de vendas de um produto específico, retornandoNone se não houver histórico
def calcular_media_vendas(vendas, nome):
    quantidades = []
    for item in vendas:
        if item[0].casefold() == nome.strip().casefold():
            quantidades.append(item[1])

    if len(quantidades) == 0:
        return None

    return sum(quantidades) / len(quantidades)
#Serve para classificar o desempenho de vendas com base na média calculada
def classificar_desempenho(media):
    if media is None:
        return "Sem histórico"
    elif media >= 30:
        return "Alto"
    elif media >= 10:
        return "Médio"
    else:
        return "Baixo"
#Serve para consultar o desempenho de vendas de um produto específico, exibindo a média e a classificação
def consultar_desempenho_vendas(vendas):
    nome = input("Digite o nome do produto: ").strip()
    media = calcular_media_vendas(vendas, nome)
    desempenho = classificar_desempenho(media)

    print("Produto:", nome)
    if media is None:
        print("Média de vendas: sem histórico")
    else:
        print("Média de vendas:", media)
    print("Desempenho:", desempenho)
#Serve para gerar um ranking de produtos com base no desempenho de vendas, salvando o resultado em um arquivo de texto
def ranking_produtos(vendas):
    resultados = []
    nomes_processados = []

    for item in vendas:
        nome = item[0]
        if nome not in nomes_processados:
            media = calcular_media_vendas(vendas, nome)
            desempenho = classificar_desempenho(media)
            resultados.append([nome, media, desempenho])
            nomes_processados.append(nome)

    if not resultados:
        print("Nenhuma venda cadastrada.")
        return

    resultados.sort(key=lambda item: item[1], reverse=True)

    print("----------Ranking de desempenho----------")
    i = 1
    with open("ranking.txt", "w", encoding="utf-8") as arquivo:
        for item in resultados:
            print(f"{i}. {item[0]} - {item[1]:.1f} - {item[2]}")
            arquivo.write(f"{i};{item[0]};{item[1]:.1f};{item[2]}\n")
            i += 1
    print("Ranking salvo em ranking.txt")
#Carrega produtos do arquivoCsv, caso o arquivo não exista, retornanone
produtos_carregados = carregar_produtos()
if produtos_carregados is None:
    salvar_produtos(produtos)
else:
    produtos = produtos_carregados

vendas_carregadas = carregar_vendas()
if vendas_carregadas is None:
    salvar_vendas(vendas)
else:
    vendas = vendas_carregadas
#continuar true para manter o loop do menu ativo até que o usuário escolha sair
continuar = True
#Loop principal do programa, exibindo o menu e processando opções escolhidas pelo usuário
while continuar:
    mostraromenu()
    Opcoes = input("digite um numero:")

    if Opcoes == "1":
        cadastrar_produto(produtos)

    elif Opcoes == "2":
        consultar_produto(produtos)

    elif Opcoes == "3":
        listar_produtos(produtos)

    elif Opcoes == "4":
        remover_produto(produtos)

    elif Opcoes == "5":
        consultar_desempenho_vendas(vendas)

    elif Opcoes == "6":
        ranking_produtos(vendas)

    elif Opcoes == "7":
        alterar_produto(produtos)

    elif Opcoes == "8":
        registrar_venda(produtos, vendas)

    elif Opcoes == "9":
        cancelar_venda(vendas)

    elif Opcoes == "10":
        continuar = False

    else:
        print("invalido")