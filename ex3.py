continuar = "s"
continuar_compra = "s"
continuar_venda = "s"

#FUNÇÕES

#aqui a função def esta calculando o valor dentro dos parâmetros, vai retornar multiplicando
def calcular_subtotal(preço, quantidade):
    return preço * quantidade

#abaixo estao as equações de desconto

def aplicar_desconto(total):
    if total >= 1000:
        return total * 0.85
    elif total >=500:
        return total * 0.90
    elif total >= 200:
        return total *0.95
    else:
        return total

#aqui esta calculando a media das vendas, o total é a soma de todas as vendas e quantidade é o número de vendas
def calcular_media(total, quantidade): #Recebe o total das vendas
    if quantidade == 0: #verifica se a quantidade de vendas é igual a zero, isso aq evita erro de matematica, dividir por zero da erro
        return 0 #se for, ele volta zerado
    else: #se nao for 0, retorna dividindo e fazendo a média v
        return total / quantidade

#essa função aqui encontra qual cliente gastou mais:
def maior_compra(vendas): #a função recebe vendas, que é a lista de todas as vendas feitas
    maior = vendas[0] #começa assumindo que a primeira venda é a maior (é o maior atual) porque o programa precisa começar comparando com algum valor.
    
    for venda in vendas: #percorre todas as vendas
    
        if venda["total"] > maior["total"]: #"o total dessa venda é maior que o maior atual?" ele compara   
    
            maior = venda
            
    return maior  #vai mostrar a maior venda

#essa função serve pra procurar o produto pelo nome dentro da lista
def buscar_produto(produtos, nome_produto):

    for produto in produtos:
    
        if produto["nome"].lower() == nome_produto.lower(): #o nome digitado é igual ao nome do produto da lista
        
            return produto #Se encontrar o produto, a função devolve ele inteiro.

#CADASTRO DE PRODUTOS:

produtos = []

while continuar == "s": # o que eu colocar dentro do continuar (s) vai ser verdadeiro, entao vai sempre voltar pra ca

    print("\nCadastro de Produto")

    nome = input("Nome do produto: ")

    while True: #laço while true criado para verificar a condição de preço, tem que ser maior que 0, nao pode aceitar negativo

        preço = float(input("Preço: ").replace(",", ".")) #pega um caracter e substitui pelo outro caracter

        if preço >= 0:
            break
            
        else:
            print("Digite um preço válido: ")

    while True:

        estoque = int(input("Estoque: "))

        if estoque >= 0:
            break  
            
        else:
            print("Digite um valor válido para produto em estoque: ")

    produto = {
        "nome": nome,
        "preço": preço,
        "estoque": estoque
    }

    produtos.append(produto)

    while True: #serve para verificar a condição

        continuar = input("Cadastrar outro produto? (s/n): ").strip().lower()

        #se dentro de continuar tiver s ou n, ele vai para o outro while
        if continuar == "n" or continuar == "s": # se eu colocar s, ele quebra apenas a repetição, mas sempre volta pro while
        
            break # o break serve apenas para sair do while true, nao do while inteiro
            
        else:
            print("Digite uma respota válida")

#Sistema de vendas:

vendas = []

while continuar_venda == "s":

    print("\nNova venda")

    nome_cliente = input("Nome do cliente: ")

    total = 0 #esvaziar o carrinho do cliente

    continuar_compra = "s"

    while continuar_compra == "s":

        print("\nProdutos disponíveis:")

        #aqui ele percorre a lista e mostra todos os produtos toda vez que for comprar
        for produto in produtos:
        
            print(f"PRODUTO: {produto['nome']} | PREÇO: {produto['preço']} | ESTOQUE: {produto['estoque']}")

        nome_produto = input("Qual produto deseja comprar?: ").strip().lower()

        #aqui ele tenta encontrar o produto digitado
        produto_encontrado = buscar_produto(produtos, nome_produto)

        if produto_encontrado is None:

            print("Produto não encontrado")

        else:

            while True: #laço criado apenas para verificar a quantidade, que tem que ser maior que 0

                quantidade = int(input("Quantidade: "))

                if quantidade > 0:
                    break

                else:
                    print("Digite uma quantidade válida")

            if quantidade > produto_encontrado["estoque"]:

                print("Estoque insuficiente")

            else:

                subtotal = calcular_subtotal(produto_encontrado["preço"], quantidade)

                produto_encontrado["estoque"] -= quantidade

                total += subtotal

                print(f"subtotal: {subtotal}")

        while True: #serve para verificar a condição de continuação de compra, se eu for colocar um "talvez" ele pede pra eu escolher direito

            continuar_compra = input("Adicionar mais produtos? (s/n): ").strip().lower()

            #se dentro de continuar tiver s ou n, ele vai para o outro while
            if continuar_compra == "n" or continuar_compra == "s":
            
                break

            else:
                print("Digite uma escolha válida: ")

    # salvando a venda

    total = aplicar_desconto(total) #chama a função que criamos la em cima e aplica no total o desconto

    venda = {
        "cliente": nome_cliente,
        "total": total
    }

    vendas.append(venda) #adiciona uma venda na nossa lista de vendas


    while True: #serve para verificar a condição de continuar venda, tratar erro

        continuar_venda = input("Realizar outra venda? (s/n): ").strip().lower()

        #se dentro de continuar tiver s ou n, ele vai para o outro while
        if continuar_venda == "n" or continuar_venda == "s":
        
            break

        else:
            print("Digite uma escolha válida, (s/n): ").strip().lower()

#Relatório Final:

total_vendas = len(vendas) #conta quantos itens tem na lista, ou seja o total_vendas é a quantidade de vendas

rendimento_total = 0 #dinheiro total da loja

for venda in vendas:

    rendimento_total = rendimento_total + venda["total"]

media = calcular_media(rendimento_total, total_vendas) #chama a função de la de cima, passa pelo faturamento, total de vendas, e faz a divisão 

if total_vendas > 0:

    maior = maior_compra(vendas)

else:

    maior = None #se nao tiver venda nenhuma, nao existe maior venda, ou seja, vira um vazio

#Exibindo informações:

print("\nResumo de vendas: ")

for venda in vendas:

    print(f"Cliente: {venda['cliente']} | Total: {venda['total']}")

print("\n Final: ")

print(f"Total de vendas: {total_vendas}")

print(f"Rendimento total: {rendimento_total}")

print(f"Média das vendas: {media}")

if maior:

    print(f"Maior compra: {maior['cliente']} : {maior['total']}")