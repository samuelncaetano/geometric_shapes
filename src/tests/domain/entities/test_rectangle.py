# pylint: disable = E0110, E0401
from unittest.mock import patch
import pytest
from src.package import Rectangle, Point


@pytest.fixture
def retangulo():
    return Rectangle(Point(2, 2), 4, 4)


def test_instanciar_retangulo(retangulo):
    assert isinstance(retangulo, Rectangle)


def test_criar_retangulo_com_ponto_invalido():
    with pytest.raises(ValueError):
        Rectangle(Point(-1, -1), 4, 4)


def test_criar_retangulo_com_largura_invalido():
    with pytest.raises(ValueError):
        return Rectangle(Point(2, 2), -4, 4)


def test_criar_retangulo_com_altura_invalido():
    with pytest.raises(ValueError):
        return Rectangle(Point(2, 2), 4, -4)


def test_obter_coordenadas_retangulo(retangulo):
    assert retangulo.get_centro().get_x() == 2
    assert retangulo.get_centro().get_y() == 2
    assert retangulo.get_largura() == 4
    assert retangulo.get_altura() == 4


def test_calcular_area_retangulo(retangulo):
    area = 4 * 4
    assert retangulo.calcular_area() == area


def test_calcular_perimetro_retangulo(retangulo):
    perimetro = 2 * (4 + 4)
    assert retangulo.calcular_perimetro() == perimetro


def test_distancia_origem_retangulo(retangulo):
    ponto_superior_esquerdo = Point(0, 4)
    ponto_inferior_direito = Point(4, 0)
    origem = min(
        ponto_inferior_direito.distancia_origem(),
        ponto_superior_esquerdo.distancia_origem(),
    )
    assert retangulo.distancia_origem() == origem


def test_distancia_pontos_retangulo(retangulo):
    ponto = Point(1, 1)
    ponto_superior_esquerdo = Point(0, 4)
    ponto_inferior_direito = Point(4, 0)
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
    assert retangulo.distancia_pontos(ponto) == min(distancias)


def test_contem_ponto_retangulo(retangulo):
    true = Point(2, 2)
    false = Point(5, 5)
    assert retangulo.contem_ponto(true) is True
    assert retangulo.contem_ponto(false) is False


def test_mover_retangulo(retangulo):
    novo_ponto = Point(4, 4)
    retangulo.mover(novo_ponto)
    assert retangulo.get_centro().get_x() == 4
    assert retangulo.get_centro().get_y() == 4


def test_str_retangulo(retangulo):
    message = "Retângulo(Centro: Ponto(2, 2), Largura: 4, Altura: 4)"
    assert str(retangulo) == message


def test_criar_retangulo():
    user_input = ["2 2", "4", "4"]

    with patch("builtins.input", side_effect=user_input):
        retangulo = Rectangle.criar_retangulo()

    assert retangulo.get_centro().get_x() == 2
    assert retangulo.get_centro().get_y() == 2
    assert retangulo.get_largura() == 4
    assert retangulo.get_altura() == 4
