import uuid

class Personagem():
    def __init__(self, vida, ataque, defesa, usuario, senha):
        self.id = uuid.uuid4()
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = 1
        self.usuario = usuario
        self.senha = senha
        self.itens = []
        
    def atacar():
        pass

    def defender():
        pass

    def gritoDeGuerra():
        pass
