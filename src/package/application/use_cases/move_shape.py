from src.package.domain import IRepository, LineSegment


class MoveShape:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, index, novo_ponto, novo_ponto2=None):
        forma = self.repository.get(index)
        if forma is None:
            raise ValueError("Forma geométrica não encontrada.")

        if isinstance(forma, LineSegment) and novo_ponto2 is not None:
            forma.mover(novo_ponto, novo_ponto2)
        else:
            forma.mover(novo_ponto)
            
        self.repository.update(index, forma)
