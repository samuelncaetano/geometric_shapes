# pylint: disable = E0110, E0401, R0801
import pytest
from src.package import Point, Triangle, LineSegment, GeometricShapeController, InMemoryRepository


@pytest.fixture
def repository():
    return InMemoryRepository()


@pytest.fixture
def controller(repository):
    return GeometricShapeController(repository)


@pytest.fixture
def triangulo():
    return Triangle(Point(0, 0), Point(0, 2), Point(3, 0))


# Triangle
def test_calcular_area_triangulo(controller, triangulo):
    ponto1 = Point(0, 0)
    ponto2 = Point(0, 2)
    ponto3 = Point(3, 0)
    x1, y1 = ponto1.get_x(), ponto1.get_y()
    x2, y2 = ponto2.get_x(), ponto2.get_y()
    x3, y3 = ponto3.get_x(), ponto3.get_y()
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    controller.adicionar_forma_geometrica(triangulo)
    assert controller.calcular_area(0) == area


def test_calcular_perimetro_triangulo(controller, triangulo):
    ponto1 = Point(0, 0)
    ponto2 = Point(0, 2)
    ponto3 = Point(3, 0)
    a = LineSegment(ponto1, ponto2).calcular_comprimento()
    b = LineSegment(ponto2, ponto3).calcular_comprimento()
    c = LineSegment(ponto3, ponto1).calcular_comprimento()
    perimetro = a + b + c
    controller.adicionar_forma_geometrica(triangulo)
    assert controller.calcular_perimetro(0) == perimetro


def test_distancia_origem_triangulo(controller, triangulo):
    ponto1 = Point(0, 0)
    ponto2 = Point(0, 2)
    ponto3 = Point(3, 0)
    origem = min(
        ponto1.distancia_origem(),
        ponto2.distancia_origem(),
        ponto3.distancia_origem(),
    )
    controller.adicionar_forma_geometrica(triangulo)
    assert controller.distancia_origem(0) == origem


def test_distancia_pontos_triangulo(controller, triangulo):
    ponto1 = Point(0, 0)
    ponto2 = Point(0, 2)
    ponto3 = Point(3, 0)
    ponto = Point(1, 1)
    distancias = [
        ponto1.distancia_pontos(ponto),
        ponto2.distancia_pontos(ponto),
        ponto3.distancia_pontos(ponto),
    ]

    controller.adicionar_forma_geometrica(triangulo)
    assert controller.distancia_pontos(0, ponto) == min(distancias)


def test_contem_ponto_triangulo(controller, triangulo):
    true = Point(1.5, 1)
    false = Point(5, 5)
    controller.adicionar_forma_geometrica(triangulo)
    assert controller.contem_ponto(0, true) is True
    assert controller.contem_ponto(0, false) is False


def test_mover_triangulo(controller, triangulo):
    controller.adicionar_forma_geometrica(triangulo)
    controller.mover_formas(0, Point(4, 4))
    item = controller._GeometricShapeController__repository.get(0)
    assert item.calcular_centro().get_x() == 4
    assert item.calcular_centro().get_y() == 4
