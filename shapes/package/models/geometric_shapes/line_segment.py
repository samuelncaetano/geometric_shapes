from math import sqrt
from shapes.package.models.geometric_shape import GeometricShape
from shapes.package.models.geometric_shapes.point import Point


class LineSegment(GeometricShape):
    def __init__(self, ponto1, ponto2):
        self.__ponto1 = ponto1
        self.__ponto2 = ponto2

    def get_ponto1(self):
        return self.__ponto1

    def get_ponto2(self):
        return self.__ponto2

    def calcular_comprimento(self):
        return self.__ponto1.distancia_pontos(self.__ponto2)

    def distancia_origem(self):
        return min(self.__ponto1.distancia_origem(), self.__ponto2.distancia_origem())

    def distancia_pontos(self, ponto):
        # Distância de um ponto a uma reta
        # D = |Ax1 + By1 + C| / sqrt(A^2 + B^2)
        A = self.__ponto2.get_y() - self.__ponto1.get_y()
        B = self.__ponto1.get_x() - self.__ponto2.get_x()
        C = (self.__ponto1.get_x() * self.__ponto2.get_y()) - (
            self.__ponto2.get_x() * self.__ponto1.get_y()
        )
        return abs((A * ponto.get_x() + B * ponto.get_y() + C) / sqrt(A**2 + B**2))

    def contem_ponto(self, ponto):
        if (ponto.get_x() - self.__ponto1.get_x()) * (
            self.__ponto2.get_y() - self.__ponto1.get_y()
        ) == (ponto.get_y() - self.__ponto1.get_y()) * (
            self.__ponto2.get_x() - self.__ponto1.get_x()
        ):
            if min(
                self.__ponto1.get_x(), self.__ponto2.get_x()
            ) <= ponto.get_x() <= max(
                self.__ponto1.get_x(), self.__ponto2.get_x()
            ) and min(
                self.__ponto1.get_y(), self.__ponto2.get_y()
            ) <= ponto.get_y() <= max(
                self.__ponto1.get_y(), self.__ponto2.get_y()
            ):
                return True
        return False

    def mover(self, novo_ponto1, novo_ponto2):
        self.__ponto1 = novo_ponto1
        self.__ponto2 = novo_ponto2

    def __str__(self):
        return f"Segmento de Reta({self.__ponto1}, {self.__ponto2})"

    @staticmethod
    def criar_segmento_de_reta():
        print("Para adicionar um segmento de reta, você precisa de dois pontos.")
        ponto1 = Point.criar_ponto()
        ponto2 = Point.criar_ponto()
        return LineSegment(ponto1, ponto2)
