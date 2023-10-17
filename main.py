from arqueiro import Arqueiro
from bruxo import Bruxo
from guerreiro import Guerreiro
from ladino import Ladino
from mago import Mago
from paladino import Paladino
from sacerdote import Sacerdote
from xama import Xama


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
    'Sacerdode': Sacerdote
}

personagens = []
personagemLogado = None


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

menuLogin = int(input('\nSeleiona a Opcao\n1 - Login\n2 - Cadastro\n:'))

if menuLogin == 1:
    retorno = cadastraPersonagem()
    if retorno:
        personagens.append(retorno)
    else:
        print('\nErro ao Cadastrar Personagem')

# menuPrincipal = int('\nSeleciona a Opcao\n1 - Status\n2 - Batalha\n3 - Level Up\n4 - Comprar Item\n5 - Sair')
