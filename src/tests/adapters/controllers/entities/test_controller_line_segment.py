# pylint: disable = E0110, E0401, R0801
import pytest
from src.package import Point, LineSegment, GeometricShapeController, InMemoryRepository


@pytest.fixture
def repository():
    return InMemoryRepository()


@pytest.fixture
def controller(repository):
    return GeometricShapeController(repository)


@pytest.fixture
def reta():
    return LineSegment(Point(1, 1), Point(4, 4))


# LineSegment
def test_calcular_area_reta(controller, reta):
    controller.adicionar_forma_geometrica(reta)
    assert controller.calcular_area(0) == 0


def test_calcular_perimetro_reta(controller, reta):
    controller.adicionar_forma_geometrica(reta)
    assert controller.calcular_perimetro(0) == 0


def test_distancia_origem_reta(controller, reta):
    controller.adicionar_forma_geometrica(reta)
    origem = min(Point(1, 1).distancia_origem(), Point(4, 4).distancia_origem())
    assert controller.distancia_origem(0) == origem


def test_distancia_pontos_reta(controller, reta):
    origem = Point(0, 0)
    controller.adicionar_forma_geometrica(reta)
    assert controller.distancia_pontos(0, origem) == 0


def test_contem_ponto_reta(controller, reta):
    ponto = Point(2, 2)
    controller.adicionar_forma_geometrica(reta)
    assert controller.contem_ponto(0, ponto) is True


def test_mover_reta(controller, reta):
    controller.adicionar_forma_geometrica(reta)
    controller.mover_segmento_de_reta(0, Point(2, 2), Point(5, 5))
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_ponto1().get_x() == 2
    assert item.get_ponto1().get_y() == 2
    assert item.get_ponto2().get_x() == 5
    assert item.get_ponto2().get_y() == 5
