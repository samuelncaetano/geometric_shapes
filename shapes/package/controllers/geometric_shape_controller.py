# pylint: disable=R1710
from shapes.package.models import Point, LineSegment


class GeometricShapeController:
    def __init__(self):
        self.__geometric_shapes = []

    def adicionar_forma_geometrica(self, forma_geometrica):
        self.__geometric_shapes.append(forma_geometrica)

    def listar_formas_geometricas(self):
        if not self.__geometric_shapes:
            print("Nenhuma forma geométrica cadastrada.")

        print("### Formas Geométricas ###")
        for i, forma in enumerate(self.__geometric_shapes, start=1):
            print(f"{i}. {forma}")

    # Usar os métodos das classes no controller
    def calcular_area(self, index):
        if 0 <= index < len(self.__geometric_shapes):
            forma = self.__geometric_shapes[index]
            area = forma.calcular_area()
            return area

    def calcular_perimetro(self, index):
        if 0 <= index < len(self.__geometric_shapes):
            forma = self.__geometric_shapes[index]
            perimetro = forma.calcular_perimetro()
            return perimetro

    def distancia_origem(self, index):
        if 0 <= index < len(self.__geometric_shapes):
            forma = self.__geometric_shapes[index]
            distancia_origem = forma.distancia_origem()
            return distancia_origem

    def distancia_pontos(self, index, ponto):
        if 0 <= index < len(self.__geometric_shapes):
            forma = self.__geometric_shapes[index]
            distancia_pontos = forma.distancia_pontos(ponto)
            return distancia_pontos

    def contem_ponto(self, index, ponto):
        if 0 <= index < len(self.__geometric_shapes):
            forma = self.__geometric_shapes[index]
            resultado = forma.contem_ponto(ponto)
            return resultado

    def mover_formas(self, index, novo_ponto):
        if 0 <= index < len(self.__geometric_shapes):
            forma = self.__geometric_shapes[index]
            resultado = forma.mover(novo_ponto)
            return resultado

    def mover_segmento_de_reta(self, index, novo_ponto1, novo_ponto2):
        if 0 <= index < len(self.__geometric_shapes):
            forma = self.__geometric_shapes[index]
            resultado = forma.mover(novo_ponto1, novo_ponto2)
            return resultado

    # Adicionar formas no controller
    def adicionar_ponto(self):
        ponto = Point.criar_ponto()
        self.adicionar_forma_geometrica(ponto)

    def adicionar_segmento_de_reta(self):
        reta = LineSegment.criar_segmento_de_reta()
        self.adicionar_forma_geometrica(reta)
