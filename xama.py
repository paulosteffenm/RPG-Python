from orc import Orc


class Xama(Orc):
    def __init__(self, usuario, senha):
        super().__init__(150, 50, usuario, senha)
