class CreateShape:
    def __init__(self, repository, factory):
        self.repository = repository
        self.factory = factory

    def execute(self, tipo_forma):
        forma = self.factory.criar_forma(tipo_forma)
        self.repository.add(forma)
