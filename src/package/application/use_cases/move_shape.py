# pylint: disable = R1710, R0801
class MoveShape:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, index, novo_ponto, novo_ponto2=None):
        forma = self.repository.get(index)
        if forma is not None:
            if novo_ponto2 is not None and hasattr(forma, "mover"):
                forma.mover(novo_ponto, novo_ponto2)
            elif hasattr(forma, "mover"):
                forma.mover(novo_ponto)
            else:
                return None

        self.repository.update(index, forma)
