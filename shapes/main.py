from shapes.package import GeometricShapeApp
from shapes.package import InMemoryRepository


if __name__ == "__main__":
    repository = InMemoryRepository()
    app = GeometricShapeApp(repository)
    app.run()
