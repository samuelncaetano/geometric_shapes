from unittest.mock import MagicMock
from src.package import CreateShape, InMemoryRepository

class TestCreateShape:
  def test_execute(self):
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
