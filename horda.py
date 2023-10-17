from personagem import Personagem


class Horda(Personagem):
    def __init__(self, vida, ataque, defesa, usuario, senha):
        super().__init__(vida, ataque, defesa, usuario, senha)
        
    def gritoDeGuerra(self):
        self.ataque = self.ataque*1.1