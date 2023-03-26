class Vertice:
    def __init__(self, idNo, pai, custo, heuristica=None, profundidade=None):
        self.__idNo = idNo
        self.__pai = pai
        self.__custo = custo
        self.__heuristica = heuristica
        self.__profundidade = profundidade

    def setIdNo(self, idNo):
        self.__idNo = idNo

    def setPai(self, pai):
        self.__pai = pai

    def setCusto(self, custo):
        self.__custo = custo

    def setHeuristica(self, heuristica):
        self.__heuristica = heuristica

    def setProfundidade(self, profundidade):
        self.__profundidade = profundidade

    def getIdNo(self):
        return self.__idNo

    def getPai(self):
        return self.__pai

    def getCusto(self):
        return self.__custo

    def getHeuristica(self):
        return self.__heuristica

    def getProfundidade(self):
        return self.__profundidade

    def __str__(self):
        return f'IdNo: {self.__idNo}, Pai: {self.__pai}, Custo: {self.__custo}, Heuristica: {self.__heuristica}'

    def __lt__(self, other):
        return self.__custo + self.__heuristica < other.__custo + other.__heuristica
