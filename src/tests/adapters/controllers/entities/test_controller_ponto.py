# pylint: disable = E0110, E0401, R0801
import pytest
from src.package import Point, GeometricShapeController, InMemoryRepository


@pytest.fixture
def repository():
    return InMemoryRepository()


@pytest.fixture
def controller(repository):
    return GeometricShapeController(repository)


@pytest.fixture
def ponto():
    return Point(0, 0)


# Point
def test_calcular_area_ponto(controller, ponto):
    controller.adicionar_forma_geometrica(ponto)
    assert controller.calcular_area(0) == 0


def test_calcular_perimetro_ponto(controller, ponto):
    controller.adicionar_forma_geometrica(ponto)
    assert controller.calcular_perimetro(0) == 0


def test_distancia_origem_ponto(controller, ponto):
    controller.adicionar_forma_geometrica(ponto)
    assert controller.distancia_origem(0) == 0


def test_distancia_pontos_ponto(controller, ponto):
    controller.adicionar_forma_geometrica(ponto)
    origem = Point(0, 0)
    assert controller.distancia_pontos(0, origem) == 0


def test_contem_ponto_ponto(controller, ponto):
    controller.adicionar_forma_geometrica(ponto)
    origem = Point(0, 0)
    assert controller.contem_ponto(0, origem) is True


def test_mover_ponto(controller, ponto):
    controller.adicionar_forma_geometrica(ponto)
    controller.mover_formas(0, Point(2, 2))
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_x() == 2
    assert item.get_y() == 2
