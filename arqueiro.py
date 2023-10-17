from elfo import Elfo


class Arqueiro(Elfo):
    def __init__(self, usuario, senha):
        super().__init__(150, 50, usuario, senha)
