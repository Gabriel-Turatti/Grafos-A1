from Grafo1 import Grafo, Nodo

def FloydWarshall(G):
    M = []
    for v in G.V:
        M.append([])
        for u in G.V:
            index = int(G.V[v].id)-1
            if v == u:
                M[index].append(0)
            else:
                M[index].append(float('inf'))
    for e in G.E:
        M[int(float(e[0].id))-1][int(float(e[1].id))-1] = int(float(e[2]))

    for v1 in G.V:
        for v2 in G.V:
            for v3 in G.V:
                iv1 = int(G.V[v1].id)-1
                iv2 = int(G.V[v2].id)-1
                iv3 = int(G.V[v3].id)-1
                if M[iv2][iv3] > M[iv2][iv1] + M[iv1][iv3]:
                    M[iv2][iv3] = M[iv2][iv1] + M[iv1][iv3]

    return M


# Exemplo de execução:
# (criamos um arquivo de teste para não demorar muito a execução)

grafo = Grafo()
with open('teste_FW.txt', 'r') as arquivo:
    info = arquivo.read()
    info = info.split('\n')
    grafo.lerArquivo(info)

Matrix = FloydWarshall(grafo)
id = 1
for c in Matrix:
    node = grafo.V[str(id)].id
    list = str(c)
    list = list[1:-1].replace(' ', '')
    print(node + ':' + list)
    id += 1 