from pathlib import Path
from src.package import GeometricShapeApp, InMemoryRepository, ShapeFactory, JsonRepository


if __name__ == "__main__":
    repository = InMemoryRepository()
    file_path = Path(__file__).parent / "shapes.json"
    repository = JsonRepository(file_path)
    factory = ShapeFactory()
    app = GeometricShapeApp(repository, factory)
    app.run()
