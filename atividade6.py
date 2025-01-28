class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def produtinhox (self):
        total = self.preco * self.quantidade_estoque
        return (f"O valor total em estoque é de: R${total} reais")

produto = Produto ("mucilon", 15, 200) 
print(produto.produtinhox())