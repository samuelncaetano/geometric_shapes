# pylint: disable = E0110, E0401
from math import pi
from unittest.mock import patch
import pytest
from src.package import Circle, Point


@pytest.fixture
def circulo():
    return Circle(Point(0, 0), 4)


def test_instanciar_circulo(circulo):
    assert isinstance(circulo, Circle)


def test_criar_circulo_com_ponto_invalido():
    with pytest.raises(ValueError):
        Circle(Point(-1, -1), 4)


def test_criar_circulo_com_raio_invalido():
    with pytest.raises(ValueError):
        Circle(Point(0, 0), -4)


def test_obter_coordenadas_circulo(circulo):
    assert circulo.get_centro().get_x() == 0
    assert circulo.get_centro().get_y() == 0
    assert circulo.get_raio() == 4


def test_calcular_area_circulo(circulo):
    area = pi * 4**2
    assert circulo.calcular_area() == area


def test_calcular_perimetro_circulo(circulo):
    perimetro = 2 * pi * 4
    assert circulo.calcular_perimetro() == perimetro


def test_distancia_origem_circulo(circulo):
    assert circulo.distancia_origem() == 0


def test_distancia_pontos_circulo(circulo):
    ponto = Point(1, 1)
    distancia = abs(circulo.get_centro().distancia_pontos(ponto) - circulo.get_raio())
    assert circulo.distancia_pontos(ponto) == distancia


def test_contem_ponto_circulo(circulo):
    true = Point(2, 2)
    false = Point(5, 5)
    assert circulo.contem_ponto(true) is True
    assert circulo.contem_ponto(false) is False


def test_mover_circulo(circulo):
    novo_ponto = Point(4, 4)
    circulo.mover(novo_ponto)
    assert circulo.get_centro().get_x() == 4
    assert circulo.get_centro().get_y() == 4


def test_str_circulo(circulo):
    message = "Círculo(Centro: Ponto(0, 0), Raio: 4)"
    assert str(circulo) == message


def test_criar_circulo():
    user_input = ["0 0", "4"]

    with patch("builtins.input", side_effect=user_input):
        circulo = Circle.criar_circulo()

    assert circulo.get_centro().get_x() == 0
    assert circulo.get_centro().get_y() == 0
    assert circulo.get_raio() == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
