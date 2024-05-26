# pylint: disable = E0110, E0401, R0801
from math import pi
import pytest
from shapes.package.models import Point, Circle
from shapes.package.controllers import GeometricShapeController
from shapes.package.repository.in_memory_repository import InMemoryRepository


@pytest.fixture
def repository():
    return InMemoryRepository()


@pytest.fixture
def controller(repository):
    return GeometricShapeController(repository)


@pytest.fixture
def circulo():
    return Circle(Point(0, 0), 4)


# Circle
def test_calcular_area_circulo(controller, circulo):
    area = pi * 4**2
    controller.adicionar_forma_geometrica(circulo)
    assert controller.calcular_area(0) == area


def test_calcular_perimetro_circulo(controller, circulo):
    perimetro = 2 * pi * 4
    controller.adicionar_forma_geometrica(circulo)
    assert controller.calcular_perimetro(0) == perimetro


def test_distancia_origem_circulo(controller, circulo):
    controller.adicionar_forma_geometrica(circulo)
    assert controller.distancia_origem(0) == 0


def test_distancia_pontos_circulo(controller, circulo):
    ponto = Point(1, 1)
    distancia = abs(circulo.get_centro().distancia_pontos(ponto) - circulo.get_raio())
    controller.adicionar_forma_geometrica(circulo)
    assert controller.distancia_pontos(0, ponto) == distancia


def test_contem_ponto_circulo(controller, circulo):
    true = Point(2, 2)
    false = Point(5, 5)
    controller.adicionar_forma_geometrica(circulo)
    assert controller.contem_ponto(0, true) is True
    assert controller.contem_ponto(0, false) is False


def test_mover_circulo(controller, circulo):
    controller.adicionar_forma_geometrica(circulo)
    controller.mover_formas(0, Point(4, 4))
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_centro().get_x() == 4
    assert item.get_centro().get_y() == 4
