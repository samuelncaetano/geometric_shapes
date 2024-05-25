# pylint: disable = E0110, E0401
from unittest.mock import patch
import pytest
from shapes.package import GeometricShapeController
from shapes.package import Point, LineSegment


@pytest.fixture
def controller():
    return GeometricShapeController()


@pytest.fixture
def ponto():
    return Point(0, 0)


@pytest.fixture
def reta():
    return LineSegment(Point(1, 1), Point(4, 4))


def test_instanciar_controller(controller):
    assert isinstance(controller, GeometricShapeController)


def test_adicionar_forma_geometrica(controller, ponto):
    controller.adicionar_forma_geometrica(ponto)
    assert ponto in controller._GeometricShapeController__geometric_shapes


def test_listar_formas_geometricas_sem_formas(controller, capsys):
    controller.listar_formas_geometricas()
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Nenhuma forma geométrica cadastrada.\n### Formas Geométricas ###\n"
    )


def test_listar_formas_geometricas_com_formas(controller, ponto, capsys):
    controller.adicionar_forma_geometrica(ponto)
    controller.listar_formas_geometricas()
    captured = capsys.readouterr()
    expected_output = "### Formas Geométricas ###\n1. Ponto(0, 0)\n"
    assert captured.out == expected_output


# Usar os métodos das classes no controller
# POINT
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
    assert controller._GeometricShapeController__geometric_shapes[0].get_x() == 2
    assert controller._GeometricShapeController__geometric_shapes[0].get_y() == 2


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
    assert (
        controller._GeometricShapeController__geometric_shapes[0].get_ponto1().get_x()
        == 2
    )
    assert (
        controller._GeometricShapeController__geometric_shapes[0].get_ponto1().get_y()
        == 2
    )
    assert (
        controller._GeometricShapeController__geometric_shapes[0].get_ponto2().get_x()
        == 5
    )
    assert (
        controller._GeometricShapeController__geometric_shapes[0].get_ponto2().get_y()
        == 5
    )


# Adicionar formas no controller
def test_adicionar_ponto(controller):
    user_input = ["0 0"]
    with patch("builtins.input", side_effect=user_input):
        controller.adicionar_ponto()
    assert len(controller._GeometricShapeController__geometric_shapes) == 1
    assert controller._GeometricShapeController__geometric_shapes[0].get_x() == 0
    assert controller._GeometricShapeController__geometric_shapes[0].get_y() == 0


def test_adicionar_reta(controller):
    user_input = ["0 0", "2 2"]
    with patch("builtins.input", side_effect=user_input):
        controller.adicionar_segmento_de_reta()
    assert len(controller._GeometricShapeController__geometric_shapes) == 1
    assert (
        controller._GeometricShapeController__geometric_shapes[0].get_ponto1().get_x()
        == 0
    )
    assert (
        controller._GeometricShapeController__geometric_shapes[0].get_ponto1().get_y()
        == 0
    )
    assert (
        controller._GeometricShapeController__geometric_shapes[0].get_ponto2().get_x()
        == 2
    )
    assert (
        controller._GeometricShapeController__geometric_shapes[0].get_ponto2().get_y()
        == 2
    )
