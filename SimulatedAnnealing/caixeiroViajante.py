import matplotlib.pyplot as plt
import random
import math
import time

''' Álvaro de Araújo		RA 120113
    Rômulo Mincache 	    RA117477'''

inicio = time.time()

# Parâmetros do algoritmo
t_inicial = 100
t_final = 1
alpha = 0.99

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

# Função para calcular o custo de uma solução


def custo(solucao):
    c = 0
    for i in range(n):
        c += distancias[solucao[i]][solucao[(i + 1) % n]]
    return c


# Gera uma solução inicial aleatória
solucao_atual = random.sample(range(n), n)
custo_atual = custo(solucao_atual)

# Melhor solução encontrada
melhor_solucao = solucao_atual[:]
melhor_custo = custo_atual

# Temperatura atual
t = t_inicial

# Algoritmo Simulated Annealing
while t > t_final:
    # Gera uma nova solução a partir da solução atual
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    nova_solucao = solucao_atual[:]
    nova_solucao[i], nova_solucao[j] = nova_solucao[j], nova_solucao[i]
    novo_custo = custo(nova_solucao)

    # Decide se aceita a nova solução
    delta = novo_custo - custo_atual
    if delta < 0 or random.random() < math.exp(-delta / t):
        solucao_atual = nova_solucao
        custo_atual = novo_custo

        # Atualiza a melhor solução encontrada
        if novo_custo < melhor_custo:
            melhor_solucao = nova_solucao[:]
            melhor_custo = novo_custo

    # Atualiza a temperatura
    t *= alpha

# Imprime a melhor solução encontrada
print("Melhor solução:", [cidades[i][0] for i in melhor_solucao])
print("Custo:", melhor_custo)


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

fim = time.time()
tempo_execucao = fim - inicio
print(f"Tempo de execução: {tempo_execucao} segundos")

# Mostra o gráfico
plt.show()
