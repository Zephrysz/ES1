import math


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio**2)

    def perimetro(self):
        return 2 * math.pi * self.raio


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return 0.5 * self.base * self.altura


class Hexagono:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (3 * math.sqrt(3) * self.lado**2) / 2

    def perimetro(self):
        return 6 * self.lado
