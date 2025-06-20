class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

retangulo = Retangulo(10, 25)
print(f"O valor da área é: {retangulo.area()}cm²")
print(f"O valor do perímetro é: {retangulo.perimetro()}cm")
