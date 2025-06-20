class Produto:
    def __init__(self, nome, preco, quantidade, categoria, fornecedor):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria
        self.fornecedor = fornecedor

class Estoque:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade inicial: "))
        categoria = input("Categoria do produto: ")
        fornecedor = input("Fornecedor: ")
        novo = Produto(nome, preco, quantidade, categoria, fornecedor)
        self.produtos.append(novo)
        print(f"{nome} cadastrado com sucesso!")

    def repor_estoque(self):
        if not self.produtos:
            print("Nenhum produto no estoque ainda.")
            return
        self.listar_produtos()
        escolha = int(input("Digite o número do produto pra repor: "))
        if 0 <= escolha < len(self.produtos):
            qtd = int(input("Quantas unidades vai adicionar? "))
            self.produtos[escolha].quantidade += qtd
            print(f"Estoque de {self.produtos[escolha].nome} agora é {self.produtos[escolha].quantidade}")
        else:
            print("Produto inválido!")

    def vender_produto(self):
        if not self.produtos:
            print("Nenhum produto no estoque ainda.")
            return
        self.listar_produtos()
        escolha = int(input("Digite o número do produto pra vender: "))
        if 0 <= escolha < len(self.produtos):
            qtd = int(input("Quantas unidades o cliente vai comprar? "))
            if qtd <= self.produtos[escolha].quantidade:
                self.produtos[escolha].quantidade -= qtd
                total = qtd * self.produtos[escolha].preco
                print(f"Venda feita! Total: R${total:.2f}. Estoque agora: {self.produtos[escolha].quantidade}")
            else:
                print("Não tem tudo isso no estoque!")
        else:
            print("Produto inválido!")

    def listar_produtos(self):
        print("\nProdutos no estoque:")
        for i, prod in enumerate(self.produtos):
            print(f"{i} - {prod.nome} | R${prod.preco} | Quantidade: {prod.quantidade} | Categoria: {prod.categoria} | Fornecedor: {prod.fornecedor}")

    def relatorio(self):
        print("\n--- Relatório de Estoque ---")
        for prod in self.produtos:
            valor_total = prod.quantidade * prod.preco
            print(f"{prod.nome} | Qtd: {prod.quantidade} | Valor em estoque: R${valor_total:.2f}")

estoque = Estoque()

while True:
    print("\nBem-vindo ao Estoque da Kamis")
    print("1 - Cadastrar produto novo")
    print("2 - Repor estoque")
    print("3 - Vender produto")
    print("4 - Ver todos os produtos")
    print("5 - Ver relatório financeiro")
    print("6 - Sair")

    op = input("Escolha: ")

    if op == "1":
        estoque.cadastrar_produto()
    elif op == "2":
        estoque.repor_estoque()
    elif op == "3":
        estoque.vender_produto()
    elif op == "4":
        estoque.listar_produtos()
    elif op == "5":
        estoque.relatorio()
    elif op == "6":
        print("Tchauu amigos")
        break
    else:
        print("Opção inválida!")
