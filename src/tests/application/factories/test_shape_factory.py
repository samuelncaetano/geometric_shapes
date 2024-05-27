from unittest.mock import patch
import pytest
from src.package import Point, LineSegment, Circle, Rectangle, Triangle, ShapeFactory

ponto = "3.0 4.0"
reta = ["1 2", "3 4"]
circulo = ["1 2", "3"]
retangulo = ["0 0", "4", "4"]
triangulo = ["0 0", "3 0", "0 4"]


class TestShapeFactory:
    @patch("builtins.input", return_value=ponto)
    def test_criar_ponto(self, mock_input):
        ponto = ShapeFactory.criar_forma("ponto")
        assert isinstance(ponto, Point)

    @patch("builtins.input", side_effect=reta)
    def test_criar_segmento_de_reta(self, mock_input):
        segmento = ShapeFactory.criar_forma("segmento_de_reta")
        assert isinstance(segmento, LineSegment)

    @patch("builtins.input", side_effect=circulo)
    def test_criar_circulo(self, mock_input):
        circulo = ShapeFactory.criar_forma("circulo")
        assert isinstance(circulo, Circle)

    @patch("builtins.input", side_effect=retangulo)
    def test_criar_retangulo(self, mock_input):
        retangulo = ShapeFactory.criar_forma("retangulo")
        assert isinstance(retangulo, Rectangle)

    @patch("builtins.input", side_effect=triangulo)
    def test_criar_triangulo(self, mock_input):
        triangulo = ShapeFactory.criar_forma("triangulo")
        assert isinstance(triangulo, Triangle)

    def test_tipo_forma_desconhecido(self):
        with pytest.raises(ValueError):
            ShapeFactory.criar_forma("forma_desconhecida")
