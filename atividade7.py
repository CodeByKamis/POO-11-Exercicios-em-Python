class Triangulo:
    def __init__(self, a, b, c, base, altura):
        self.a=a
        self.b = b
        self.c=c
        self.base = base
        self.altura = altura

    def verificando_avalidade(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            return False

    def area (self):
        calculo = (self.base*self.altura)/2 
        return (f"O valor da área é de {calculo}cm")

triangulo = Triangulo(10, 15, 10, 25, 9)
if triangulo.verificando_avalidade():
    print("O triângulo é válido") 
    print(f"e o valor da sua área é: {triangulo.area()}")
else:
    print("O triângulo não é válido, então não é possível calcular a sua área")