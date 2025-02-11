class MaquinadeVendas:
    def __init__(self):
        pass
        self.lista_produto = []
        self.lista_estoque = []
        self.quantidade_carrinho = 0

    def cadastro (self):
         while True:
            print("Vamos adicionar novos produtos!")
            addproduto = input("Adicione o nome do produto: ")
            addeestoque = int(input("Adicione quanto tem em estoque: "))
            self.lista_produto.append(addproduto)
            self.lista_estoque.append(addeestoque)
            print(f"Essa é a sua lista de produtos: \n{list(zip(self.lista_produto, self.lista_estoque))}")
            pergunta = input("Deseja adicionar mais algum produto? Y/N")
            if pergunta == "N":
                break
            elif pergunta == "Y":
                continue

    def selecionarProduto (self):
        lista_completa = list(zip(self.lista_produto, self.lista_estoque))
        while True:
            print(f"Essa é a sua lista de produtos: \n{lista_completa}")
            indexproduto = int(input("Qual é o index do produto que você gostaria de comprar? "))
            if 0 <= indexproduto < len(self.lista_produto):
                add_carrinho = []
                self.quantidade_carrinho +=1
                self.lista_estoque[indexproduto] -=1
                add_carrinho.append(lista_completa[indexproduto])
                print(f"Produto selecionado com sucesso, olhe o seu carrinho: {add_carrinho}.\nTemos {self.lista_estoque} quantidades em estoque agora")
                print(f"Quantidade de produtos no carrinho {self.quantidade_carrinho} produtos.")
            else:
                print("Acho que você errou o índice :c")
            pergunta = input ("Deseja adicionar outro produto? Y/N")
            if pergunta == "N":
                break

    def pagamento (self):
        while True:
            perguntinha = input("Você terminou de fazer a sua compra? Y/N")
            if perguntinha == "N":
                print("Então continue comprando")
                break
            elif perguntinha == "Y":
                try:
                    print(f"\nSua lista de compras: \n{list(zip(self.lista_produto, [self.quantidade_carrinho]))}")
                    valorda_compra = self.quantidade_carrinho * 10
                    modo_pagamento = input(f"Ficou R${valorda_compra} reais. Como será o seu modo de pagamento (débito ou crédito)?")
                    senha = input("Digite a senha: ")
                    print(f"Senha {senha} correta!\nPagamento por {modo_pagamento} realizado com sucesso! Volte sempre!")
                    break
                except ValueError:
                    print("Algo deu errado, entte com as respostas corretas ")

    def estoque (self):
        print(f"Veja o estoque disponível:\n {list(zip(self.lista_produto, self.lista_estoque))} ")

maquinadevendas = MaquinadeVendas()
while True:
    print("Bem-vindo a lojinha da Kamila, como podemos te ajudar?")
    pergunta = input("(01)Cadastrar produto\n(02)Selecionar Produto para o carrinho\n(03)Pagamento\n(04)Estoque\n(05)Sair\n")
    if pergunta == "01":
        maquinadevendas.cadastro()

    elif pergunta == "02":
        maquinadevendas.selecionarProduto()

    elif pergunta == "03":
        maquinadevendas.pagamento()

    elif pergunta == "04":
        maquinadevendas.estoque()

    elif pergunta == "05":
        print("Ok, até logo.")
        break