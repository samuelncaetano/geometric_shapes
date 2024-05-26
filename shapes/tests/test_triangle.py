# pylint: disable = E0110, E0401
from unittest.mock import patch
import pytest
from shapes.package import Triangle, Point, LineSegment


@pytest.fixture
def triangulo():
    return Triangle(Point(0, 0), Point(0, 2), Point(2, -1.5), Point(-2, -1.5))


def test_instanciar_triangulo(triangulo):
    assert isinstance(triangulo, Triangle)


def test_obter_coordenadas_triangulo(triangulo):
    assert triangulo.get_centro().get_x() == 0
    assert triangulo.get_centro().get_y() == 0
    assert triangulo.get_ponto1().get_x() == 0
    assert triangulo.get_ponto1().get_y() == 2
    assert triangulo.get_ponto2().get_x() == 2
    assert triangulo.get_ponto2().get_y() == -1.5
    assert triangulo.get_ponto3().get_x() == -2
    assert triangulo.get_ponto3().get_y() == -1.5


def test_calcular_area_triangulo(triangulo):
    ponto1 = Point(0, 2)
    ponto2 = Point(2, -1.5)
    ponto3 = Point(-2, -1.5)
    x1, y1 = ponto1.get_x(), ponto1.get_y()
    x2, y2 = ponto2.get_x(), ponto2.get_y()
    x3, y3 = ponto3.get_x(), ponto3.get_y()
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    assert triangulo.calcular_area() == area


def test_calcular_perimetro_triangulo(triangulo):
    a = LineSegment(Point(0, 2), Point(2, -1.5)).calcular_comprimento()
    b = LineSegment(Point(2, -1.5), Point(-2, -1.5)).calcular_comprimento()
    c = LineSegment(Point(-2, -1.5), Point(0, 2)).calcular_comprimento()
    perimetro = a + b + c
    assert triangulo.calcular_perimetro() == perimetro


def test_distancia_origem_triangulo(triangulo):
    origem = min(
        Point(0, 2).distancia_origem(),
        Point(2, -1.5).distancia_origem(),
        Point(-2, -1.5).distancia_origem(),
    )
    assert triangulo.distancia_origem() == origem


def test_distancia_pontos_triangulo(triangulo):
    ponto = Point(1, 1)
    distancias = [
        Point(0, 2).distancia_pontos(ponto),
        Point(2, -1.5).distancia_pontos(ponto),
        Point(-2, -1.5).distancia_pontos(ponto),
    ]
    assert triangulo.distancia_pontos(ponto) == min(distancias)


def test_contem_ponto_triangulo(triangulo):
    true = Point(-0.5, -0.5)
    false = Point(2, 2)
    assert triangulo.contem_ponto(true) is True
    assert triangulo.contem_ponto(false) is False


def test_mover_triangulo(triangulo):
    novo_centro = Point(4, 4)
    novo_ponto1 = Point(4, 6)
    novo_ponto2 = Point(6, 2.5)
    novo_ponto3 = Point(2, 2.5)
    triangulo.mover(novo_centro)
    assert triangulo.get_centro().get_x() == 4
    assert triangulo.get_centro().get_y() == 4
    assert triangulo.contem_ponto(novo_ponto1) is True
    assert triangulo.contem_ponto(novo_ponto2) is True
    assert triangulo.contem_ponto(novo_ponto3) is True


def test_str_triangulo(triangulo):
    message = "Triângulo(Centro: Ponto(0, 0), Ponto1: Ponto(0, 2), Ponto2: Ponto(2, -1.5), Ponto3: Ponto(-2, -1.5))"
    assert str(triangulo) == message


def test_criar_triangulo():
    user_input = ["0 0", "0 2", "2 -1.5", "-2 -1.5"]
    with patch("builtins.input", side_effect=user_input):
        triangulo = Triangle.criar_triangulo()

    assert triangulo.get_centro().get_x() == 0
    assert triangulo.get_centro().get_y() == 0
    assert triangulo.get_ponto1().get_x() == 0
    assert triangulo.get_ponto1().get_y() == 2
    assert triangulo.get_ponto2().get_x() == 2
    assert triangulo.get_ponto2().get_y() == -1.5
    assert triangulo.get_ponto3().get_x() == -2
    assert triangulo.get_ponto3().get_y() == -1.5
