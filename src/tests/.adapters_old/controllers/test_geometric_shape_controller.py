# pylint: disable = E0110, E0401, R0801, R0913, E0102
from unittest.mock import patch
import pytest
from src.package import (
    Point,
    LineSegment,
    Circle,
    Rectangle,
    Triangle,
    GeometricShapeController,
    InMemoryRepository,
)


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


@pytest.fixture
def triangulo():
    return Triangle(Point(0, 0), Point(0, 2), Point(3, 0))


def test_instanciar_controller(controller):
    assert isinstance(controller, GeometricShapeController)


def test_adicionar_forma_geometrica(
    controller, ponto, reta, circulo, retangulo, triangulo, repository
):
    controller.adicionar_forma_geometrica(ponto)
    controller.adicionar_forma_geometrica(reta)
    controller.adicionar_forma_geometrica(circulo)
    controller.adicionar_forma_geometrica(retangulo)
    controller.adicionar_forma_geometrica(triangulo)
    assert [ponto, reta, circulo, retangulo, triangulo] == repository.list_all()
    assert ponto == repository.get(0)
    assert reta == repository.get(1)
    assert circulo == repository.get(2)
    assert retangulo == repository.get(3)
    assert triangulo == repository.get(4)


def test_listar_formas_geometricas_sem_formas(controller, capsys):
    controller.listar_formas_geometricas()
    captured = capsys.readouterr()
    assert captured.out == "Nenhuma forma geométrica cadastrada.\n"


def test_listar_formas_geometricas_com_uma_forma(controller, ponto, capsys):
    controller.adicionar_forma_geometrica(ponto)
    controller.listar_formas_geometricas()
    captured = capsys.readouterr()
    expected_output = "### Formas Geométricas ###\n1. Ponto(0, 0)\n"
    assert captured.out == expected_output


def test_listar_formas_geometricas_com_formas(
    controller, ponto, reta, circulo, retangulo, triangulo, capsys
):
    controller.adicionar_forma_geometrica(ponto)
    controller.adicionar_forma_geometrica(reta)
    controller.adicionar_forma_geometrica(circulo)
    controller.adicionar_forma_geometrica(retangulo)
    controller.adicionar_forma_geometrica(triangulo)
    controller.listar_formas_geometricas()
    captured = capsys.readouterr()
    expected_output = (
        "### Formas Geométricas ###\n"
        "1. Ponto(0, 0)\n"
        "2. Segmento de Reta(Ponto(1, 1), Ponto(4, 4))\n"
        "3. Círculo(Centro: Ponto(0, 0), Raio: 4)\n"
        "4. Retângulo(Centro: Ponto(0, 0), Largura: 4, Altura: 4)\n"
        "5. Triângulo(Centro: Ponto(1.0, 0.7), Ponto1: Ponto(0, 0), Ponto2: Ponto(0, 2), Ponto3: Ponto(3, 0))\n"
    )
    assert captured.out == expected_output


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


def test_adicionar_triangulo(controller):
    user_input = ["0 0", "3 0", "0 4"]
    with patch("builtins.input", side_effect=user_input):
        controller.adicionar_triangulo()
    item = controller._GeometricShapeController__repository.get(0)
    assert item.calcular_centro().get_x() == 1
    assert item.calcular_centro().get_y() == 1.3
    assert item.get_ponto1().get_x() == 0
    assert item.get_ponto1().get_y() == 0
    assert item.get_ponto2().get_x() == 3
    assert item.get_ponto2().get_y() == 0
    assert item.get_ponto3().get_x() == 0
    assert item.get_ponto3().get_y() == 4
