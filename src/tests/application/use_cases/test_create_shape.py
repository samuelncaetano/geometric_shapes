from unittest.mock import MagicMock
import pytest
from src.package import CreateShape, InMemoryRepository


def test_execute():
    mock_repository = InMemoryRepository()
    mock_factory = MagicMock()
    mock_factory.criar_forma.return_value = "ponto"
    create_shape = CreateShape(mock_repository, mock_factory)
    mock_repository.add = MagicMock()
    mock_point = MagicMock()
    mock_point.__class__.__name__ = "Point"
    mock_factory.criar_forma = MagicMock(return_value=mock_point)
    create_shape.execute("ponto")
    mock_repository.add.assert_called_once_with(mock_point)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
