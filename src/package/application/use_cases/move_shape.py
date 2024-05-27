from src.package.domain import IRepository, LineSegment


class MoveShape:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def execute(self, index, novo_ponto1, novo_ponto2=None):
        forma = self.repository.get(index)
        if forma:
            if isinstance(forma, LineSegment) and novo_ponto2:
                forma.mover(novo_ponto1, novo_ponto2)
            else:
                forma.mover(novo_ponto1)
