import uuid
import math
import random

from item import Item
class Personagem():
    def __init__(self, vida, ataque, defesa, usuario, senha):
        self.id = uuid.uuid4().hex
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = 1
        self.xp = 0
        self.dinheiro = 0
        self.usuario = usuario
        self.senha = senha
        self.itens = []
        self.classe = self.__class__.__name__
        self.qtdeItensEquipados = 0
        self.ataqueMaximo = 0
        self.defesaMaxima = 0

    def itemsToJson(self):
        jsonItens = []
        for item in self.itens:
            jsonItens.append(item.toJson())
        return jsonItens

    def itemFromJson(self, jsonItens):
        arrayDeItens = []
        for jsonItem in jsonItens:
            arrayDeItens.append(Item(jsonItem['nome'], jsonItem['vida'], jsonItem['ataque'], jsonItem['defesa'], jsonItem['preco'], jsonItem['equipado']))
        return arrayDeItens

    def toJson(self):
        return {
            "id": self.id,
            "vida": self.vida,
            "ataque": self.ataque,
            "defesa": self.defesa,
            "dinheiro": self.dinheiro,
            "nivel": self.nivel,
            "xp": self.xp,
            "usuario": self.usuario,
            "senha": self.senha,
            "itens": self.itemsToJson(),
            "classe": self.classe
        }
    
    def fromJson(self, jsonPersonagem):
        self.id = jsonPersonagem['id']
        self.vida = jsonPersonagem['vida']
        self.ataque = jsonPersonagem['ataque']
        self.defesa = jsonPersonagem['defesa']
        self.dinheiro = jsonPersonagem['dinheiro']
        self.nivel = jsonPersonagem['nivel']
        self.xp = jsonPersonagem['xp']
        self.itens = self.itemFromJson(jsonPersonagem['itens'])

    def getSenha(self):
        return self.senha
    
    def getUsuario(self):
        return self.usuario
    
    def getXp(self):
        return self.xp

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

    def setXp(self, xp):
        self.xp += xp
        if(self.xp >= self.nivelBreackpoint(self.nivel)):
            self.nivel += 1
            self.vida += 5
            print(f'{self.usuario} subiu de nivel para {self.nivel}')

    def setDinheiro(self, dinheiro):
        self.dinheiro = dinheiro

    def setItens(self, itens):
        self.itens = itens

    def atacar(self, personagemSelecionado):
        dano = self.ataque + ((self.ataqueMaximo/100) * random.randint(40, 100))
        return personagemSelecionado.defender(dano)

    def defender(self, dano):
        danoSofrido = dano - (self.defesa + ((self.defesaMaxima/100) * random.randint(40, 100)))
        if(danoSofrido <= 0):
            danoSofrido = 1
        return danoSofrido

    def gritoDeGuerra():
        pass

    def nivelBreackpoint(self, nivel):
        return (50 * math.pow(2, nivel))
    
    def equiparItem(self, item):
        self.qtdeItensEquipados = self.contItensEquipados()
        if(self.qtdeItensEquipados >= 6):
            print('Voce ja tem 6 itens equipados')
            return
        item.equipado = True
        self.qtdeItensEquipados += 1
        print(f'{item.nome} equipado')
    
    def desequiparItem(self, item):
        item.equipado = False
        self.qtdeItensEquipados -= 1
        print(f'{item.nome} desequipado')
    
    def equiparItens(self):
        self.ataqueMaximo = 0
        self.defesaMaxima = 0
        for item in self.itens:
            if(item.equipado):
                self.ataqueMaximo += item.ataque
                self.defesaMaxima += item.defesa
                print(self.ataqueMaximo)

    def contItensEquipados(self):
        cont = 0
        for item in self.itens:
            if(item.equipado):
                cont += 1
        return cont