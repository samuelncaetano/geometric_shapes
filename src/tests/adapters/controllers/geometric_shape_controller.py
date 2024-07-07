# pylint: disable = W0613
from unittest.mock import patch
import pytest
from pathlib import Path
from src.package import (
    InMemoryRepository,
    JsonRepository,
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
def memory_repository():
    return InMemoryRepository()


@pytest.fixture
def memory_controller(memory_repository):
    return GeometricShapeController(memory_repository)


@pytest.fixture
def temp_json_file(tmpdir):
    file = tmpdir.join("test_shapes.json")
    file.write("[]")
    return Path(file)


@pytest.fixture
def json_repository(temp_json_file):
    return JsonRepository(temp_json_file)


@pytest.fixture
def json_controller(json_repository):
    return GeometricShapeController(json_repository)


class TestMemoryController:
    def test_instanciar_controller(self, memory_controller):
        assert isinstance(memory_controller, GeometricShapeController)

    @patch("builtins.input", return_value=ponto)
    def test_adicionar_ponto(self, mock_input, memory_controller):
        memory_controller.adicionar_ponto()
        assert len(memory_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            memory_controller.listar_formas_geometricas()[0], Point)

    @patch("builtins.input", side_effect=reta)
    def test_adicionar_segmento_de_reta(self, mock_input, memory_controller):
        memory_controller.adicionar_segmento_de_reta()
        assert len(memory_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            memory_controller.listar_formas_geometricas()[0], LineSegment)

    @patch("builtins.input", side_effect=circulo)
    def test_adicionar_circulo(self, mock_input, memory_controller):
        memory_controller.adicionar_circulo()
        assert len(memory_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            memory_controller.listar_formas_geometricas()[0], Circle)

    @patch("builtins.input", side_effect=retangulo)
    def test_adicionar_retangulo(self, mock_input, memory_controller):
        memory_controller.adicionar_retangulo()
        assert len(memory_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            memory_controller.listar_formas_geometricas()[0], Rectangle)

    @patch("builtins.input", side_effect=triangulo)
    def test_adicionar_triangulo(self, mock_input, memory_controller):
        memory_controller.adicionar_triangulo()
        assert len(memory_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            memory_controller.listar_formas_geometricas()[0], Triangle)

    @patch("builtins.input", return_value=ponto)
    def test_calcular_area(self, mock_input, memory_controller):
        memory_controller.adicionar_ponto()
        assert memory_controller.calcular_area(0) == 0

    @patch("builtins.input", side_effect=reta)
    def test_calcular_perimetro(self, mock_input, memory_controller):
        memory_controller.adicionar_ponto()
        assert memory_controller.calcular_perimetro(0) == 0

    @patch("builtins.input", return_value=ponto_zero)
    def test_distancia_origem(self, mock_input, memory_controller):
        memory_controller.adicionar_ponto()
        assert memory_controller.distancia_origem(0) == 0

    @patch("builtins.input", return_value=ponto_zero)
    def test_distancia_pontos(self, mock_input, memory_controller):
        memory_controller.adicionar_ponto()
        assert memory_controller.distancia_pontos(0, Point(3, 4)) == 5

    @patch("builtins.input", return_value=ponto_zero)
    def test_contem_ponto(self, mock_input, memory_controller):
        memory_controller.adicionar_ponto()
        assert memory_controller.contem_ponto(0, Point(0, 0)) is True

    @patch("builtins.input", return_value=ponto_zero)
    def test_mover_forma(self, mock_input, memory_controller):
        memory_controller.adicionar_ponto()
        memory_controller.mover_forma(0, Point(1, 1))
        forma = memory_controller.listar_formas_geometricas()[0]
        assert forma.get_x() == 1 and forma.get_y() == 1

    @patch("builtins.input", side_effect=reta)
    def test_mover_segmento_de_reta(self, mock_input, memory_controller):
        memory_controller.adicionar_segmento_de_reta()
        memory_controller.mover_segmento_de_reta(0, Point(1, 1), Point(4, 4))
        forma = memory_controller.listar_formas_geometricas()[0]
        assert forma.get_ponto1().get_x() == 1 and forma.get_ponto1().get_y() == 1
        assert forma.get_ponto2().get_x() == 4 and forma.get_ponto2().get_y() == 4


class TestJsonController:
    def test_instanciar_controller(self, json_controller):
        assert isinstance(json_controller, GeometricShapeController)

    @patch("builtins.input", return_value=ponto)
    def test_adicionar_ponto(self, mock_input, json_controller):
        json_controller.adicionar_ponto()
        assert len(json_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            json_controller.listar_formas_geometricas()[0], Point)

    @patch("builtins.input", side_effect=reta)
    def test_adicionar_segmento_de_reta(self, mock_input, json_controller):
        json_controller.adicionar_segmento_de_reta()
        assert len(json_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            json_controller.listar_formas_geometricas()[0], LineSegment)

    @patch("builtins.input", side_effect=circulo)
    def test_adicionar_circulo(self, mock_input, json_controller):
        json_controller.adicionar_circulo()
        assert len(json_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            json_controller.listar_formas_geometricas()[0], Circle)

    @patch("builtins.input", side_effect=retangulo)
    def test_adicionar_retangulo(self, mock_input, json_controller):
        json_controller.adicionar_retangulo()
        assert len(json_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            json_controller.listar_formas_geometricas()[0], Rectangle)

    @patch("builtins.input", side_effect=triangulo)
    def test_adicionar_triangulo(self, mock_input, json_controller):
        json_controller.adicionar_triangulo()
        assert len(json_controller.listar_formas_geometricas()) == 1
        assert isinstance(
            json_controller.listar_formas_geometricas()[0], Triangle)

    @patch("builtins.input", return_value=ponto)
    def test_calcular_area(self, mock_input, json_controller):
        json_controller.adicionar_ponto()
        assert json_controller.calcular_area(0) == 0

    @patch("builtins.input", side_effect=reta)
    def test_calcular_perimetro(self, mock_input, json_controller):
        json_controller.adicionar_ponto()
        assert json_controller.calcular_perimetro(0) == 0

    @patch("builtins.input", return_value=ponto_zero)
    def test_distancia_origem(self, mock_input, json_controller):
        json_controller.adicionar_ponto()
        assert json_controller.distancia_origem(0) == 0

    @patch("builtins.input", return_value=ponto_zero)
    def test_distancia_pontos(self, mock_input, json_controller):
        json_controller.adicionar_ponto()
        assert json_controller.distancia_pontos(0, Point(3, 4)) == 5

    @patch("builtins.input", return_value=ponto_zero)
    def test_contem_ponto(self, mock_input, json_controller):
        json_controller.adicionar_ponto()
        assert json_controller.contem_ponto(0, Point(0, 0)) is True

    @patch("builtins.input", return_value=ponto_zero)
    def test_mover_forma(self, mock_input, json_controller):
        json_controller.adicionar_ponto()
        json_controller.mover_forma(0, Point(1, 1))
        forma = json_controller.listar_formas_geometricas()[0]
        assert forma.get_x() == 1 and forma.get_y() == 1

    @patch("builtins.input", side_effect=reta)
    def test_mover_segmento_de_reta(self, mock_input, json_controller):
        json_controller.adicionar_segmento_de_reta()
        json_controller.mover_segmento_de_reta(0, Point(1, 1), Point(4, 4))
        forma = json_controller.listar_formas_geometricas()[0]
        assert forma.get_ponto1().get_x() == 1 and forma.get_ponto1().get_y() == 1
        assert forma.get_ponto2().get_x() == 4 and forma.get_ponto2().get_y() == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
