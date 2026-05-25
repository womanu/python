#FUNÇÕES

class Produto: #Classe dos produtos
    def __init__(self , nome ,preço): #init é o metodo contrutot qando criamos automaticamente um produtototal
        self.nome = nome
        self.preço = preço
        
    def mostrar(self):
        print(f"{self.nome} - R${self.preço:.2f})")

produtos =[] 
        
def aplicar_desconto(total): #função para desconto

    if total >= 100:
        print("Você possui desconto!")

    else:
        print("Você não possui desconto!")
    
        
def cadastrar_produtos(): #função para cadastrar produtos
    
        nome = input("Nome do produto: ").strip().lower()
          
        try: #tratamento de erro, TENTE ISSO

            preço = float(input("Preço: ").replace(",", ".").strip().lower()) #Pedir o preço pro usuario
            
            if preço <=0: #se o preço for esse valor, invalido
                print("Valores inválidos!")

            else:
                produto = Produto(nome, preço) #se nao, o nosso produto vira o produto da classe, com nome e preço
                produtos.append(produto)  #colocando nosso produto dentro da lista

                print("Produto cadastrado!")

        except: #exceção, erro, vai pedir dnv
            print("Erro! Digite valores válidos.")
        
def listar_produtos(): #função para percorrer a lista de produtos
    if len(produtos) <= 0: #se a quantidade dentro da lista for 0,
        print("Nenhum produto cadastrado.") #vai dar isso
    else: #se nao for
        for i in range(len(produtos)): #percorre o indice em um raio de quantidade da lista produtos
            produto = produtos[i] #produto = lista de produtos na posição que ela esta
            # Somamos 1 ao índice apenas na exibição
            print(f"Produto: {i + 1} - {produto.nome} | Preço: {produto.preço:.2f} | ") #.2f significa que ele vai colocar apenas duas casas decimais após a virgula no nosso numero

def comprar_produto():
    if len (produtos) ==0: #se a quantidade for igual a zero, mostra q n tem nd
        print("Nenhum produto cadastrado!")
    else:
        try:
           i = int(input("Digite o numero do produto: ")) #indice é o numero do produto, ou seja, ele esta pedindo a posição do produto que o usuario quer
           produto = produtos[i-1] #produto é igual ao indice dele
           quantidade = int(input("Quantidade: ")) #pede a quantidade
           total_pagar = produto.preço * quantidade #calcula 
           print(f"Total da compra: R$ {total_pagar:.2f}") #exibe o valor
           aplicar_desconto(total_pagar) #mostra se tem desconto
        except:
            print("Digite apenas números!") #nesse bloco inteireo o usuario so responde com numero, se nao responder, da erro
           

    
#LAÇO INFINITO MENU:


while True:
    print("\nMENU DO USUÁRIO:")
    print("1 - Cadastro de Produto(s)")
    print("2 - Listar produtos")
    print("3 - Comprar produto(s)")
    print("4 - Sair")
    
    
    try:
        
       opção = int(input("Escolha uma opção: "))
       
       if opção == 1:
            cadastrar_produtos()
            
       elif opção == 2:
            listar_produtos()
            
       elif opção == 3:
            comprar_produto()
            
       elif opção == 4:
            print("Programa encerrado!")
            break
       else:
            print("opção inválida")
    except ValueError:
        print("Digite apenas números!")
    
        
        
 

        
    