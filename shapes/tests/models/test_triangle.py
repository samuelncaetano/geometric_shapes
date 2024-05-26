# pylint: disable = E0110, E0401, W0613
from unittest.mock import patch
import pytest
from shapes.package import Triangle, Point, LineSegment


@pytest.fixture
def triangulo():
    return Triangle(Point(0, 0), Point(3, 0), Point(0, 4))


def test_instanciar_triangulo_valido(triangulo):
    try:
        assert isinstance(triangulo, Triangle)
    except ValueError:
        pytest.fail("Os pontos fornecidos não formam um triângulo válido.")


def test_instanciar_triangulo_invalido():
    ponto1 = Point(0, 0)
    ponto2 = Point(1, 1)
    ponto3 = Point(2, 2)
    with pytest.raises(ValueError):
        Triangle(ponto1, ponto2, ponto3)


def test_obter_coordenadas_triangulo(triangulo):
    assert triangulo.calcular_centro().get_x() == 1
    assert triangulo.calcular_centro().get_y() == 1.3
    assert triangulo.get_ponto1().get_x() == 0
    assert triangulo.get_ponto1().get_y() == 0
    assert triangulo.get_ponto2().get_x() == 3
    assert triangulo.get_ponto2().get_y() == 0
    assert triangulo.get_ponto3().get_x() == 0
    assert triangulo.get_ponto3().get_y() == 4


def test_calcular_area_triangulo(triangulo):
    ponto1 = Point(0, 0)
    ponto2 = Point(3, 0)
    ponto3 = Point(0, 4)
    x1, y1 = ponto1.get_x(), ponto1.get_y()
    x2, y2 = ponto2.get_x(), ponto2.get_y()
    x3, y3 = ponto3.get_x(), ponto3.get_y()
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    assert triangulo.calcular_area() == area


def test_calcular_perimetro_triangulo(triangulo):
    a = LineSegment(Point(0, 0), Point(3, 0)).calcular_comprimento()
    b = LineSegment(Point(3, 0), Point(0, 4)).calcular_comprimento()
    c = LineSegment(Point(0, 4), Point(0, 0)).calcular_comprimento()
    perimetro = a + b + c
    assert triangulo.calcular_perimetro() == perimetro


def test_distancia_origem_triangulo(triangulo):
    origem = min(
        Point(0, 0).distancia_origem(),
        Point(3, 0).distancia_origem(),
        Point(0, 4).distancia_origem(),
    )
    assert triangulo.distancia_origem() == origem


def test_distancia_pontos_triangulo(triangulo):
    ponto = Point(1, 1)
    distancias = [
        Point(0, 0).distancia_pontos(ponto),
        Point(3, 0).distancia_pontos(ponto),
        Point(0, 4).distancia_pontos(ponto),
    ]
    assert triangulo.distancia_pontos(ponto) == min(distancias)


def test_contem_ponto_triangulo(triangulo):
    true = Point(1, 1.5)
    false = Point(2, 2)
    assert triangulo.contem_ponto(true) is True
    assert triangulo.contem_ponto(false) is False


def test_mover_triangulo(triangulo):
    novo_centro = Point(4, 4)
    novo_ponto1 = Point(3.0, 2.7)
    novo_ponto2 = Point(6.0, 2.7)
    novo_ponto3 = Point(3.0, 6.7)
    triangulo.mover(novo_centro)
    assert triangulo.calcular_centro().get_x() == 4
    assert triangulo.calcular_centro().get_y() == 4
    assert triangulo.contem_ponto(novo_ponto1) is True
    assert triangulo.contem_ponto(novo_ponto2) is True
    assert triangulo.contem_ponto(novo_ponto3) is True


def test_str_triangulo(triangulo):
    message = "Triângulo(Centro: Ponto(1.0, 1.3), Ponto1: Ponto(0, 0), Ponto2: Ponto(3, 0), Ponto3: Ponto(0, 4))"
    assert str(triangulo) == message


def test_criar_triangulo_valido():
    user_input = ["0 0", "3 0", "0 4"]
    with patch("builtins.input", side_effect=user_input):
        triangulo = Triangle.criar_triangulo()

    assert triangulo.calcular_centro().get_x() == 1
    assert triangulo.calcular_centro().get_y() == 1.3
    assert triangulo.get_ponto1().get_x() == 0
    assert triangulo.get_ponto1().get_y() == 0
    assert triangulo.get_ponto2().get_x() == 3
    assert triangulo.get_ponto2().get_y() == 0
    assert triangulo.get_ponto3().get_x() == 0
    assert triangulo.get_ponto3().get_y() == 4


@patch("builtins.input", side_effect=["1 1", "1 2", "1 3"])
def test_criar_triangulo_invalido(mock_input):
    with pytest.raises(ValueError):
        Triangle.criar_triangulo()
