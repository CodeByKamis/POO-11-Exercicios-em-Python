class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
    
    def emprestar(self):
        emprestimo = input("Deseja qual livro? ")
        if emprestimo == self.titulo:
            print("Que bacana, temos esse em nosso acervo! ")
            print(f"O livro {self.titulo} possui {self.numero_paginas} páginas e foi escrito por: {self.autor}")
            dias = int(input("Quantos dias você deseja ficar com o livro? No máximo 10 dias.\n"))
            if dias >10:
                print("Não é possível mais de 10 dias.")
            else:
                print(f"Ok, você tem {dias} dias de empréstimo")
        else:
            print("Que pena, não temos esse livro!")
        
livro = Livro("Crepúsculo", "Stephenie Meyer", "480" )
livro.emprestar()