import random
import numpy as np

from deap import base
from deap import creator
from deap import algorithms
from deap import tools


''' Álvaro de Araújo		RA 120113
    Rômulo Barreto 		    RA117477'''

def avaliacao(individuo):
    # calcula o número de conflitos (ameaças) no tabuleiro
    conflicts = 0
    for i in range(len(individuo)):
        for j in range(i+1, len(individuo)):
            if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == j - i:
                conflicts += 1
    # retorna o inverso do número de conflitos como a pontuação de aptidão
    return 1.0 / (conflicts + 1),


# define o tamanho do tabuleiro
n = 8

# cria o framework do algoritmo genético
toolbox = base.Toolbox()
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox.register("attr_int", random.randint, 0, n-1)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_int, n=n)
toolbox.register("populacao", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", avaliacao)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=n-1, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# roda o algoritmo genético
if __name__ == "__main__":
    tamanho_populacao = 389
    probabilidade_crossover = 0.79
    probabilidade_mutacao = 0.03
    numero_geracoes = 200

    # iniciar a população
    populacao = toolbox.populacao(n=tamanho_populacao)

    # rodar o algoritmo genético
    statistics = tools.Statistics(key=lambda ind: ind.fitness.values)
    statistics.register("max", np.max)
    statistics.register("min", np.min)
    statistics.register("avg", np.mean)
    statistics.register("std", np.std)

    mu = len(populacao)
    lambda_ = tamanho_populacao - mu
    populacao, info = algorithms.eaMuPlusLambda(populacao, toolbox, mu, lambda_,
                                                probabilidade_crossover,
                                                probabilidade_mutacao,
                                                numero_geracoes,
                                                stats=statistics,
                                                verbose=True)

    # mostrar o melhor indivíduo encontrado
    melhores = tools.selBest(populacao, k=1)[0]
    print("Best individual found: ", melhores)
    print("Fitness score: ", melhores.fitness.values[0])

    for i in range(len(melhores)):
        for j in range(len(melhores)):
            if melhores[i] == j:
                print('Q', end=' ')
            else:
                print('-', end=' ')

        print('\n')
    print('\n\n')
