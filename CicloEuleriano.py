from Grafo1 import Grafo, Nodo


def Hierholzer(g: Grafo):
    C = {}
    for e in g.arestas():
        C[frozenset([e[0].id, e[1].id])] = False
    i = 1
    while i < g.qtdVertices():
        v = g.getNodo(str(i))
        if v.conections > 0:
            break
        i += 1
    r, ciclo = buscaCiclo(g, i, C)
    if r == False:
        print(0)
        return (False, None)
    else:
        try:
            list(C.values()).index(False)
        except ValueError:
            print(1)
            print(','.join(ciclo))
            return (True, ciclo)
        else:
            print(0)
            return (False, None)


def buscaCiclo(g: Grafo, v: str, C):
    ciclo = []
    v = g.getNodo(str(v))
    ciclo.append(v.id)
    t = v
    while True:
        u = None
        e = None
        vizinhos = list(v.vizinhos.keys())
        for x in vizinhos:
            cont = len(vizinhos)
            if C[frozenset([x, v.id])] == False:
                u = g.getNodo(x)
                e = frozenset([x, v.id])
                break
            else:
                cont -= 1
            if cont == 0:
                return (False, None)
        C[e] = True
        v = u
        ciclo.append(v.id)
        if v == t:
            break
    for x in ciclo:
        for u in list(g.getNodo(x).vizinhos.keys()):
            if C[frozenset([x, u])] == False:
                (r, ciclo2) = buscaCiclo(g, x, C)
                if r == False:
                    return (False, None)
                i = ciclo.index(x)
                ciclo[i] = ciclo2.pop(0)
                for nodo in ciclo2:
                    i += 1
                    ciclo.insert(i, nodo)
    return (True, ciclo)


# Exemplo de execução:

grafo = Grafo()
with open('ContemCicloEuleriano.net', 'r') as arquivo:
    info = arquivo.read()
    info = info.split('\n')
    grafo.lerArquivo(info)
(Hierholzer(grafo))
