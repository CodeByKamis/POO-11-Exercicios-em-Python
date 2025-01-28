class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.1416
    def area(self):
        return self.pi * (self.raio **2)
    def perimetro(self):
        return 2 * self.pi * self.raio

circulo = Circulo(5)
print (f"O valor da área do Círculo é: {circulo.area():.5f} ")
print (f"O valor do perimetro do círculo é {circulo.perimetro():.5f}")