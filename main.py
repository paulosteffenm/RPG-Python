import json
from arqueiro import Arqueiro
from bruxo import Bruxo
from guerreiro import Guerreiro
from ladino import Ladino
from mago import Mago
from paladino import Paladino
from sacerdote import Sacerdote
from xama import Xama
from item import Item

CONST_HIERARQUIA = {
    'Reinos': {
        'Horda': {
            'Orc': ['Xama', 'Guerreiro'],
            'Goblin': ['Bruxo', 'Ladino']
        },
        'Alianca': {
            'Humano': ['Mago', 'Paladino'],
            'Elfo': ['Arqueiro', 'Sacerdote']
        }
    }
}

CONST_CLASSES = {
    'Xama': Xama,
    'Guerreiro': Guerreiro,
    'Bruxo': Bruxo,
    'Ladino': Ladino,
    'Mago': Mago,
    'Paladino': Paladino,
    'Arqueiro': Arqueiro,
    'Sacerdote': Sacerdote
}

CONST_ITENS = {
    'Luva': Item('Luva', 100, 100, 100, 100),
    'Capacete': Item('Capacete', 200, 200, 200, 200)
}

PERSONAGENS = []
PERSONAGEM_LOGADO = None

def atualizaMemoria():
    with open("memoria.json", "w") as outfile:
        jsonDictionary = []
        for personagem in PERSONAGENS:
            jsonDictionary.append(personagem.toJson())
        json_personagens = json.dumps(jsonDictionary, indent=4)
        outfile.write(json_personagens)

def lerMemoria():
    with open("memoria.json", "r") as openfile:
        jsonPersonagens = json.load(openfile)
        for jsonPersonagem in jsonPersonagens:
            personagemToAppend = CONST_CLASSES.get(jsonPersonagem['classe'], None)(jsonPersonagem['usuario'], jsonPersonagem['senha'])
            personagemToAppend.fromJson(jsonPersonagem)
            PERSONAGENS.append(personagemToAppend)


def cadastraPersonagem():

    usuario = input('Nome do Usuario: ')
    senha = input('Senha: ')
    reino = input(f'Reino({'/'.join(CONST_HIERARQUIA['Reinos'].keys())}): ')
    if reino in CONST_HIERARQUIA['Reinos']:
        raca = input(
            f'Raça ({'/'.join(CONST_HIERARQUIA['Reinos'][reino].keys())}): ')

        if raca in CONST_HIERARQUIA['Reinos'][reino]:
            classe = input(
                f'Classe ({", ".join(CONST_HIERARQUIA["Reinos"][reino][raca])}): ')

            if classe in CONST_HIERARQUIA['Reinos'][reino][raca]:
                classeSelecionada = CONST_CLASSES.get(classe, None)
                if classeSelecionada:
                    return classeSelecionada(usuario, senha)
                else:
                    print('Classe inválida')
                    return None
            else:
                print('Classe inválida')
                return None
        else:
            print('Raça inválida')
            return None
    else:
        print('Reino inválida')
        return None

def loginPersonagem():
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    return next((personagem for personagem in PERSONAGENS if personagem.usuario == usuario and personagem.senha == senha), None)

def realizarMissao():
    print(f'{PERSONAGEM_LOGADO.usuario} completou a missao e obteve +50 dinheiros e 1 nivel')
    PERSONAGEM_LOGADO.setNivel(PERSONAGEM_LOGADO.nivel + 1)
    PERSONAGEM_LOGADO.setDinheiro(PERSONAGEM_LOGADO.dinheiro + 50)
    atualizaMemoria()

def batalha():
    print('Seleciona o usuario para batalha')
    for personagem in PERSONAGENS:
        if(personagem.usuario != PERSONAGEM_LOGADO.usuario):
            print(f'{personagem.usuario}: Nivel {personagem.nivel}')

    personagemSeleciondo = input(':')
    personagemEncontrado = next((personagem for personagem in PERSONAGENS if personagem.usuario == personagemSeleciondo), None)

    vidaA = personagemEncontrado.vida
    vidaB = PERSONAGEM_LOGADO.vida

    while(True):
        danoCausado = personagemEncontrado.atacar(PERSONAGEM_LOGADO)
        vidaB -= danoCausado
        print(f'{PERSONAGEM_LOGADO.usuario} sofreu {danoCausado}: Vida {vidaB}')
        if(vidaB<=0):
            break

        danoCausado = PERSONAGEM_LOGADO.atacar(personagemEncontrado)
        vidaA -= danoCausado
        print(f'{personagemEncontrado.usuario} sofreu {danoCausado}: Vida {vidaA}')
        if(vidaA<=0):
            break
    
    if(vidaA > vidaB):
        print(f'{personagemEncontrado.usuario} venceu')
    else:
        print(f'{PERSONAGEM_LOGADO.usuario} venceu')

def loja():
    for itemKey, itemObj in CONST_ITENS.items():
        print(f'Nome: {itemObj.nome}, Vida: {itemObj.vida}, Ataque: {itemObj.ataque}, Defesa: {itemObj.defesa}, Preco: {itemObj.preco}')
        
    nomeItem = input('Nome Item: ')
    if nomeItem in CONST_ITENS:
        itemEncontrado = CONST_ITENS[nomeItem]
        if PERSONAGEM_LOGADO.dinheiro >= itemEncontrado.preco:
            PERSONAGEM_LOGADO.itens.append(itemEncontrado)
            PERSONAGEM_LOGADO.setDinheiro(PERSONAGEM_LOGADO.dinheiro - itemEncontrado.preco)
            atualizaMemoria()
        else:
            print('No money for you')
    else:
        print('Item nao encontrado')

def menuPrincipal():
    while(True):
        menuLogin = int(input('\nSeleiona a Opcao\n1 - Missao\n2 - Batalhar\n3 - Loja\n4 - Sair:\n'))
        if menuLogin == 1:
            realizarMissao()
            
        elif menuLogin == 2:
            batalha()
        elif menuLogin == 3:
            loja()
            pass
        elif menuLogin == 4:
            break
        else:
            print('Opcao Invalida')

lerMemoria()

menuLogin = int(input('\nSeleiona a Opcao\n1 - Cadastro\n2 - Login\n:'))

if menuLogin == 1:
    retorno = cadastraPersonagem()
    if retorno:
        PERSONAGENS.append(retorno)
        PERSONAGEM_LOGADO = retorno
        atualizaMemoria()
        menuPrincipal()
    else:
        print('\nErro ao Cadastrar Personagem')
elif menuLogin == 2:
    PERSONAGEM_LOGADO = loginPersonagem()
    if(PERSONAGEM_LOGADO):
        menuPrincipal()
    else:
        print('Usuario nao encontrado')

# menuPrincipal = int('\nSeleciona a Opcao\n1 - Status\n2 - Batalha\n3 - Level Up\n4 - Comprar Item\n5 - Sair')
