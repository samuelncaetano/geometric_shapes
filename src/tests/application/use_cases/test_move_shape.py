from unittest.mock import MagicMock
import pytest
from src.package import MoveShape
from src.package import LineSegment


def test_execute_move_line_segment():
    mock_repository = MagicMock()
    move_shape = MoveShape(mock_repository)
    mock_line_segment = MagicMock(spec=LineSegment)
    mock_repository.get.return_value = mock_line_segment
    move_shape.execute(0, (1, 1), (2, 2))
    mock_line_segment.mover.assert_called_once_with((1, 1), (2, 2))


def test_execute_move_other_shape():
    mock_repository = MagicMock()
    move_shape = MoveShape(mock_repository)
    mock_other_shape = MagicMock()
    mock_repository.get.return_value = mock_other_shape
    move_shape.execute(0, (1, 1))
    mock_other_shape.mover.assert_called_once_with((1, 1))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
