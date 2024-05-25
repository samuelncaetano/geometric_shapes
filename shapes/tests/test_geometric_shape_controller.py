# pylint: disable = E0110, E0401
from math import pi
from unittest.mock import patch
import pytest
from shapes.package.models import Point, LineSegment, Circle, Rectangle
from shapes.package.controllers import GeometricShapeController
from shapes.package.repository.in_memory_repository import InMemoryRepository


@pytest.fixture
def repository():
    return InMemoryRepository()


@pytest.fixture
def controller(repository):
    return GeometricShapeController(repository)


@pytest.fixture
def ponto():
    return Point(0, 0)


@pytest.fixture
def reta():
    return LineSegment(Point(1, 1), Point(4, 4))


@pytest.fixture
def circulo():
    return Circle(Point(0, 0), 4)


@pytest.fixture
def retangulo():
    return Rectangle(Point(0, 0), 4, 4)


def test_instanciar_controller(controller):
    assert isinstance(controller, GeometricShapeController)


def test_adicionar_forma_geometrica(controller, ponto, repository):
    controller.adicionar_forma_geometrica(ponto)
    assert ponto in repository.list_all()


def test_listar_formas_geometricas_sem_formas(controller, capsys):
    controller.listar_formas_geometricas()
    captured = capsys.readouterr()
    assert captured.out == "Nenhuma forma geométrica cadastrada.\n"


def test_listar_formas_geometricas_com_formas(controller, ponto, capsys):
    controller.adicionar_forma_geometrica(ponto)
    controller.listar_formas_geometricas()
    captured = capsys.readouterr()
    expected_output = "### Formas Geométricas ###\n1. Ponto(0, 0)\n"
    assert captured.out == expected_output


# Usar os métodos das classes no controller
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


# Circle
def test_calcular_area_circulo(controller, circulo):
    area = pi * 4**2
    controller.adicionar_forma_geometrica(circulo)
    assert controller.calcular_area(0) == area


def test_calcular_perimetro_circulo(controller, circulo):
    perimetro = 2 * pi * 4
    controller.adicionar_forma_geometrica(circulo)
    assert controller.calcular_perimetro(0) == perimetro


def test_distancia_origem_circulo(controller, circulo):
    controller.adicionar_forma_geometrica(circulo)
    assert controller.distancia_origem(0) == 0


def test_distancia_pontos_circulo(controller, circulo):
    ponto = Point(1, 1)
    distancia = abs(circulo.get_centro().distancia_pontos(ponto) - circulo.get_raio())
    controller.adicionar_forma_geometrica(circulo)
    assert controller.distancia_pontos(0, ponto) == distancia


def test_contem_ponto_circulo(controller, circulo):
    true = Point(2, 2)
    false = Point(5, 5)
    controller.adicionar_forma_geometrica(circulo)
    assert controller.contem_ponto(0, true) is True
    assert controller.contem_ponto(0, false) is False


def test_mover_circulo(controller, circulo):
    controller.adicionar_forma_geometrica(circulo)
    controller.mover_formas(0, Point(4, 4))
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_centro().get_x() == 4
    assert item.get_centro().get_y() == 4


# Circle
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


# Adicionar formas no controller
def test_adicionar_ponto(controller):
    user_input = ["0 0"]
    with patch("builtins.input", side_effect=user_input):
        controller.adicionar_ponto()
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_x() == 0
    assert item.get_y() == 0


def test_adicionar_reta(controller):
    user_input = ["0 0", "2 2"]
    with patch("builtins.input", side_effect=user_input):
        controller.adicionar_segmento_de_reta()
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_ponto1().get_x() == 0
    assert item.get_ponto1().get_y() == 0
    assert item.get_ponto2().get_x() == 2
    assert item.get_ponto2().get_y() == 2


def test_adicionar_circulo(controller):
    user_input = ["0 0", "4"]
    with patch("builtins.input", side_effect=user_input):
        controller.adicionar_circulo()
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_centro().get_x() == 0
    assert item.get_centro().get_y() == 0
    assert item.get_raio() == 4


def test_adicionar_retangulo(controller):
    user_input = ["0 0", "4", "4"]
    with patch("builtins.input", side_effect=user_input):
        controller.adicionar_retangulo()
    item = controller._GeometricShapeController__repository.get(0)
    assert item.get_centro().get_x() == 0
    assert item.get_centro().get_y() == 0
    assert item.get_largura() == 4
    assert item.get_altura() == 4
