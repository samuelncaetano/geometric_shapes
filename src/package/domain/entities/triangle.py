from src.package.domain.entities.geometric_shape import GeometricShape
from src.package.domain.entities.point import Point
from src.package.domain.entities.line_segment import LineSegment


class Triangle(GeometricShape):
    def __init__(self, ponto1, ponto2, ponto3):
        if self.formar_triangulo(ponto1, ponto2, ponto3):
            self.__ponto1 = ponto1
            self.__ponto2 = ponto2
            self.__ponto3 = ponto3
        else:
            raise ValueError("Os pontos fornecidos não formam um triângulo válido.")

    def get_ponto1(self):
        return self.__ponto1

    def get_ponto2(self):
        return self.__ponto2

    def get_ponto3(self):
        return self.__ponto3

    def calcular_centro(self):
        x = (self.__ponto1.get_x() + self.__ponto2.get_x() + self.__ponto3.get_x()) / 3
        y = (self.__ponto1.get_y() + self.__ponto2.get_y() + self.__ponto3.get_y()) / 3
        centro_x = round(x, 1)
        centro_y = round(y, 1)
        return Point(centro_x, centro_y)

    def calcular_area(self):
        x1, y1 = self.__ponto1.get_x(), self.__ponto1.get_y()
        x2, y2 = self.__ponto2.get_x(), self.__ponto2.get_y()
        x3, y3 = self.__ponto3.get_x(), self.__ponto3.get_y()
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def calcular_perimetro(self):
        a = LineSegment(self.__ponto1, self.__ponto2).calcular_comprimento()
        b = LineSegment(self.__ponto2, self.__ponto3).calcular_comprimento()
        c = LineSegment(self.__ponto3, self.__ponto1).calcular_comprimento()
        return a + b + c

    def distancia_origem(self):
        return min(
            self.__ponto1.distancia_origem(),
            self.__ponto2.distancia_origem(),
            self.__ponto3.distancia_origem(),
        )

    def distancia_pontos(self, ponto):
        distancias = [
            self.__ponto1.distancia_pontos(ponto),
            self.__ponto2.distancia_pontos(ponto),
            self.__ponto3.distancia_pontos(ponto),
        ]
        return min(distancias)

    def contem_ponto(self, ponto):
        def area(p1, p2, p3):
            return abs(
                (
                    p1.get_x() * (p2.get_y() - p3.get_y())
                    + p2.get_x() * (p3.get_y() - p1.get_y())
                    + p3.get_x() * (p1.get_y() - p2.get_y())
                )
                / 2
            )

        a = self.calcular_area()
        a1 = area(ponto, self.__ponto2, self.__ponto3)
        a2 = area(self.__ponto1, ponto, self.__ponto3)
        a3 = area(self.__ponto1, self.__ponto2, ponto)
        return a == (a1 + a2 + a3)

    def mover(self, novo_ponto):
        dx = novo_ponto.get_x() - self.calcular_centro().get_x()
        dy = novo_ponto.get_y() - self.calcular_centro().get_y()
        self.__ponto1 = Point(self.__ponto1.get_x() + dx, self.__ponto1.get_y() + dy)
        self.__ponto2 = Point(self.__ponto2.get_x() + dx, self.__ponto2.get_y() + dy)
        self.__ponto3 = Point(self.__ponto3.get_x() + dx, self.__ponto3.get_y() + dy)

    def __str__(self):
        return f"Triângulo(Centro: {self.calcular_centro()}, Ponto1: {self.__ponto1}, Ponto2: {self.__ponto2}, Ponto3: {self.__ponto3})"

    @staticmethod
    def formar_triangulo(ponto1, ponto2, ponto3):
        def calcular_area(p1, p2, p3):
            return abs(
                (
                    p1.get_x() * (p2.get_y() - p3.get_y())
                    + p2.get_x() * (p3.get_y() - p1.get_y())
                    + p3.get_x() * (p1.get_y() - p2.get_y())
                )
                / 2
            )

        area_total = calcular_area(ponto1, ponto2, ponto3)
        return area_total > 0

    @staticmethod
    def criar_triangulo():
        print("Digite as coordenadas dos três pontos do triângulo:")
        ponto1 = Point.criar_ponto()
        ponto2 = Point.criar_ponto()
        ponto3 = Point.criar_ponto()
        return Triangle(ponto1, ponto2, ponto3)
