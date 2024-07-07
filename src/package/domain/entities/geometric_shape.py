# pylint: disable = R0801
from abc import ABC, abstractmethod


class GeometricShape(ABC):
    def calcular_area(self):
        return 0

    def calcular_perimetro(self):
        return 0

    @abstractmethod
    def distancia_origem(self):
        pass

    @abstractmethod
    def distancia_pontos(self, ponto):
        pass

    @abstractmethod
    def contem_ponto(self, ponto):
        pass

    def mover(self):
        pass

    def __str__(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    @staticmethod
    @abstractmethod
    def from_dict(data):
        pass
