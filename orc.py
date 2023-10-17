from horda import Horda


class Orc(Horda):
    
    def __init__(self, ataque, defesa, usuario, senha):
        super().__init__(100, ataque, defesa, usuario, senha)
