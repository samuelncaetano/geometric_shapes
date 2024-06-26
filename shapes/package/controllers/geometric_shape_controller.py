# pylint: disable=R1710
from shapes.package.models import Point, LineSegment, Circle, Rectangle, Triangle


class GeometricShapeController:
    def __init__(self, repository):
        self.__repository = repository

    def adicionar_forma_geometrica(self, forma_geometrica):
        self.__repository.add(forma_geometrica)

    def listar_formas_geometricas(self):
        formas = self.__repository.list_all()
        if not formas:
            print("Nenhuma forma geométrica cadastrada.")
            return

        print("### Formas Geométricas ###")
        for i, forma in enumerate(formas, start=1):
            print(f"{i}. {forma}")

    def calcular_area(self, index):
        forma = self.__repository.get(index)
        if forma:
            return forma.calcular_area()

    def calcular_perimetro(self, index):
        forma = self.__repository.get(index)
        if forma:
            return forma.calcular_perimetro()

    def distancia_origem(self, index):
        forma = self.__repository.get(index)
        if forma:
            return forma.distancia_origem()

    def distancia_pontos(self, index, ponto):
        forma = self.__repository.get(index)
        if forma:
            return forma.distancia_pontos(ponto)

    def contem_ponto(self, index, ponto):
        forma = self.__repository.get(index)
        if forma:
            return forma.contem_ponto(ponto)

    def mover_formas(self, index, novo_ponto):
        forma = self.__repository.get(index)
        if forma:
            return forma.mover(novo_ponto)

    def mover_segmento_de_reta(self, index, novo_ponto1, novo_ponto2):
        forma = self.__repository.get(index)
        if forma:
            return forma.mover(novo_ponto1, novo_ponto2)

    def adicionar_ponto(self):
        ponto = Point.criar_ponto()
        self.adicionar_forma_geometrica(ponto)

    def adicionar_segmento_de_reta(self):
        reta = LineSegment.criar_segmento_de_reta()
        self.adicionar_forma_geometrica(reta)

    def adicionar_circulo(self):
        circulo = Circle.criar_circulo()
        self.adicionar_forma_geometrica(circulo)

    def adicionar_retangulo(self):
        retangulo = Rectangle.criar_retangulo()
        self.adicionar_forma_geometrica(retangulo)

    def adicionar_triangulo(self):
        triangulo = Triangle.criar_triangulo()
        self.adicionar_forma_geometrica(triangulo)
