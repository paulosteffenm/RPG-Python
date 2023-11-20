class Item():
    def __init__(self, nome, vida, ataque, defesa, preco, equipado):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.preco = preco
        self.equipado = equipado

    def toJson(self):
        return {
        "nome": self.nome,
        "vida": self.vida,
        "ataque": self.ataque,
        "defesa": self.defesa,
        "preco": self.preco,
        "equipado": self.equipado
        }
    
    def fromJson(self, jsonItem):
        self.nome= jsonItem['nome']
        self.vida= jsonItem['vida']
        self.ataque= jsonItem['ataque']
        self.defesa= jsonItem['defesa']
        self.preco= jsonItem['preco']
        self.equipado= jsonItem['equipado']
