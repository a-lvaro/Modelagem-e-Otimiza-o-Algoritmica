import matplotlib.pyplot as plt
import random
import math
import time

''' Álvaro de Araújo		RA 120113
    Rômulo Mincache 	    RA117477'''

inicio = time.time()
# Parâmetros do algoritmo
alpha = 1.0
beta = 5.0
rho = 0.5
iteracoes = 100

# Cidades
cidades = [
    ("Cidade 1", (10, 20)),
    ("Cidade 2", (35, 35)),
    ("Cidade 3", (20, 10)),
    ("Cidade 4", (50, 75)),
    ("Cidade 5", (20, 30)),
    ("Cidade 6", (50, 80)),
    ("Cidade 7", (70, 52)),
    ("Cidade 8", (140, 30)),
    ("Cidade 9", (90, 10)),
    ("Cidade 10", (100, 50))
]

# Número de cidades
n = len(cidades)

# Distâncias entre as cidades
distancias = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = cidades[i][1]
        x2, y2 = cidades[j][1]
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        distancias[i][j] = d
        distancias[j][i] = d

# Feromônios iniciais
tau = [[1 for j in range(n)] for i in range(n)]

# Número de formigas
m = n

# Número de iterações
t_max = 100

# Melhor solução encontrada
melhor_solucao = None
melhor_custo = float("inf")

# Função para calcular o custo de uma solução


def custo(solucao):
    c = 0
    for i in range(n):
        c += distancias[solucao[i]][solucao[(i + 1) % n]]
    return c

# Função para escolher a próxima cidade


def proxima_cidade(atual, visitadas):
    probabilidades = []
    for i in range(n):
        if i not in visitadas:
            p = (tau[atual][i] ** alpha) * ((1 / distancias[atual][i]) ** beta)
            probabilidades.append(p)
        else:
            probabilidades.append(0)
    s = sum(probabilidades)
    probabilidades = [p / s for p in probabilidades]
    return random.choices(range(n), weights=probabilidades)[0]


def plotarGrafico():
    # Coordenadas das cidades
    x = [coord[0] for nome, coord in cidades]
    y = [coord[1] for nome, coord in cidades]

    # Desenha o gráfico
    plt.plot(x, y, 'co')

    # Desenha as linhas entre as cidades
    for i in range(n):
        i1 = melhor_solucao[i]
        i2 = melhor_solucao[(i + 1) % n]
        plt.arrow(x[i1], y[i1], x[i2] - x[i1], y[i2] - y[i1],
                  color='r', length_includes_head=True)

    # Mostra o nome das cidades
    for i in range(n):
        plt.annotate(cidades[i][0], (x[i], y[i]))

    # Mostra a distância total do caminho percorrido
    plt.title(f"Distância total: {melhor_custo:.2f}")

    # Mostra o gráfico
    plt.show()


# Algoritmo Ant System
for t in range(t_max):
    # Construção das soluções pelas formigas
    solucoes = []
    for k in range(m):
        solucao = [random.randint(0, n - 1)]
        visitadas = set(solucao)
        for i in range(n - 1):
            proxima = proxima_cidade(solucao[-1], visitadas)
            solucao.append(proxima)
            visitadas.add(proxima)
        solucoes.append(solucao)

    # Atualização dos feromônios
    delta_tau = [[0 for j in range(n)] for i in range(n)]
    for solucao in solucoes:
        c = custo(solucao)
        if c < melhor_custo:
            melhor_solucao = solucao[:]
            melhor_custo = c
        for i in range(n):
            delta_tau[solucao[i]][solucao[(i + 1) % n]] += iteracoes / c
            delta_tau[solucao[(i + 1) % n]][solucao[i]] += iteracoes / c
    for i in range(n):
        for j in range(i + 1, n):
            tau[i][j] = (1 - rho) * tau[i][j] + delta_tau[i][j]
            tau[j][i] = tau[i][j]

# Imprime a melhor solução encontrada
print("Melhor solução:", [cidades[i][0] for i in melhor_solucao])
print("Custo:", melhor_custo)

fim = time.time()
tempo_execucao = fim - inicio
print(f"Tempo de execução: {tempo_execucao} segundos")

plotarGrafico()
