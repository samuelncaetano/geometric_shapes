# pylint: disable=R1710
from src.package import CalculateMetrics, CreateShape, MoveShape


class GeometricShapeController:
    def __init__(self, repository, factory):
        self.create_shape_use_case = CreateShape(repository, factory)
        self.move_shape_use_case = MoveShape(repository)
        self.calculate_metrics_use_case = CalculateMetrics(repository)

    def adicionar_forma_geometrica(self, tipo_forma):
        self.create_shape_use_case.execute(tipo_forma)

    def listar_formas_geometricas(self):
        return self.create_shape_use_case.repository.list_all()

    def calcular_area(self, index):
        return self.calculate_metrics_use_case.calcular_area(index)

    def calcular_perimetro(self, index):
        return self.calculate_metrics_use_case.calcular_perimetro(index)

    def distancia_origem(self, index):
        return self.calculate_metrics_use_case.distancia_origem(index)

    def distancia_pontos(self, index, ponto):
        return self.calculate_metrics_use_case.distancia_pontos(index, ponto)

    def contem_ponto(self, index, ponto):
        return self.calculate_metrics_use_case.contem_ponto(index, ponto)

    def mover_forma(self, index, novo_ponto):
        self.move_shape_use_case.execute(index, novo_ponto)

    def mover_segmento_de_reta(self, index, novo_ponto1, novo_ponto2):
        self.move_shape_use_case.execute(index, novo_ponto1, novo_ponto2)

    def adicionar_ponto(self):
        self.adicionar_forma_geometrica("ponto")

    def adicionar_segmento_de_reta(self):
        self.adicionar_forma_geometrica("segmento_de_reta")

    def adicionar_circulo(self):
        self.adicionar_forma_geometrica("circulo")

    def adicionar_retangulo(self):
        self.adicionar_forma_geometrica("retangulo")

    def adicionar_triangulo(self):
        self.adicionar_forma_geometrica("triangulo")
