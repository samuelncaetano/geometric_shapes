from src.package.domain import IRepository


class CalculateMetrics:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def calcular_area(self, index):
        forma = self.repository.get(index)
        if forma:
            return forma.calcular_area()

    def calcular_perimetro(self, index):
        forma = self.repository.get(index)
        if forma:
            return forma.calcular_perimetro()

    def distancia_origem(self, index):
        forma = self.repository.get(index)
        if forma:
            return forma.distancia_origem()

    def distancia_pontos(self, index, ponto):
        forma = self.repository.get(index)
        if forma:
            return forma.distancia_pontos(ponto)

    def contem_ponto(self, index, ponto):
        forma = self.repository.get(index)
        if forma:
            return forma.contem_ponto(ponto)
