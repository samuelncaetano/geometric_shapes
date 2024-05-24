from abc import ABC, abstractmethod


class GeometricShape(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    @abstractmethod
    def distancia_origem(self):
        pass

    @abstractmethod
    def distancia_pontos(self):
        pass

    @abstractmethod
    def contem_ponto(self, ponto):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
