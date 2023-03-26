import pandas as pd
import osmnx as ox

# distância do vértice de inicio até o vértice atual
def custo(dfGrafo, u, v):
    return u.getCusto() + dfGrafo[(dfGrafo['u'] == u.getIdNo()) & (dfGrafo['v'] == v)]['length'].tolist()[0]


def recuperarCaminho(arvore):
    caminho = [arvore[-1].getIdNo()]
    pai = arvore[-1].getPai()
    cont = len(arvore) - 1

    bool = True
    while bool:
        if arvore[cont].getIdNo() == pai:
            caminho.append(arvore[cont].getIdNo())
            pai = arvore[cont].getPai()

        if pai == None:
            bool = False

        cont -= 1

    return caminho[::-1], arvore[-1].getCusto()

def grafoDataFrame(grafo):
    df = pd.DataFrame(ox.graph_to_gdfs(grafo, nodes=False))
    df = pd.DataFrame(df['length']).reset_index().copy()
    df.drop(['key'], axis=1, inplace=True)

    return df