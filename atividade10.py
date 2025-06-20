class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.disponivel = True


    def verificar_disponibilidade(self):
        return self.disponivel

    def emprestar(self):
        if not self.disponivel:
            print(f"O livro '{self.titulo}' não está disponível no momento.")
            return False
        
        print(f"Que bacana, temos o livro '{self.titulo}' em nosso acervo!")
        dias = int(input("Quantos dias você quer ficar com o livro? (máximo 10 dias e digite com números): "))
        
        if dias > 10:
            print("Não é possível emprestar por mais de 10 dias.")
            return False
        
        self.disponivel = False
        print(f"Ok, você tem {dias} dias de empréstimo para o livro '{self.titulo}'.")
        return True

    def devolver(self):
        if self.disponivel:
            print(f"O livro '{self.titulo}' já tá disponível na biblioteca.")
        else:
            self.disponivel = True
            print(f"Obrigadinha por devolver o livro '{self.titulo}'. Agora ele já tá disponível para empréstimo.")

livro = Livro("Crepúsculo", "Stephenie Meyer", 480)

livro.emprestar()

livro.devolver()
