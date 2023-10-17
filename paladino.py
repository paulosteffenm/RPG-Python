from humano import Humano


class Paladino(Humano):
    def __init__(self, usuario, senha):
        super().__init__(150, 50, usuario, senha)
