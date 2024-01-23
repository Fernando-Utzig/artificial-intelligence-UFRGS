from typing import Iterable, Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:Nodo, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        raise NotImplementedError


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    for i in range(0,9):
        if estado[i] == "_":
            pos_espaco = i

    ret = []
    possiveis_acoes = ["abaixo", "acima", "direita", "esquerda"]

    if pos_espaco in (0,1,2):
        ret.append(swap_positions(estado, pos_espaco, pos_espaco+3, possiveis_acoes[0])) # Quando vai para baixo a partir da linha 0
    elif pos_espaco in (3,4,5):
        ret.append(swap_positions(estado, pos_espaco, pos_espaco+3, possiveis_acoes[0])) # Quando vai para baixo a partir da linha 1
        ret.append(swap_positions(estado, pos_espaco, pos_espaco-3, possiveis_acoes[1])) # Quando vai para cima a partir da linha 1
    else:
        ret.append(swap_positions(estado, pos_espaco, pos_espaco-3, possiveis_acoes[1])) # Quando vai para cima a partir da linha 2

    if pos_espaco in (0,3,6):
        ret.append(swap_positions(estado, pos_espaco, pos_espaco+1, possiveis_acoes[2])) # Quando vai para direita a partir da coluna 0
    elif pos_espaco in (1,4,7):
        ret.append(swap_positions(estado, pos_espaco, pos_espaco+1, possiveis_acoes[2])) # Quando vai para direita a partir da coluna 1
        ret.append(swap_positions(estado, pos_espaco, pos_espaco-1, possiveis_acoes[3])) # Quando vai para esquerda a partir da coluna 1
    else:
        ret.append(swap_positions(estado, pos_espaco, pos_espaco-1, possiveis_acoes[3])) # Quando vai para esquerda a partir da coluna 2

    return ret

    
def swap_positions(estado, pos_elemento1, pos_elemento2, acao:str):
    ret_string = ""
    for i in range(len(estado)):
        if i == pos_elemento1:
            ret_string += estado[pos_elemento2]
        elif i == pos_elemento2:
            ret_string += estado[pos_elemento1]
        else:
            ret_string += estado[i]
    
    return (ret_string, acao)


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
