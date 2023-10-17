from goblin import Goblin


class Bruxo(Goblin):
    def __init__(self, usuario, senha):
        super().__init__(150, 50, usuario, senha)
