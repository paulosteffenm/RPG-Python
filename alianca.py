from personagem import Personagem


class Alianca(Personagem):

    def __init__(self, vida, ataque, defesa, usuario, senha):
        super().__init__(vida, ataque, defesa, usuario, senha)

    def gritoDeGuerra(self):
        self.defesa = self.defesa*1.1
