from Grafo1 import Grafo


def buscaLargura(nome_arquivo: str, s: str):
    '''Função que faz a instancia do grafo e a sua busca em largura
        a partir de um arquivo de texto'''
    
    # Criação do grafo e leitura do arquivo
    grafo = Grafo()
    with open(nome_arquivo, 'r') as arquivo:
        info = arquivo.read()
        info = info.split('\n')
        grafo.lerArquivo(info)

    # Algoritmo de busca em largura
    conhecido = [False] * (grafo.qtdVertices() + 1)
    distancia = [float('inf')] * (grafo.qtdVertices() + 1)
    ancestral = [None] * (grafo.qtdVertices() + 1)

    conhecido[int(s)] = True
    distancia[int(s)] = 0
    fila = []
    fila.append(grafo.getNodo(s))

    while fila:
        u = fila.pop(0)
        for v in grafo.vizinhos(u):
            i = int(v)
            if conhecido[i] == False:
                conhecido[i] = True
                distancia[i] = distancia[int(u.id)] + 1
                ancestral[i] = u
                fila.append(grafo.getNodo(v))

    return (distancia, ancestral)


def printResult(s: str):
    '''Função que imprime o resultado a busca em largura a partir do
        arquivo 'facebook_santiago.net' e da variável de entrada 's' '''

    # Print da primeira linha com o elemento de origem
    print("0: " + s)
    
    # Resultados da busca
    distancia, ancestral = buscaLargura('facebook_santiago.net', s)
    
    # Loop para o print das distâncias a partir da de número 1 
    count = 1
    while True:
        aux = []
        for i in range(len(distancia)):
            if distancia[i] == count:
                aux.append(i)
        
        if not aux:
            break 

        print(f'{count}: {aux[0]}', end='')
        for i in range(1, len(aux)):
            print(f",{aux[i]}", end='')
        print()
        
        count += 1


# Exemplo de execução:

num_input = input("Digite o id do nodo de origem da busca:")
printResult(num_input)
