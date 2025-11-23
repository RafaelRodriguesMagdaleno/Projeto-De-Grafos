from collections import deque  # Estrutura para otimizar operações em fila


def criar_grafo():
    # Começa com listas vazias
    vertices = []
    arestas = []
    # Aqui ele vai retornar duas listas
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    # Adciona o vértice se ele ainda não existir na lista
    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    # Garante que os vértices existam na lista
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)

    # Adiciona a aresta origem -> destino
    arestas.append([origem, destino])

    # Caso não seja direcionado, adiciona também destino -> origem
    if nao_direcionado:
        arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    # Remove a aresta origem -> destino se existir
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])

    # Se for não direcionado, remove também destino -> origem
    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])


def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        # Remove o vértice da lista
        vertices.remove(vertice)
        # Remove todas as arestas ligadas a ele
        arestas[:] = [a for a in arestas if vertice not in a]


def existe_aresta(arestas, origem, destino):
    # Verifica se tem uma aresta origem -> destino
    return [origem, destino] in arestas


def vizinhos(vertices, arestas, vertice):
    # Retorna os vizinhos do vértice
    vizinhos = []
    for origem, destino in arestas:
        if origem == vertice:
            vizinhos.append(destino)
    return vizinhos


def grau_vertices(vertices, arestas):
    # Inicializa dicionário com graus zerados
    graus = {v: {"entrada": 0, "saida": 0, "total": 0} for v in vertices}

    for origem, destino in arestas:
        # Incrementa saída do vértice origem
        graus[origem]["saida"] += 1
        # Incrementa entrada do vértice destino
        graus[destino]["entrada"] += 1

    # Calcula o total = entrada + saída
    for v in vertices:
        graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]

    return graus


def percurso_valido(arestas, caminho):
    # Verifica se o percurso é possível, pelas as arestas que foram dadas
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i+1]
        if not existe_aresta(arestas, u, v):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    # Lista os vizinhos de um vértice
    viz = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {', '.join(viz) if viz else 'nenhum'}")


def exibir_grafo(vertices, arestas):
    # Mostra todas as arestas do grafo
    print("Vértices:", vertices)
    print("Arestas:")
    for origem, destino in arestas:
        print(f"{origem} -> {destino}")

# Busca em Largura padrão

# A busca de Largura guarda o vértice origme e o caminho que faz até o vertice destino em filas

def bfs(vertices, arestas, inicio):

    fila = deque([{"vertice": inicio, "caminho": [inicio]}])
    visitados = []

    while fila:
        item = fila.popleft()
        vertice = item["vertice"]
        caminho = item["caminho"]

        if vertice not in visitados:
            visitados.append(vertice)

            for viz in vizinhos(vertices, arestas, vertice):
                # Aqui ele verifica se o vizinho já esta na lista
                if viz not in visitados and all(viz != elem["vertice"] for elem in fila):
                    fila.append({"vertice": viz, "caminho": caminho + [viz]})

    return visitados

# Busca em Largura para Menor Caminho

#Ela prioriza encontrar o menor caminho entre o vertíce de origem e o vertice de destino, guarda o caminho até ele 

def bfs_menor_caminho(vertices, arestas, inicio, destino):

    fila = deque([{"vertice": inicio, "caminho": [inicio]}])
    visitados = []

    while fila:
        item = fila.popleft()
        vertice = item["vertice"]
        caminho = item["caminho"]

        if vertice == destino:
            return caminho  # Aqui ele vê se chegou no destino, e caso tenha chegado, ele mostra o caminho até ele

        if vertice not in visitados:
            visitados.append(vertice)

            for viz in vizinhos(vertices, arestas, vertice):
                if viz not in visitados and all(viz != elem["vertice"] for elem in fila):
                    fila.append({"vertice": viz, "caminho": caminho + [viz]})

    return []  # E ele vai retornar vazio caso não encontre o caminho

# Busca em Profundidade (DFS)

# A busca em profundidade guarda o vértice origem e o caminho até o destino em uma pilha (LIFO)

def dfs(vertices, arestas, inicio):

    pilha = [{"vertice": inicio, "caminho": [inicio]}]
    visitados = []

    while pilha:
        item = pilha.pop()  # Retira o último elemento da pilha
        vertice = item["vertice"]
        caminho = item["caminho"]

        if vertice not in visitados:
            visitados.append(vertice)

            for viz in vizinhos(vertices, arestas, vertice):
                # Verifica se o vizinho já está na pilha ou já foi visitado
                if viz not in visitados and all(viz != elem["vertice"] for elem in pilha):
                    pilha.append({"vertice": viz, "caminho": caminho + [viz]})

    return visitados

# Busca em Profundidade para Detecção de Ciclos

# A busca em profundidade agora guarda o vértice atual e o vértice pai que o adicionou na pilha
# Isso permite identificar ciclos ignorando a ligação direta com o pai

def dfs_detectar_ciclo(vertices, arestas, inicio):
    pilha = [{"vertice": inicio, "pai": None}]  # Inserir vértice inicial com pai vazio
    visitados = []

    while pilha:
        item = pilha.pop()
        vertice = item["vertice"]
        pai = item["pai"]

        if vertice not in visitados:
            visitados.append(vertice)

            for viz in vizinhos(vertices, arestas, vertice):
                if viz not in visitados and all(viz != elem["vertice"] for elem in pilha):
                    pilha.append({"vertice": viz, "pai": vertice})
                else:
                    if viz != pai:
                        return True  # ciclo detectado

    return False  # Nenhum ciclo detectado

# Programa principal abaixo

def main():
    vertices, arestas = criar_grafo()

    # Aqui estou criando um grafo de exemplo
    inserir_aresta(vertices, arestas, "A", "B")
    inserir_aresta(vertices, arestas, "B", "C", nao_direcionado=True)
    inserir_aresta(vertices, arestas, "A", "D")
    inserir_aresta(vertices, arestas, "D", "E")

    exibir_grafo(vertices, arestas)

    listar_vizinhos(vertices, arestas, "B")

    print("Graus:", grau_vertices(vertices, arestas))

    caminho = ["A", "B", "C"]
    print("Percurso válido?", percurso_valido(arestas, caminho))

    print("\n--- Busca de Largura Padrão ---")
    print("Visitados a partir de A:", bfs(vertices, arestas, "A"))

    print("\n--- Busca de Largura por menor Caminho ---")
    menor = bfs_menor_caminho(vertices, arestas, "A", "C")
    print("Menor caminho de A até C:", menor if menor else "não encontrado")

    print("\n--- Busca em Profundidade (DFS) ---")
    print("Visitados a partir de A:", dfs(vertices, arestas, "A"))

    print("\n--- DFS para Detecção de Ciclos ---")
    ciclo = dfs_detectar_ciclo(vertices, arestas, "A")
    print("Ciclo detectado?", "Sim" if ciclo else "Não")


if __name__ == "__main__":
    main()
