# pylint: disable = E0110, E0401, R0801
import pytest
from src.package import Point, Rectangle, GeometricShapeController, InMemoryRepository


@pytest.fixture
def repository():
    return InMemoryRepository()


@pytest.fixture
def controller(repository):
    return GeometricShapeController(repository)


@pytest.fixture
def retangulo():
    return Rectangle(Point(0, 0), 4, 4)


# Rectangle
def test_calcular_area_retangulo(controller, retangulo):
    area = 4 * 4
    controller.adicionar_forma_geometrica(retangulo)
    assert controller.calcular_area(0) == area


def test_calcular_perimetro_retangulo(controller, retangulo):
    perimetro = 2 * (4 + 4)
    controller.adicionar_forma_geometrica(retangulo)
    assert controller.calcular_perimetro(0) == perimetro


def test_distancia_origem_retangulo(controller, retangulo):
    ponto_superior_esquerdo = Point(-2, 2)
    ponto_inferior_direito = Point(2, -2)
    origem = min(
        ponto_inferior_direito.distancia_origem(),
        ponto_superior_esquerdo.distancia_origem(),
    )
    controller.adicionar_forma_geometrica(retangulo)
    assert controller.distancia_origem(0) == origem


def test_distancia_pontos_retangulo(controller, retangulo):
    ponto = Point(1, 1)
    ponto_superior_esquerdo = Point(-2, 2)
    ponto_inferior_direito = Point(2, -2)
    distancias = [
        ponto_inferior_direito.distancia_pontos(ponto),
        ponto_superior_esquerdo.distancia_pontos(ponto),
        ponto.distancia_pontos(
            Point(
                ponto_inferior_direito.get_x(),
                ponto_superior_esquerdo.get_y(),
            )
        ),
        ponto.distancia_pontos(
            Point(
                ponto_superior_esquerdo.get_x(),
                ponto_inferior_direito.get_y(),
            )
        ),
    ]
    controller.adicionar_forma_geometrica(retangulo)
    assert controller.distancia_pontos(0, ponto) == min(distancias)


def test_contem_ponto_retangulo(controller, retangulo):
    true = Point(2, 2)
    false = Point(5, 5)
    controller.adicionar_forma_geometrica(retangulo)
    assert controller.contem_ponto(0, true) is True
    assert controller.contem_ponto(0, false) is False


def test_mover_retangulo(controller, retangulo):
    controller.adicionar_forma_geometrica(retangulo)
    controller.mover_formas(0, Point(4, 4))
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_centro().get_x() == 4
    assert item.get_centro().get_y() == 4
