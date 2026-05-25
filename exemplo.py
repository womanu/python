# =========================
# CLASSE
# =========================

class Produto:

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


# =========================
# FUNÇÕES
# =========================

def calcular_subtotal(preco, quantidade):
    return preco * quantidade


def aplicar_desconto(total):

    if total >= 100:
        return print("Você possui desconto!")

    else:
        return print("Você não possui desconto!")


def calcular_media(total, quantidade):

    if quantidade == 0:
        return 0

    return total / quantidade


def maior_compra(vendas):

    maior = vendas[0]

    for venda in vendas:

        if venda["total"] > maior["total"]:

            maior = venda

    return maior


def buscar_produto(produtos, nome_produto):

    for produto in produtos:

        if produto.nome.lower() == nome_produto.lower():

            return produto

    return None

def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for i in range(len(produtos)):
            produto = produtos[i]
            # Somamos 1 ao índice apenas na exibição
            print(f"Produto: {i + 1} - {produto.nome} | "
                  f"Preço: {produto.preco:.2f} | ")


# =========================
# LISTAS
# =========================

produtos = []
vendas = []


# =========================
# MENU
# =========================

while True:

    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Relatório final")
    print("5 - Sair")

    try:

        opcao = int(input("Escolha: "))

    except:

        print("Digite apenas números!")
        continue


    # =========================
    # CADASTRAR
    # =========================

    if opcao == 1:

        nome = input("Nome do produto: ")

        try:

            preco = float(input("Preço: ").replace(",", "."))
            estoque = int(input("Estoque: "))

            if preco < 0 or estoque < 0:

                print("Valores inválidos!")

            else:

                produto = Produto(nome, preco, estoque)

                produtos.append(produto)

                print("Produto cadastrado!")

        except ValueError:

            print("Erro! Digite valores válidos.")


    # =========================
    # LISTAR
    # =========================

    elif opcao == 2:

        listar_produtos(produtos)


    # =========================
    # COMPRAR
    # =========================

    elif opcao == 3:

        if len(produtos) == 0:

            print("Nenhum produto cadastrado!")

        else:

            nome_cliente = input("Nome do cliente: ")

            listar_produtos(produtos)

            nome_produto = input("Produto desejado: ")

            produto = buscar_produto(produtos, nome_produto)

            if produto is None:

                print("Produto não encontrado!")

            else:

                try:

                    quantidade = int(input("Quantidade: "))

                    if quantidade <= 0:

                        print("Quantidade inválida!")

                    elif quantidade > produto.estoque:

                        print("Estoque insuficiente!")

                    else:

                        subtotal = calcular_subtotal(
                            produto.preco,
                            quantidade
                        )

                        produto.estoque -= quantidade

                        total = aplicar_desconto(subtotal)

                        print(f"Total: R$ {total:.2f}")

                        if total >= 100:

                            print("Desconto disponível")

                        else:

                            print("Sem desconto")

                        venda = {
                            "cliente": nome_cliente,
                            "total": total
                        }

                        vendas.append(venda)

                except ValueError:

                    print("Digite apenas números!")


    # =========================
    # RELATÓRIO
    # =========================

    elif opcao == 4:

        total_vendas = len(vendas)

        rendimento_total = 0

        for venda in vendas:

            rendimento_total += venda["total"]

        media = calcular_media(rendimento_total, total_vendas)

        print("\nRELATÓRIO FINAL")

        print(f"Total de vendas: {total_vendas}")
        print(f"Rendimento total: R$ {rendimento_total:.2f}")
        print(f"Média das vendas: R$ {media:.2f}")

        if total_vendas > 0:

            maior = maior_compra(vendas)

            print(f"Maior compra: "
                  f"{maior['cliente']} - "
                  f"R$ {maior['total']:.2f}")


    # =========================
    # SAIR
    # =========================

    elif opcao == 5:

        print("Programa encerrado!")
        break


    # =========================
    # ERRO
    # =========================

    else:

        print("Opção inválida!")