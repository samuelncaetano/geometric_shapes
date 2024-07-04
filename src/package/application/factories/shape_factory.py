# pylint: disable = R1705
from src.package.domain import Point, LineSegment, Circle, Rectangle, Triangle


class ShapeFactory:
    @staticmethod
    def criar_forma(tipo_forma):
        if tipo_forma == "ponto":
            return Point.criar_ponto()
        elif tipo_forma == "segmento_de_reta":
            return LineSegment.criar_segmento_de_reta()
        elif tipo_forma == "circulo":
            return Circle.criar_circulo()
        elif tipo_forma == "retangulo":
            return Rectangle.criar_retangulo()
        elif tipo_forma == "triangulo":
            return Triangle.criar_triangulo()
        else:
            raise ValueError("Tipo de forma desconhecido.")
