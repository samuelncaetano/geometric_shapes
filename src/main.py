from src.package import GeometricShapeApp, InMemoryRepository, ShapeFactory


if __name__ == "__main__":
    repository = InMemoryRepository()
    factory = ShapeFactory()
    app = GeometricShapeApp(repository, factory)
    app.run()
