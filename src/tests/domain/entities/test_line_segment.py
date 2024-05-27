# pylint: disable = E0110, E0401
from math import sqrt
from unittest.mock import patch
import pytest
from src.package import LineSegment, Point


@pytest.fixture
def reta():
    return LineSegment(Point(1, 1), Point(4, 4))


def test_instanciar_reta(reta):
    assert isinstance(reta, LineSegment)


def test_obter_coordenadas_reta(reta):
    assert reta.get_ponto1().get_x() == 1
    assert reta.get_ponto1().get_y() == 1
    assert reta.get_ponto2().get_x() == 4
    assert reta.get_ponto2().get_y() == 4


def test_calcular_area_reta(reta):
    assert reta.calcular_area() == 0


def test_calcular_perimetro_reta(reta):
    assert reta.calcular_perimetro() == 0


def test_calcular_comprimento_reta(reta):
    comprimento = sqrt((4 - 1) ** 2 + (4 - 1) ** 2)
    assert reta.calcular_comprimento() == comprimento


def test_distancia_origem_reta(reta):
    origem = min(Point(1, 1).distancia_origem(), Point(4, 4).distancia_origem())
    assert reta.distancia_origem() == origem


def test_distancia_pontos_reta(reta):
    origem = Point(0, 0)
    assert reta.distancia_pontos(origem) == 0


def test_contem_ponto_reta(reta):
    true = Point(2, 2)
    false = Point(3, 4)
    assert reta.contem_ponto(true) is True
    assert reta.contem_ponto(false) is False


def test_mover_reta(reta):
    novo_ponto1 = Point(3, 3)
    novo_ponto2 = Point(4, 4)
    reta.mover(novo_ponto1, novo_ponto2)
    assert reta.get_ponto1().get_x() == 3
    assert reta.get_ponto1().get_y() == 3
    assert reta.get_ponto2().get_x() == 4
    assert reta.get_ponto2().get_y() == 4


def test_str_reta(reta):
    message = "Segmento de Reta(Ponto(1, 1), Ponto(4, 4))"
    assert str(reta) == message


def test_criar_reta():
    user_input = ["0 0", "2 2"]

    with patch("builtins.input", side_effect=user_input):
        reta = LineSegment.criar_segmento_de_reta()

    assert reta.get_ponto1().get_x() == 0
    assert reta.get_ponto1().get_y() == 0
    assert reta.get_ponto2().get_x() == 2
    assert reta.get_ponto2().get_y() == 2
