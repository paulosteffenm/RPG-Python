from alianca import Alianca


class Humano(Alianca):
    def __init__(self, ataque, defesa, usuario, senha):
        super().__init__(100, ataque, defesa, usuario, senha)
