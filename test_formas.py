import pytest
from formas import Circulo, Retangulo, Triangulo, Hexagono


def test_area_circulo():
    circulo = Circulo(10)
    assert pytest.approx(circulo.area(), 0.01) == 314.16


def test_perimetro_circulo():
    circulo = Circulo(10)
    assert pytest.approx(circulo.perimetro(), 0.01) == 62.83


def test_area_retangulo():
    retangulo = Retangulo(10, 20)
    assert retangulo.area() == 200


def test_perimetro_retangulo():
    retangulo = Retangulo(10, 20)
    assert retangulo.perimetro() == 60


def test_area_triangulo():
    triangulo = Triangulo(10, 20)
    assert triangulo.area() == 100


def test_area_hexagono():
    hexagono = Hexagono(10)
    assert pytest.approx(hexagono.area(), 0.01) == 259.80


def test_area_hexagono():
    hexagono = Hexagono(10)
    assert hexagono.perimetro() == 60
