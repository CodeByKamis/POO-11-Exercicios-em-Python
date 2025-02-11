class LojaVirtual:
    # desconto
    # cadastrar produtos
    # gerar carrinho de compras
    # calcular valor total da compra
    def __init__(self, desconto):
        self.desconto = desconto
        self.lista_produtos = []

    def cadastrar_produto(self):
        while True:
            print("Muito bem, vamos cadastrar produtos")
            novo_produto = input("Digite o nome do produto que quer adicionar:")
            self.lista_produtos.append(novo_produto)
            print(f"Produto adicionado com sucesso! Veja os produtos que você possui cadastrado no sistema: \n {self.lista_produtos}")
            pergunta = input("Quer continuar cadastrando produtos? Y/N \n")
            if pergunta == "N":
                break
            elif pergunta == "Y":
                continue

    def carrinho (self):
        carrinho = []
        while True:
            print("Vamos às compras:")
            print(f"Esses são os produtos da loja: \n{self.lista_produtos}")
            produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
            carrinho.append(produto)
            pergunta = input("Terminou a compra? Y/N ")
            if pergunta == "Y":
                print(f"Seu carrinho tem esses produtos: {carrinho}")
                valor = float(input("Digite o valor total da compra: "))
                valorajustado = valor - self.desconto
                print(f"ÓTIMO! Então ficou R${valorajustado} com o desconto!")
                pagamento = input("Vai ser no débito ou no crédito?")
                print(f"Pagamento no {pagamento} bem sucessido, volte sempre!")
                break
            elif pergunta == "N":
                continue
    
    def olhadinha (self):
        print("Veja os produtos da loja: ")
        print(self.lista_produtos)

lojavirtual = LojaVirtual(0.10)

print ("Bem vindo a loja Kamis Roupas, o que gostaria de fazer?")
while True:
    escolha = input("(01) Cadastrar produtos\n(02) Comprar produtos\n(03) Dar uma olhadinha\n")
    if escolha == "01":
            print("Muito bem, vamos cadastrar os produtos")
            print(lojavirtual.cadastrar_produto())
            

    elif escolha == "02":
        perguntinha = input("Você deseja realizar compras? ").lower()
        if perguntinha == "sim":
            print(lojavirtual.carrinho())
        else:
            print("Tudo bem, esperamos logo suas comprinhas")
            

    elif escolha == "03":
        print(lojavirtual.olhadinha())
