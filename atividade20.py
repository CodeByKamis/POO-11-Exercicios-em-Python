class Peca:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.pos = None

    def mover(self, nova_pos):
        self.pos = nova_pos
        print(f"{self.cor} {self.nome} foi pra {self.pos}")

class Torre(Peca):
    def mover(self, nova_pos):
        self.pos = nova_pos
        print(f"Torre {self.cor} foi pra {self.pos}")

class Cavalo(Peca):
    def mover(self, nova_pos):
        self.pos = nova_pos
        print(f"Cavalo {self.cor} foi pra {self.pos}")

class Xadrez:
    def __init__(self):
        self.pecas = []
        self.pecas.append(Torre("torre", "branca"))
        self.pecas.append(Cavalo("cavalo", "preta"))

    def mover_peca(self):
        print("Peças:")
        for i, p in enumerate(self.pecas):
            print(f"{i} - {p.cor} {p.nome} na {p.pos}")
        escolha = int(input("Qual peça quer mover? (número) "))
        if 0 <= escolha < len(self.pecas):
            nova = input("Pra onde quer mover? (ex: A3) ")
            self.pecas[escolha].mover(nova)
        else:
            print("Número inválido.")

xadrez = Xadrez()

while True:
    print("\nXadrez Kamila")
    print("1 - Mover peça")
    print("2 - Sair")
    op = input("O que quer? ")
    if op == "1":
        xadrez.mover_peca()
    elif op == "2":
        print("tchauuuuu, mas vê se volta depois >.>")
        break
    else:
        print("Escolha errada.")
