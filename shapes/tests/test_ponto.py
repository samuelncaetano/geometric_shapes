# pylint: disable=E0110, E0401
import pytest
from shapes.package import Point


@pytest.fixture
def ponto():
    return Point(0, 0)


def test_instanciar_ponto(ponto):
    assert isinstance(ponto, Point)


def test_obter_coordenadas(ponto):
    assert ponto.get_x() == 0
    assert ponto.get_y() == 0


def test_calcular_area_ponto(ponto):
    assert ponto.calcular_area() == 0


# def test_calcular_perimetro_ponto():
#     pass


# def test_contem_ponto_ponto():
#     pass


# def test_mover_ponto():
#     pass


# def test_str_ponto():
#     pass
