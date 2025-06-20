import random
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 100
        self.forca = 20
        self.defesa = 10
        self.xp = 0
        self.nivel = 1
        self.itens = {"poção": 2}

    def atacar(self, alvo):
        dano = max(0, self.forca - alvo.defesa + random.randint(-5, 5))
        alvo.saude -= dano
        print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano!")

    def usar_pocao(self):
        if self.itens.get("poção", 0) > 0:
            self.saude += 30
            self.itens["poção"] -= 1
            print(f"{self.nome} usou uma poção e recuperou 30 de saúde!")
        else:
            print("Sem poção!")

    def verificar_vitoria(self, alvo):
        if alvo.saude <= 0:
            self.xp += 20
            print(f"{self.nome} venceu a batalha e ganhou 20xp e vai tomandooo!")
            if self.xp >= 100:
                self.nivel += 1
                self.xp = 0
                self.forca += 5
                self.defesa += 3
                print(f"{self.nome} subiu para o nível {self.nivel}!")
            return True
        return False

def batalha(p1, p2):
    vez = 0
    while p1.saude > 0 and p2.saude > 0:
        atacante = p1 if vez % 2 == 0 else p2
        defensor = p2 if vez % 2 == 0 else p1
        print(f"\n{atacante.nome} - HP: {atacante.saude} | {defensor.nome} - HP: {defensor.saude}")
        escolha = input(f"{atacante.nome}, digite 'a' para atacar ou 'p' para usar poção: ").lower()
        if escolha == 'a':
            atacante.atacar(defensor)
        elif escolha == 'p':
            atacante.usar_pocao()
        else:
            print("Comando inválido!")
            continue
        if atacante.verificar_vitoria(defensor):
            break
        vez += 1

p1 = Personagem(input("Nome do personagem 1: "))
p2 = Personagem(input("Nome do personagem 2: "))
batalha(p1, p2)