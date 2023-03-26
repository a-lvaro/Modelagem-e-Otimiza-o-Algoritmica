import random
import numpy

from deap import base
from deap import creator
from deap import algorithms
from deap import tools


''' Álvaro de Araújo		RA 120113
    Rômulo Barreto 		    RA117477'''


class Cidade():
    def __init__(self, nome, coordenadas):
        self.nome = nome
        self.coordenadas = coordenadas


# adiciona as cidades na lista_cidades
lista_cidades = []
lista_cidades.append(Cidade("Cidade 1", (10, 20)))
lista_cidades.append(Cidade("Cidade 2", (35, 35)))
lista_cidades.append(Cidade("Cidade 3", (20, 10)))
lista_cidades.append(Cidade("Cidade 4", (50, 75)))
lista_cidades.append(Cidade("Cidade 5", (20, 30)))
lista_cidades.append(Cidade("Cidade 6", (50, 80)))
lista_cidades.append(Cidade("Cidade 7", (70, 52)))
lista_cidades.append(Cidade("Cidade 8", (140, 30)))
lista_cidades.append(Cidade("Cidade 9", (90, 10)))
lista_cidades.append(Cidade("Cidade 10", (100, 50)))


# define a distância euclidiana entre duas cidades
def distancia(cidade1, cidade2):
    return numpy.sqrt((cidade1.coordenadas[0] - cidade2.coordenadas[0])**2 +
                      (cidade1.coordenadas[1] - cidade2.coordenadas[1])**2)


# define a função de avaliação
def avaliacao(individual):
    distancia_total = 0
    for i in range(len(individual)):
        cidade_atual = lista_cidades[individual[i]]
        cidade_proxima = lista_cidades[individual[(i + 1) % len(individual)]]
        distancia_total += distancia(cidade_atual, cidade_proxima)
    return distancia_total,


# cria o framework do algoritmo genético
toolbox = base.Toolbox()
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox.register("indices", random.sample, range(
    len(lista_cidades)), len(lista_cidades))
toolbox.register("individual", tools.initIterate,
                 creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", avaliacao)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.01)
toolbox.register("select", tools.selTournament, tournsize=3)

if __name__ == "__main__":
    populacao = toolbox.population(n=50)
    probabilidade_crossover = 0.7
    probabilidade_mutacao = 0.5
    numero_geracoes = 500

    # registra as estatísticas
    estatisticas = tools.Statistics(
        key=lambda individuo: individuo.fitness.values)
    estatisticas.register("min", numpy.min)
    estatisticas.register("avg", numpy.mean)

    populacao, info = algorithms.eaSimple(populacao, toolbox,
                                          probabilidade_crossover,
                                          probabilidade_mutacao,
                                          numero_geracoes, estatisticas)
    melhores = tools.selBest(populacao, 1)

    # imprime o melhor indivíduo
    print('\n\n')
    for individuo in melhores:
        print('individuo: ', individuo)
        print('Distância percorrida: ', individuo.fitness)

        rota = []
        for i in individuo:
            rota.append(lista_cidades[i].nome)
        print("Melhor rota encontrada:")
        print(rota)
