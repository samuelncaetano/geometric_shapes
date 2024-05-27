# pylint: disable = E0110, E0401
from unittest.mock import patch
import pytest
from src.package import Point


@pytest.fixture
def origem():
    return Point(0, 0)


@pytest.fixture
def ponto():
    return Point(3, 4)


def test_instanciar_ponto(origem, ponto):
    assert isinstance(origem, Point)
    assert isinstance(ponto, Point)


def test_obter_coordenadas_ponto(origem, ponto):
    assert origem.get_x() == 0
    assert origem.get_y() == 0
    assert ponto.get_x() == 3
    assert ponto.get_y() == 4


def test_calcular_area_ponto(origem, ponto):
    assert origem.calcular_area() == 0
    assert ponto.calcular_area() == 0


def test_calcular_perimetro_ponto(origem, ponto):
    assert origem.calcular_perimetro() == 0
    assert ponto.calcular_perimetro() == 0


def test_distancia_origem_ponto(origem, ponto):
    assert origem.distancia_origem() == 0
    assert ponto.distancia_origem() == 5


def test_distancia_pontos_ponto(origem, ponto):
    origem = Point(0, 0)
    assert origem.distancia_pontos(origem) == 0
    assert ponto.distancia_pontos(origem) == 5


def test_contem_ponto_ponto(origem, ponto):
    origem = Point(0, 0)
    ponto = Point(3, 4)
    ponto_false = Point(5, 5)
    assert origem.contem_ponto(origem) is True
    assert ponto.contem_ponto(ponto) is True
    assert origem.contem_ponto(ponto) is False
    assert ponto.contem_ponto(origem) is False
    assert origem.contem_ponto(ponto_false) is False
    assert ponto.contem_ponto(ponto_false) is False


def test_mover_ponto(origem, ponto):
    novo_ponto = Point(5, 5)
    origem.mover(novo_ponto)
    origem.mover(novo_ponto)
    ponto.mover(novo_ponto)
    ponto.mover(novo_ponto)
    assert origem.get_x() == 5
    assert origem.get_y() == 5
    assert ponto.get_x() == 5
    assert ponto.get_y() == 5


def test_str_ponto(origem, ponto):
    message_origem = "Ponto(0, 0)"
    message_ponto = "Ponto(3, 4)"
    assert str(origem) == message_origem
    assert str(ponto) == message_ponto


def test_criar_ponto():
    user_input = "3.0 4.0\n"

    with patch("builtins.input", return_value=user_input):
        ponto = Point.criar_ponto()

        assert ponto.get_x() == 3.0
        assert ponto.get_y() == 4.0
