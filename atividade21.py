class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.carrinho = []
        self.desconto = 0
        self.frete = 5

    def add_produto(self, produto):
        self.carrinho.append(produto)
        print(f"\n{produto.nome} adicionado no carrinho")

    def calcular_total(self):
        total = sum(p.preco for p in self.carrinho)
        total -= self.desconto
        total += self.frete
        return total

    def finalizar(self):
        total = self.calcular_total()
        self.cliente.historico.append(self.carrinho[:])
        print(f"Compra finalizada! Total: R${total:.2f}")
        self.carrinho.clear()

class Loja:
    def __init__(self):
        self.produtos = []
        self.clientes = []

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$"))
        self.produtos.append(Produto(nome, preco))
        print(f"{nome} cadastrado!")

    def cadastrar_cliente(self):
        nome = input("Nome do cliente: ")
        self.clientes.append(Cliente(nome))
        print(f"Cliente {nome} cadastrado!")

    def recomendar(self, cliente):
        produtos_comprados = set(p.nome for compra in cliente.historico for p in compra)
        recomendados = [p.nome for p in self.produtos if p.nome not in produtos_comprados]
        if recomendados:
            print(f"Produtos que você pode gostar: {', '.join(recomendados)}")
        else:
            print("Você já comprou tudo :D")

loja = Loja()

while True:
    print("\n1-Cadastrar produto\n2-Cadastrar cliente\n3-Fazer pedido\n4-Sair")
    op = input("Escolha: ")
    if op == "1":
        loja.cadastrar_produto()
    elif op == "2":
        loja.cadastrar_cliente()
    elif op == "3":
        if not loja.clientes or not loja.produtos:
            print("Cadastre pelo menos 1 cliente e 1 produto antes.")
            continue
        nome_cli = input("Nome do cliente: ")
        cliente = next((c for c in loja.clientes if c.nome == nome_cli), None)
        if not cliente:
            print("Cliente não encontrado.")
            continue
        pedido = Pedido(cliente)
        while True:
            print("Produtos disponíveis:")
            for i, p in enumerate(loja.produtos):
                print(f"{i} - {p.nome} - R${p.preco:.2f}")
            escolha = input("Escolha o número do produto pra adicionar, depois de adicionado digite 'fim' ou já escreva 'fim' se estiver so dando uma olhadinha: ")
            if escolha == "fim":
                break
            if escolha.isdigit() and 0 <= int(escolha) < len(loja.produtos):
                pedido.add_produto(loja.produtos[int(escolha)])
            else:
                print("Escolha inválida.")
        desconto = input("Tem cupom de desconto? (sim/nao) ").lower()
        if desconto == "sim":
            pedido.desconto = float(input("Quanto de desconto? R$"))
        frete = input("Quer calcular frete? (sim/nao) ").lower()
        if frete == "sim":
            pedido.frete = float(input("Quanto que você vai pagar de frete? R$"))
        pedido.finalizar()
        loja.recomendar(cliente)
    elif op == "4":
        break
    else:
        print("Opção inválida")
