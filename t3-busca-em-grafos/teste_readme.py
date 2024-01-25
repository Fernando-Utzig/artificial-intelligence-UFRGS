import time
import solucao as solucao

estado_inicial = "2_3541687"

def teste_a_hamming():
    inicio = time.time()
    ret = solucao.astar_hamming(estado_inicial)
    fim = time.time()

    print(f"Tempo hamming: {fim - inicio}")
    print(f"Custo hamming: {len(ret)}\n")

def teste_a_manhattan():
    inicio = time.time()
    ret = solucao.astar_manhattan(estado_inicial)
    fim = time.time()

    print(f"Tempo manhattan: {fim - inicio}")
    print(f"Custo manhattan: {len(ret)}\n")

teste_a_hamming()
teste_a_manhattan()