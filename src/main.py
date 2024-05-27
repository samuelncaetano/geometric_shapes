from src.package import GeometricShapeApp, InMemoryRepository


if __name__ == "__main__":
    repository = InMemoryRepository()
    app = GeometricShapeApp(repository)
    app.run()
