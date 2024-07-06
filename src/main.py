from pathlib import Path
from src.package import GeometricShapeApp


if __name__ == "__main__":
    file_path = Path(__file__).parent / "shapes.json"
    repository = GeometricShapeApp.selecionar_repositorio(file_path)
    app = GeometricShapeApp(repository)
    app.run()
