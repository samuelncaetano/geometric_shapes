from shapes.package.models.geometric_shape import GeometricShape
from shapes.package.models.geometric_shapes.line_segment import LineSegment
from shapes.package.models.geometric_shapes.point import Point


class Triangle(GeometricShape):
    def __init__(self, centro, ponto1, ponto2, ponto3):
        self.__centro = centro
        self.__ponto1 = ponto1
        self.__ponto2 = ponto2
        self.__ponto3 = ponto3

    def get_centro(self):
        return self.__centro

    def get_ponto1(self):
        return self.__ponto1

    def get_ponto2(self):
        return self.__ponto2

    def get_ponto3(self):
        return self.__ponto3

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
        dx = novo_ponto.get_x() - self.__centro.get_x()
        dy = novo_ponto.get_y() - self.__centro.get_y()
        self.__centro = novo_ponto
        self.__ponto1 = Point(self.__ponto1.get_x() + dx, self.__ponto1.get_y() + dy)
        self.__ponto2 = Point(self.__ponto2.get_x() + dx, self.__ponto2.get_y() + dy)
        self.__ponto3 = Point(self.__ponto3.get_x() + dx, self.__ponto3.get_y() + dy)

    def __str__(self):
        return f"Triângulo(Centro: {self.__centro}, Ponto1: {self.__ponto1}, Ponto2: {self.__ponto2}, Ponto3: {self.__ponto3})"

    @staticmethod
    def criar_triangulo():
        print("Digite as coordenadas x e y do centro do triângulo")
        centro = Point.criar_ponto()
        print("Digite as coordenadas dos três pontos do triângulo:")
        ponto1 = Point.criar_ponto()
        ponto2 = Point.criar_ponto()
        ponto3 = Point.criar_ponto()
        print("Triângulo adicionado com sucesso.")
        return Triangle(centro, ponto1, ponto2, ponto3)
