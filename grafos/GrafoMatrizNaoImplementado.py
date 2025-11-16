class Grafo :
    
    #Matriz de Adjacência
    
    #Inicialização da classe chamando com a variavel vertices que é a quantidade de vertices do grafo
    def __init__(self, vertices):
        #Recebe o mesmo valor da quantidade de vertices
        self.vertices = vertices
        #Matriz Adjacências, ela é uma lista dentro de uma lista
        
        #Ele multiplica pela quantidade de vertices que vai ser a quantidade de linhas e colunas
        self.grafo =[[0]*self.vertices for i in range(self.vertices)]
    
    #Ele dá como entrada os dois vertices que estão conectados
    def adicionar_aresta(self, u, v):
        #Matriz Adjacência
        
        #No python as contagem de lista comceça com 0, então o 0 vai ser o vertice 1 e o 1 o vertice 2
        
        #Para fazer uma contagem de aresta, troque o = por += se for grafo multiplo
        
        #Esse é para grafos direcionados simples
        #Se não for simples troque o = por +=
        self.grafo[u-1][v-1] = 1
        
        #Se não for um grafo direcionado
        #self.grafo[v-1][u-1] = 1
        
    def mostra_matriz(self):
        print("A matriz de adjacências é ")
        #Percorre a lista principal e imprimi os elementos diretos, percorre do 0 até o elemento menor que o self.vertices
        for i in range(self.vertices):
            #Na posição i está a linha inteira
            print(self.grafo[i])

# Grafo com 4 vertices

#Fazendo isso o self.vertices virou 4 e o self.grafo está zerado, e se mostrar a matriz adjacência será uma matriz de 4x4 tudo zerado
g = Grafo(4)
g.adicionar_aresta(1,2)
g.adicionar_aresta(3,4)
g.adicionar_aresta(2,3)

g.mostra_matriz()