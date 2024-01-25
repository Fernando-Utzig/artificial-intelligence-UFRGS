from typing import Iterable, Set, Tuple
from queue import PriorityQueue

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __lt__(self, outro):
        return self.custo < outro.custo


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

# Usado apenas para trocar de posição dois elementos de uma string
def swap_positions(estado, pos_elemento1, pos_elemento2, acao:str):
    ret_string = ""
    for i in range(len(estado)):
        if i == pos_elemento1:
            ret_string += estado[pos_elemento2]
        elif i == pos_elemento2:
            ret_string += estado[pos_elemento1]
        else:
            ret_string += estado[i]
    
    return (acao, ret_string)


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    conjunto_nodos = []
    # pega os possiveis proximos estados
    sucessores = sucessor(nodo.estado)

    # cria um conjunto de nodos, cada um correspondente a um próximo estado
    for i in range(len(sucessores)):
        conjunto_nodos.append(Nodo(sucessores[i][1], nodo, sucessores[i][0], nodo.custo + 1)) # atribuição dos valores 'pai', 'estado', acao' e 'custo'

    return conjunto_nodos

def obter_caminho(nodo_atual: Nodo) -> list[str]:
    # Reconstruir o caminho para o objetivo
    caminho = []
    while nodo_atual:
        caminho.insert(0, nodo_atual.acao)
        nodo_atual = nodo_atual.pai
    return caminho[1:]  # Excluindo a ação 'None' do nó raiz

def hamming_distance(estado1: str, estado2: str) -> int:
    return sum(e1 != e2 for e1, e2 in zip(estado1, estado2))

def astar_hamming(estado:str)->list[str]:
    # Fila de prioridade para ordenar os nodos com base no custo total (f(n) = g(n) + h(n))
    fila_prioridade = PriorityQueue()

    # Objetivo
    estado_objetivo = "12345678_"

    # Variável responsável por somar os nós expandidos
    qtd_nodos_expandidos = 0
    
    # Nodo inicial
    nodo_inicial = Nodo(estado, None, None, 0)
    fila_prioridade.put((hamming_distance(estado, estado_objetivo), nodo_inicial))

    # Conjunto para manter o controle de estados já visitados
    estados_visitados = set()

    while not fila_prioridade.empty():
        _, nodo_atual = fila_prioridade.get()

        # Verificar se chegamos ao objetivo
        if nodo_atual.estado == estado_objetivo:
            # print(f"Quantidade nodos expadidos Hamming: {qtd_nodos_expandidos}")
            # Reconstruir o caminho para o objetivo
            return obter_caminho(nodo_atual)

        # Adicionar estado atual ao conjunto de estados visitados
        estados_visitados.add(nodo_atual.estado)

        # Gerar filhos do nodo atual
        filhos = expande(nodo_atual)
        # Incremento na quantidade de nós expandidos
        qtd_nodos_expandidos += len(filhos)

        for filho in filhos:
            if filho.estado not in estados_visitados:
                # Calcular custo total f(n) = g(n) + h(n)
                #qtd_nodos_expandidos += 1
                custo_total = filho.custo + hamming_distance(filho.estado, estado_objetivo)
                fila_prioridade.put((custo_total, filho))

    # Se a fila estiver vazia e não encontramos o objetivo, retornamos None
    #print(f"Quantidade nodos expadidos Hamming: {qtd_nodos_expandidos}")
    return None

def manhattan_distance(estado, objetivo):
    """
    Recebe um estado (string) e calcula a quantidade de movimentos que todas peças
    devem realizar para chegar no mesmo lugar do estado final
    :param estado: str
    :return: int
    """
    distancia = 0

    for i in objetivo:
        if i != "_":
            pos_atual = estado.index(i)
            pos_final = objetivo.index(i)
            linha_atual, coluna_atual = pos_atual // 3, pos_atual % 3
            linha_final, coluna_final = pos_final // 3, pos_final % 3
            distancia += abs(linha_atual - linha_final) + abs(coluna_atual - coluna_final)
    return distancia

def astar_manhattan(estado:str)->list[str]:
    # Fila de prioridade para ordenar os nodos com base no custo total (f(n) = g(n) + h(n))
    fila_prioridade = PriorityQueue()

    # Objetivo
    objetivo = "12345678_"

    # Variável responsável por somar os nós expandidos
    qtd_nodos_expandidos = 0
    
    # Nodo inicial
    nodo_inicial = Nodo(estado, None, None, 0)
    fila_prioridade.put((manhattan_distance(estado, objetivo), nodo_inicial))

    # Conjunto para manter o controle de estados já visitados
    estados_visitados = set()

    while not fila_prioridade.empty():
        _, nodo_atual = fila_prioridade.get()

        # Verificar se chegamos ao objetivo
        if nodo_atual.estado == objetivo:
            # print(f"Quantidade nodos expadidos Manhattan: {qtd_nodos_expandidos}")
            # Reconstruir o caminho para o objetivo
            return obter_caminho(nodo_atual)

        # Adicionar estado atual ao conjunto de estados visitados
        estados_visitados.add(nodo_atual.estado)

        # Gerar filhos do nodo atual
        filhos = expande(nodo_atual)
        # Incremento na quantidade de nós expandidos
        qtd_nodos_expandidos += len(filhos)

        for filho in filhos:
            if filho.estado not in estados_visitados:
                # Calcular custo total f(n) = g(n) + h(n)
                custo_total = filho.custo + manhattan_distance(filho.estado, objetivo)
                fila_prioridade.put((custo_total, filho))

    # Se a fila estiver vazia e não encontramos o objetivo, retornamos None
    return None

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
