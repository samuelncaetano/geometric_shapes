# pylint: disable = W0613
from unittest.mock import patch
import pytest
from src.package import (
    InMemoryRepository,
    ShapeFactory,
    Point,
    LineSegment,
    Circle,
    Rectangle,
    Triangle,
    GeometricShapeController,
)

ponto = "3.0 4.0"
ponto_zero = "0.0 0.0"
reta = ["1 2", "3 4"]
circulo = ["1 2", "3"]
retangulo = ["2 2", "4", "4"]
triangulo = ["0 0", "3 0", "0 4"]


@pytest.fixture
def repository():
    return InMemoryRepository()


@pytest.fixture
def factory():
    return ShapeFactory()


@pytest.fixture
def controller(repository, factory):
    return GeometricShapeController(repository, factory)


def test_instanciar_controller(controller):
    assert isinstance(controller, GeometricShapeController)


@patch("builtins.input", return_value=ponto)
def test_adicionar_ponto(mock_input, controller):
    controller.adicionar_ponto()
    assert len(controller.listar_formas_geometricas()) == 1
    assert isinstance(controller.listar_formas_geometricas()[0], Point)


@patch("builtins.input", side_effect=reta)
def test_adicionar_segmento_de_reta(mock_input, controller):
    controller.adicionar_segmento_de_reta()
    assert len(controller.listar_formas_geometricas()) == 1
    assert isinstance(controller.listar_formas_geometricas()[0], LineSegment)


@patch("builtins.input", side_effect=circulo)
def test_adicionar_circulo(mock_input, controller):
    controller.adicionar_circulo()
    assert len(controller.listar_formas_geometricas()) == 1
    assert isinstance(controller.listar_formas_geometricas()[0], Circle)


@patch("builtins.input", side_effect=retangulo)
def test_adicionar_retangulo(mock_input, controller):
    controller.adicionar_retangulo()
    assert len(controller.listar_formas_geometricas()) == 1
    assert isinstance(controller.listar_formas_geometricas()[0], Rectangle)


@patch("builtins.input", side_effect=triangulo)
def test_adicionar_triangulo(mock_input, controller):
    controller.adicionar_triangulo()
    assert len(controller.listar_formas_geometricas()) == 1
    assert isinstance(controller.listar_formas_geometricas()[0], Triangle)


@patch("builtins.input", return_value=ponto)
def test_calcular_area(mock_input, controller):
    controller.adicionar_ponto()
    assert controller.calcular_area(0) == 0


@patch("builtins.input", side_effect=reta)
def test_calcular_perimetro(mock_input, controller):
    controller.adicionar_ponto()
    assert controller.calcular_perimetro(0) == 0


@patch("builtins.input", return_value=ponto_zero)
def test_distancia_origem(mock_input, controller):
    controller.adicionar_ponto()
    assert controller.distancia_origem(0) == 0


@patch("builtins.input", return_value=ponto_zero)
def test_distancia_pontos(mock_input, controller):
    controller.adicionar_ponto()
    assert controller.distancia_pontos(0, Point(3, 4)) == 5


@patch("builtins.input", return_value=ponto_zero)
def test_contem_ponto(mock_input, controller):
    controller.adicionar_ponto()
    assert controller.contem_ponto(0, Point(0, 0)) is True


@patch("builtins.input", return_value=ponto_zero)
def test_mover_forma(mock_input, controller):
    controller.adicionar_ponto()
    controller.mover_forma(0, Point(1, 1))
    forma = controller.listar_formas_geometricas()[0]
    assert forma.get_x() == 1 and forma.get_y() == 1


@patch("builtins.input", side_effect=reta)
def test_mover_segmento_de_reta(mock_input, controller):
    controller.adicionar_segmento_de_reta()
    controller.mover_segmento_de_reta(0, Point(1, 1), Point(4, 4))
    forma = controller.listar_formas_geometricas()[0]
    assert forma.get_ponto1().get_x() == 1 and forma.get_ponto1().get_y() == 1
    assert forma.get_ponto2().get_x() == 4 and forma.get_ponto2().get_y() == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
