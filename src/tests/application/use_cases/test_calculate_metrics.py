from unittest.mock import MagicMock
import pytest
from src.package import CalculateMetrics

mock_repository = MagicMock()
mock_forma = MagicMock()
calculate_metrics = CalculateMetrics(mock_repository)


def test_calcular_area():
    mock_forma.calcular_area.return_value = 10
    mock_repository.get.return_value = mock_forma
    area = calculate_metrics.calcular_area(0)
    mock_forma.calcular_area.assert_called_once()
    assert area == 10


def test_calcular_perimetro():
    mock_forma.calcular_perimetro.return_value = 20
    mock_repository.get.return_value = mock_forma
    perimetro = calculate_metrics.calcular_perimetro(0)
    mock_forma.calcular_perimetro.assert_called_once()
    assert perimetro == 20


def test_distancia_origem():
    mock_forma.distancia_origem.return_value = 5
    mock_repository.get.return_value = mock_forma
    distancia = calculate_metrics.distancia_origem(0)
    mock_forma.distancia_origem.assert_called_once()
    assert distancia == 5


def test_distancia_pontos():
    mock_forma.distancia_pontos.return_value = 7
    mock_repository.get.return_value = mock_forma
    distancia = calculate_metrics.distancia_pontos(0, (2, 3))
    mock_forma.distancia_pontos.assert_called_once_with((2, 3))
    assert distancia == 7


def test_contem_ponto():
    mock_forma.contem_ponto.return_value = True
    mock_repository.get.return_value = mock_forma
    contem = calculate_metrics.contem_ponto(0, (4, 5))
    mock_forma.contem_ponto.assert_called_once_with((4, 5))
    assert contem is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
