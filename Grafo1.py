class Nodo():
    def __init__(self, n, rotulo):
        self.id = n
        self.rotulo = rotulo
        self.conections = 0
        self.vizinhos = {}

class Grafo():
    def __init__(self):
        self.V = {}
        self.nV = 0
        self.E = []
        self.nE = 0

    def qtdVertices(self):
        return self.nV

    def qtdArestas(self):
        return self.nE

    def grau(self, v):
        return v.conections

    def rotulo(self, v):
        return v.rotulo

    def vizinhos(self, v):
        return v.vizinhos

    def haAresta(self, u, v):
        if u.vizinhos[v.id] < float('inf'):
            return True
        return False

    def peso(self, u, v):
        return u.vizinhos[v]

    def getNodo(self, id):
        return self.V[id]

    def lerArquivo(self, arquivo):
        leitura = 0
        for linha in arquivo:
            if linha == '':
                continue
            if linha[0] == '*':
                leitura += 1
                continue
            else:
                if leitura == 1:
                    valores = linha.split(' ')
                    node = Nodo(valores[0], valores[1])
                    self.V[node.id] = node
                    self.nV += 1
                elif leitura == 2:
                    valores = linha.split(' ')
                    u = self.getNodo(valores[0])
                    v = self.getNodo(valores[1])
                    u.conections += 1
                    v.conections += 1
                    self.nE += 1
                    self.E.append([u, v, valores[2]])


grafo = Grafo()
with open('facebook_santiago.net', 'r') as arquivo:
    info = arquivo.read()
    info = info.split('\n')
    grafo.lerArquivo(info)