import uuid

class Personagem():
    def __init__(self, vida, ataque, defesa, usuario, senha):
        self.id = uuid.uuid4().hex
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = 1
        self.dinheiro = 0
        self.usuario = usuario
        self.senha = senha
        self.itens = []
        self.classe = self.__class__.__name__

    def toJson(self):
        return {
            "id": self.id,
            "vida": self.vida,
            "ataque": self.ataque,
            "defesa": self.defesa,
            "dinheiro": self.dinheiro,
            "nivel": self.nivel,
            "usuario": self.usuario,
            "senha": self.senha,
            "itens": self.itens,
            "classe": self.classe
        }
    
    def fromJson(self, jsonPersonagem):
        self.id = jsonPersonagem['id']
        self.vida = jsonPersonagem['vida']
        self.ataque = jsonPersonagem['ataque']
        self.defesa = jsonPersonagem['defesa']
        self.dinheiro = jsonPersonagem['dinheiro']
        self.nivel = jsonPersonagem['nivel']
        self.itens = jsonPersonagem['itens']

    def getSenha(self):
        return self.senha
    
    def getUsuario(self):
        return self.usuario
    
    def setId(self, id):
        self.id = id

    def setVida(self, vida):
        self.vida = vida

    def setAtaque(self, ataque):
        self.ataque = ataque

    def setDefesa(self, defesa):
        self.defesa = defesa

    def setNivel(self, nivel):
        self.nivel = nivel

    def setDinheiro(self, dinheiro):
        self.dinheiro = dinheiro

    def setItens(self, itens):
        self.itens = itens

    def atacar(self, personagemSelecionado):
        dano = self.ataque + self.nivel
        return personagemSelecionado.defender(dano)

    def defender(self, dano):
        danoSofrido = dano - self.defesa
        if(danoSofrido <= 0):
            danoSofrido = 1
        return danoSofrido

    def gritoDeGuerra():
        pass
