import random
class JogoCartas:
    def __init__(self):
        self.cartas_azul = ["1 AZUL", "2 AZUL", "3 AZUL", "4 AZUL", "5 AZUL", "6  AZUL", "7 AZUL", "8 AZUL", "9 AZUL", "0 AZUL" "+4 PRETO", "+2  AZUL" "BLOQUEIO AZUL" "REVERSE AZUL" "ESCOLHA COR"]
        self.cartas_amarela = ["1 AMARELO", "2 AMARELO", "3 AMARELO", "4 AMARELO", "5 AMARELO", "6 AMARELO", "7 AMARELO", "8 AMARELO", "9 AMARELO", "0 AMARELO" "+4 PRETO", "+2 AMARELO" "BLOQUEIO AMARELO" "REVERSE AMARELO" "ESCOLHA COR"]
        self.cartas_verde = ["1 VERDE", "2 VERDE", "3 VERDE", "4 VERDE", "5 VERDE", "6 VERDE", "7 VERDE", "8 VERDE", "9 VERDE", "0  VERDE" "+4 PRETO", "+2  VERDE" "BLOQUEIO VERDE" "REVERSE VERDE" "ESCOLHA COR"]
        self.cartas_vermelha = ["1 VERMELHO", "2 VERMELHO", "3 VERMELHO", "4 VERMELHO", "5 VERMELHO", "6 VERMELHO", "7 VERMELHO", "8 VERMELHO", "9 VERMELHO", "0 VERMELHO" "+4 PRETO", "+2 VERMELHO" "BLOQUEIO VERMELHO" "REVERSE VERMELHO" "ESCOLHA COR"]
        self.todas_cartas = zip(self.cartas_azul, self.cartas_amarela, self.cartas_verde, self.cartas_vermelha)
    def emabaralhar (self):
        random.shuffle(self.todas_cartas)

    def jogadas (self):
        jogador1 = input("Qual é o seu nome jogador 1: ")
        cartas1 = self.todas_cartas[:5]

        jogador2 = input("Qual é o seu nome jogador 2: ")
        cartas2 = self.todas_cartas[5:10]

        vez = 1
        while True:
            if vez %2 != 0:
                jogadorda_vez = jogador1
                cartas_atual = cartas1
            else:
                jogadorda_vez = jogador2
                cartas_atual = cartas2

                print(f"Jogador(a) {jogadorda_vez} sua vez\n Suas cartas são {cartas1}")
                jogada = input(f"{jogadorda_vez}, escolha uma carta para jogar ou escreva passar para passar a vez: ")

                if jogada == "passar":
                    print(f"O(A) {jogadorda_vez} passou a vez")
                    continue
                if jogada in cartas_atual:
                    cartas_atual.remove(jogada)
                    print(f"{jogadorda_vez} jogoo {jogada}")
                else:
                    print("carta inválida, tente de novo")
                    continue

jogocartas = JogoCartas()
print("Seja bem vindo ao jogo do uno!")
