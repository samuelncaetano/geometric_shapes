from shapes.package.models.geometric_shape import GeometricShape
from shapes.package.models.geometric_shapes.point import Point


class Rectangle(GeometricShape):
    def __init__(self, centro, largura, altura):
        self.__centro = centro
        self.__largura = largura
        self.__altura = altura
        self.__atualizar_pontos()

    def get_centro(self):
        return self.__centro

    def get_largura(self):
        return self.__largura

    def get_altura(self):
        return self.__altura

    def __atualizar_pontos(self):
        self.__ponto_superior_esquerdo = Point(
            self.__centro.get_x() - self.__largura / 2,
            self.__centro.get_y() + self.__altura / 2,
        )
        self.__ponto_inferior_direito = Point(
            self.__centro.get_x() + self.__largura / 2,
            self.__centro.get_y() - self.__altura / 2,
        )

    def calcular_area(self):
        return self.__largura * self.__altura

    def calcular_perimetro(self):
        return 2 * (self.__largura + self.__altura)

    def distancia_origem(self):
        return min(
            self.__ponto_inferior_direito.distancia_origem(),
            self.__ponto_superior_esquerdo.distancia_origem(),
        )

    def distancia_pontos(self, ponto):
        distancias = [
            self.__ponto_inferior_direito.distancia_pontos(ponto),
            self.__ponto_superior_esquerdo.distancia_pontos(ponto),
            ponto.distancia_pontos(
                Point(
                    self.__ponto_inferior_direito.get_x(),
                    self.__ponto_superior_esquerdo.get_y(),
                )
            ),
            ponto.distancia_pontos(
                Point(
                    self.__ponto_superior_esquerdo.get_x(),
                    self.__ponto_inferior_direito.get_y(),
                )
            ),
        ]
        return min(distancias)

    def contem_ponto(self, ponto):
        return (
            self.__ponto_superior_esquerdo.get_x()
            <= ponto.get_x()
            <= self.__ponto_inferior_direito.get_x()
            and self.__ponto_inferior_direito.get_y()
            <= ponto.get_y()
            <= self.__ponto_superior_esquerdo.get_y()
        )

    def mover(self, novo_ponto):
        self.__centro = novo_ponto
        self.__atualizar_pontos()

    def __str__(self):
        return f"Retângulo(Centro: {self.__centro}, Largura: {self.__largura}, Altura: {self.__altura})"

    @staticmethod
    def criar_retangulo():
        x, y = map(
            float,
            input(
                "Digite as coordenadas x e y do centro do retângulo separadas por espaço: "
            ).split(),
        )
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        centro = Point(x, y)
        return Rectangle(centro, largura, altura)
