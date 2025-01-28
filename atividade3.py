class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area (self, base):
        self.base = base
        base = 10
        calculo = base * self.altura
        return calculo
    
    def perimetro (self, comprimento):
        self.comprimento = comprimento
        calculo = 2 * comprimento * self.largura
        return calculo
    
retangulo = Retangulo(10, 25)
print(f"O valor da área é de: {retangulo.area(10)}cm")
print(f"O valor do perimetro é de: {retangulo.perimetro(20)}cm")
