class Biblioteca:
    def __init__(self):
        self.livros = {}
    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        quantidade = int(input("Digite a quantidade disponível: "))
        if titulo in self.livros:
            self.livros[titulo] += quantidade
        else:
            self.livros[titulo] = quantidade
        print(f"Livro '{titulo}' cadastrado/atualizado com {quantidade} cópias.")

    def emprestar_livro(self):
        titulo = input("Qual livro deseja emprestar? ")
        if titulo in self.livros and self.livros[titulo] > 0:
            self.livros[titulo] -= 1
            print(f"Livro '{titulo}' emprestado com sucesso! Aproveite a leitura :)")
        else:
            print(f"Desculpe, o livro '{titulo}' não está disponível por agora.")

    def devolver_livro(self):
        titulo = input("Qual livro você vai devolver? ")
        if titulo in self.livros:
            self.livros[titulo] += 1
            print(f"Livro '{titulo}' devolvido. thanks queridinho(a)!")
        else:
            print(f"Livro '{titulo}' não pertence ao estoque da KAMIS e.e biblioteca.")

    def verificar_disponibilidade(self):
        print("Livros disponíveis na biblioteca:")
        for titulo, quantidade in self.livros.items():
            print(f" - {titulo}: {quantidade} livros dele está disponível")

biblioteca = Biblioteca()

while True:
    print("\n--- KAMIS e.e Biblioteca ---")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Verificar disponibilidade")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        biblioteca.cadastrar_livro()
    elif escolha == "2":
        biblioteca.emprestar_livro()
    elif escolha == "3":
        biblioteca.devolver_livro()
    elif escolha == "4":
        biblioteca.verificar_disponibilidade()
    elif escolha == "5":
        print("Até logo! Volte sempre :)")
        break
    else:
        print("Opção inválida, tente novamente.")
