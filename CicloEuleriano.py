from Grafo1 import Grafo, Nodo


def Hierholzer(g: Grafo):
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


def buscaCiclo(g: Grafo, v: Nodo, C):
    ciclo = []
    ciclo.append(v)
    t = v
    while True:
        u = None
        for x in list(v.vizinhos().keys()):
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
    for x in ciclo:
        for u in list(x.vizinhos().keys()):
            if C[frozenset(x, u.id())] == False:
                (r, ciclo2) = buscaCiclo(g, x, C)
                if r == False:
                    return (False, None)
                i = ciclo.index(x)
                ciclo[i] = ciclo2.pop(0)
                for nodo in ciclo2:
                    i += 1
                    ciclo.insert(i, nodo)
    return (True, ciclo)


'''grafo = Grafo()
with open(r'D:\UFSC\Grafos\atividade1\Grafos-A1\facebook_santiago.net', 'r') as arquivo:
    info = arquivo.read()
    info = info.split('\n')
    grafo.lerArquivo(info)
print(Hierholzer(grafo))'''
