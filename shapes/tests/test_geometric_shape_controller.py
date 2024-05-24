# pylint: disable = E0110, E0401
from unittest.mock import patch
import pytest
from shapes.package import GeometricShapeController
from shapes.package import Point


@pytest.fixture
def controller():
    return GeometricShapeController()


@pytest.fixture
def ponto():
    return Point(0, 0)


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
def test_calcular_area_ponto(controller, ponto):
    # POINT
    controller.adicionar_forma_geometrica(ponto)
    assert controller.calcular_area(0) == 0


def test_calcular_perimetro_ponto(controller, ponto):
    # POINT
    controller.adicionar_forma_geometrica(ponto)
    assert controller.calcular_perimetro(0) == 0


def test_distancia_origem_ponto(controller, ponto):
    # POINT
    controller.adicionar_forma_geometrica(ponto)
    assert controller.distancia_origem(0) == 0


def test_distancia_pontos_ponto(controller, ponto):
    # POINT
    controller.adicionar_forma_geometrica(ponto)
    origem = Point(0, 0)
    assert controller.distancia_pontos(0, origem) == 0


def test_contem_ponto_ponto(controller, ponto):
    # POINT
    controller.adicionar_forma_geometrica(ponto)
    origem = Point(0, 0)
    assert controller.contem_ponto(0, origem) is True


def test_mover_ponto(controller, ponto):
    # POINT
    controller.adicionar_forma_geometrica(ponto)
    controller.mover_formas(0, Point(2, 2))
    assert controller._GeometricShapeController__geometric_shapes[0].get_x() == 2
    assert controller._GeometricShapeController__geometric_shapes[0].get_y() == 2


# Adicionar formas no controller
def test_adicionar_ponto(controller):
    with patch("builtins.input", side_effect=["0 0"]):
        controller.adicionar_ponto()
    assert len(controller._GeometricShapeController__geometric_shapes) == 1
    assert controller._GeometricShapeController__geometric_shapes[0].get_x() == 0
    assert controller._GeometricShapeController__geometric_shapes[0].get_y() == 0
