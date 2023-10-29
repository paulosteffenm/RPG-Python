class Item():
    def __init__(self, nome, vida, ataque, defesa, preco):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.preco = preco

    def toJson(self):
        return {
        "nome": self.nome,
        "vida": self.vida,
        "ataque": self.ataque,
        "defesa": self.defesa,
        "preco": self.preco
        }
    
    def fromJson(self, jsonItem):
        self.nome= jsonItem['nome']
        self.vida= jsonItem['vida']
        self.ataque= jsonItem['ataque']
        self.defesa= jsonItem['defesa']
        self.preco= jsonItem['preco']
