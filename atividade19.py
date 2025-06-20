import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero = random.randint(1, 100)

    def jogar(self):
        print("Tenta adivinhar o número entre 1 e 100!")
        tentativas = 0
        while True:
            try:
                palpite = int(input("Seu palpite: "))
                tentativas += 1
                if palpite == self.numero:
                    print(f"AEEEEEEEEE Acertou! Foram {tentativas} tentativas.")
                    break
                elif palpite < self.numero:
                    print("É maior que isso.")
                else:
                    print("É menor que isso.")
            except:
                print("Coloca um número aí!")

jogo = JogoAdivinhacao()
jogo.jogar()
