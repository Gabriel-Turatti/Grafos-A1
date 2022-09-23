from Grafo1 import Grafo, Nodo


def Hierholzer(g:Grafo):
    C = {}
    for e in g.arestas():
        C[frozenset(e[0].id(), e[1].id())] = False
    while True:
        i = 0
        v = g.getNodo(g.arestas().keys()[i])
        if v.conections() > 0:
            break
    r, ciclo = buscaCiclo(g, v, C)
    if r == False or C.values().find() != -1:
        return (False, None)
    else:
        return (True, ciclo)

        

def buscaCiclo(g:Grafo, v:Nodo, C):
    ciclo = []
    ciclo.append(v)
    t = v
    while True:
        u = None
        for x in v.vizinhos().keys():
            i = 0
            if C[frozenset(x, v.id())] == False:
                u = x
                e = frozenset(x, v.id())
                continue
            return (False, None)
        C[e] = True
        v = u
        ciclo.append(v)
        if v == t:
            break

    

        