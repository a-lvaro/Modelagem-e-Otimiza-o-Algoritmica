import osmnx as ox

from visualizarGrafo import mostrarPontosNoGrafo, mostrarCaminho
from funcoes import grafoDataFrame
from aestrela import buscaAestrela


class Rota:
    def __init__(self):

        self.noInicio = 8859042730
        self.noFim = 1415538243

        self.grafo_inga = ox.graph_from_address('Maringá, PR, Brazil')

        self.dfGrafo = grafoDataFrame(self.grafo_inga)

    def mostrarPontos(self):
        mostrarPontosNoGrafo(self.grafo_inga, self.noInicio, self.noFim)

    def bucaAestrela(self):
        arvore = buscaAestrela(
            self.grafo_inga, self.dfGrafo, self.noInicio, self.noFim)
        mostrarCaminho(arvore, self.grafo_inga, "A*")

