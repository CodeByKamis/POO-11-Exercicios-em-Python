class Carro:
    def __init__(self, marca, modelo, velocidade_atual):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
    
    def aumentar_velocidade (self):
        aumentar = int(input("Digite o quanto você deseja aumentar a velocidade: "))
        calculo = aumentar + self.velocidade_atual
        print(f"A velocidade atual é de: {calculo}km/h")
    
    def frear (self):
        print(f"O carro freou!")

    def mostrar_velocidade (self):
        print(f"A velocidade atual do carro é igual a: {self.velocidade_atual}")

carro = Carro("Fiat", "Fiat 500c", 80)
pergunta = int(input("Você deseja ver a velocidade atual(1), aumentar a velocidade(2) ou freiar o carro(3)? "))
if pergunta == 1:
        carro.mostrar_velocidade()
elif pergunta == 2:
        carro.aumentar_velocidade()
elif pergunta == 3:
        carro.frear()
