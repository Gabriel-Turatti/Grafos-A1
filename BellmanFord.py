from Grafo1 import Grafo, Nodo


def BellmanFord(grafo: str, s: str):
    
    # Criação do grafo e leitura do arquivo
    g = Grafo()
    with open(grafo, 'r') as arquivo:
        info = arquivo.read()
        info = info.split('\n')
        g.lerArquivo(info)
    
    
    D = {}
    A = {}
    for v in g.vertices().keys():
        D[int(v)] = float('inf')
        A[int(v)] = None

    D[int(s)] = 0

    for i in range(1, g.qtdVertices()):
        for j in g.arestas():
            u = int(j[0].id)
            v = int(j[1].id)
            w = j[2]
            
            if D[v] > D[u] + float(w):
                D[v] = D[u] + float(w)
                A[v] = u

    for j in g.arestas():
        u = int(j[0].id)
        v = int(j[1].id)
        w = j[2]

        if D[v] > D[u] + float(w):
            return (False, None, None)

    return (True, D, A)


def montaCaminho(Grafo: str ='facebook_santiago.net', s: str = None):
    
    ciclo_neg, distancias, antecessores = BellmanFord(Grafo, s) 

    if ciclo_neg:
        lista = sorted(list(distancias.keys()))
        for v in lista:
            caminho = []
            nodo = v
            while nodo != int(s) and nodo != None:
                caminho.insert(0, str(nodo))
                nodo = antecessores[nodo]
            caminho.insert(0, str(nodo))
            print(f'{v}:', ','.join(caminho), end='')
            print(f'; d={distancias[v]}')
    else:
        print('Ciclo negativo encontrado!')
        

# Exemplo de execução:

montaCaminho('facebook_santiago.net', s='2')