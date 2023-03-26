import random
import time

''' Álvaro de Araújo		RA 120113
    Rômulo Mincache 	    RA117477'''

inicio = time.time()
# Parâmetros do algoritmo Ant System
alpha = 1  # alpha, beta, rho e Q
beta = 1  # controla a influência da informação heurística
rho = 0.5  # coeficiente de evaporação do feromônio
Q = 1  # quantidade de feromônio depositada pelas formigas

formigas = 10
tarefas = 5
maquinas = 3
iteracao = 100

# Tempo de processamento de cada tarefa em cada máquina, 5 tarefas e 3 máquinas
tempoProcessamento = [[7, 2, 4], [8, 5, 1], [3, 6, 9], [4, 2, 1], [5, 8, 7]]

# Inicializa a matriz de feromônios com valores iguais para todas as arestas
feromoniosMatriz = [[1 for _ in range(tarefas)] for _ in range(tarefas)]


def tempoTotalProcessamento(sequencia):
    """
    Calcula o tempo total de processamento para uma dada sequência de tarefas.
    """
    tempoTotalMaquina = [0 for _ in range(maquinas)]
    tempoTotal = 0
    for task in sequencia:
        tempoTotalMaquina[0] += tempoProcessamento[task][0]
        for maquina in range(1, maquinas):
            tempoTotalMaquina[maquina] = max(
                tempoTotalMaquina[maquina], tempoTotalMaquina[maquina-1]) + tempoProcessamento[task][maquina]
        tempoTotal = max(tempoTotal, tempoTotalMaquina[-1])
    return tempoTotal


def gerarSolucaoFormigas():
    """
    Gera uma solução (sequência de tarefas) usando uma formiga.
    """
    tarefasNaoVisitadas = list(range(tarefas))
    sequencia = []
    tarefaAtual = random.choice(tarefasNaoVisitadas)
    tarefasNaoVisitadas.remove(tarefaAtual)
    sequencia.append(tarefaAtual)
    while tarefasNaoVisitadas:
        denominator = sum([feromoniosMatriz[tarefaAtual][j]**alpha *
                          (1 / tempoProcessamento[j][0])**beta for j in tarefasNaoVisitadas])
        probabilidades = [feromoniosMatriz[tarefaAtual][j]**alpha *
                          (1 / tempoProcessamento[j][0])**beta / denominator for j in tarefasNaoVisitadas]
        tarefaAtual = random.choices(
            tarefasNaoVisitadas, weights=probabilidades)[0]
        tarefasNaoVisitadas.remove(tarefaAtual)
        sequencia.append(tarefaAtual)
    return sequencia


def atualizarFeromonio(melhorSequencia):
    # Atualiza a matriz de feromônios com base na melhor sequência encontrada.
    global feromoniosMatriz
    deltaFeromonio = Q / tempoTotalProcessamento(melhorSequencia)
    feromoniosMatriz = [[(1 - rho) * feromoniosMatriz[i][j]
                         for j in range(tarefas)] for i in range(tarefas)]
    for i in range(tarefas - 1):
        feromoniosMatriz[melhorSequencia[i]
                         ][melhorSequencia[i+1]] += deltaFeromonio


def antSystem():
    # Executa o algoritmo Ant System para encontrar a melhor sequência de tarefas.
    melhorSequencia = None
    melhorTempoTotal = float('inf')
    for _ in range(iteracao):
        sequencias = [gerarSolucaoFormigas() for ant in range(formigas)]
        tempoTotals = [tempoTotalProcessamento(
            sequencia) for sequencia in sequencias]
        min_tempoTotal = min(tempoTotals)
        if min_tempoTotal < melhorTempoTotal:
            melhorTempoTotal = min_tempoTotal
            melhorSequencia = sequencias[tempoTotals.index(min_tempoTotal)]
        atualizarFeromonio(melhorSequencia)
    return melhorSequencia


melhorSequencia = antSystem()
print(f'Melhor sequência: {melhorSequencia}')
print(f'Tempo total: {tempoTotalProcessamento(melhorSequencia)}')

fim = time.time()
tempo_execucao = fim - inicio
print(f"Tempo de execução: {tempo_execucao} segundos")
