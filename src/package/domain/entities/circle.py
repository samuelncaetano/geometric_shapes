from math import pi
from src.package.domain.entities.geometric_shape import GeometricShape
from src.package.domain.entities.point import Point


class Circle(GeometricShape):
    def __init__(self, centro, raio):
        self.__centro = centro
        self.__raio = raio

    def get_centro(self):
        return self.__centro

    def get_raio(self):
        return self.__raio

    def calcular_area(self):
        return pi * self.__raio**2

    def calcular_perimetro(self):
        return 2 * pi * self.__raio

    def distancia_origem(self):
        return self.__centro.distancia_origem()

    def distancia_pontos(self, ponto):
        return abs(self.__centro.distancia_pontos(ponto) - self.__raio)

    def contem_ponto(self, ponto):
        return self.__centro.distancia_pontos(ponto) <= self.__raio

    def mover(self, novo_ponto):
        self.__centro = novo_ponto

    def __str__(self):
        return f"Círculo(Centro: {self.__centro}, Raio: {self.__raio})"

    @staticmethod
    def criar_circulo():
        x, y = map(
            float,
            input(
                "Digite as coordenadas x e y do centro do círculo separadas por espaço: "
            ).split(),
        )
        raio = float(input("Digite o raio do círculo: "))
        centro = Point(x, y)
        return Circle(centro, raio)
