class LojaVirtual:
    def __init__(self, desconto ):
        self.desconto = desconto
    #o cliente pode ver os produtos - e tem que fazer com que o admin cadastre mais produtos nessa lista
    def produtos_loja (self):
        pass
    #aqui vai cadastrar os produtos novos - somente admin pode ver
    def cadastrar_produtos (self):
        pass
    #carrinho de compra do cliente - ele vai adicionado os produtos
    def carrinho_compras (self):
        pass
    #é o check-out - vai ter que dar o valor do carrinho de comprar e ele vai ter que dar a opcão de pagamento (tentar juntar isso com a atividade do banco)
    def valor_final (self):
        pass

lojavirtual = LojaVirtual (0.10)

#inicio do codigo com o cliente
while True:
    try:
        admin_ou_cliente = input("Seja bem-vindo ao LolaCosmetics!\n você é um cliente ou admin?")
        if admin_ou_cliente == "cliente":
            print("Olá querido(a) cliente! Vamos as compras! :D")
            print("Abaixo teremos a lista dos nosso produtos disponíveis em loja: ")
            print()



#autenticando o admin
        elif admin_ou_cliente == "admin":
            ("Olá admin, vamos autenticar sua entrada: ")
            senha = 1234
            tentativa_senha = int(input("Digite a senha para o sistema autenticar a sua entrada: "))
            if tentativa_senha == senha:
                print("Entrada autenticada, seja bem-vindo, o sistema fica feliz em te ver novamente!")
            else:
                print("Entrada bloqueada")
        else:
            print("Não entendi, tente novamente!")
    except ValueError:
        print("Não entendi usuário, entre com algo válido.")





#     def prateleira(self):
#         lista_cadastrado = ["Morte Súbita", "Danos Vorazes"]
#         preco_cadastrado = [35.40, 40.00]
#         LojaVirtual.cadastrar_produtos()
#         for i, (lista_cadastrado, preco_cadastrado) in enumerate (zip(lista_cadastrado, preco_cadastrado)):
#             return(f"{lista_cadastrado} por apenas R${preco_cadastrado} reais.")
        
#     def cadastrar_produtos (self):
#         LojaVirtual.prateleira()
#         adicionar_produto = ("Coloque o nome do produto que deseja cadastrar: ")
#         lista_cadastrado.append(adicionar_produto)
#         print(f"O produto {adicionar_produto} foi adicionado à lista de produtos.")
    
#     def carrinho (self):
        
#     def valor_total (self):
#         pass

# lojavirtual = LojaVirtual(0.10)

# pergunta = input("Você é admin ou cliente?")
# if pergunta == "admin":
#     senha = "1234"
#     acessar = input("Digite a senha: ")
#     if acessar == senha:
#         print("Bem-vindo admin a loja LolaCosmetics! Cadastre os produtos no estoque da loja")
#         lojavirtual.cadastrar_produtos()
#     else:
#         print("Senha incorreta")
# else:
#     print("Seja bem-vindo querido cliente a loja LolaCosmetics!")
#     print("Veja o nosso armazém de produtos: ")
#     print(f"A LolaCosmetics tem os seguintes produtos {lojavirtual.prateleira()}")