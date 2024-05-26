from math import sqrt
from shapes.package.models.geometric_shape import GeometricShape


class Point(GeometricShape):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distancia_origem(self):
        return sqrt(self.__x**2 + self.__y**2)

    def distancia_pontos(self, ponto):
        return sqrt((self.__x - ponto.__x) ** 2 + (self.__y - ponto.__y) ** 2)

    def contem_ponto(self, ponto):
        return ponto.get_x() == self.__x and ponto.get_y() == self.__y

    def mover(self, novo_ponto):
        self.__x = novo_ponto.get_x()
        self.__y = novo_ponto.get_y()

    def __str__(self):
        return f"Ponto({self.__x}, {self.__y})"

    @staticmethod
    def criar_ponto():
        x, y = map(
            float,
            input(
                "Digite as coordenadas x e y do ponto separadas por espaço: "
            ).split(),
        )
        return Point(x, y)
