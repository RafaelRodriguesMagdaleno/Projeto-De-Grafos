class Grafo :
    
    #Definir inicialização
    
    ##Vertices = Quantidade de vertices que vamos ter no grafo
    
    def __init__(self,vertices):
        
        #Atribuindo o vertices para a variavel
        self.vertices = vertices
        
        #Lista de Adjacencia
        
        #Não sabemos qual o tamanho da lista
        
        #Vai ter uma quantidade de linhas = quantidade de vertices
        self.grafo = [[] for i in range(self.vertices)]
    
    def adciona_aresta(self, u,v):
        
        #Pensando em grafo direcionado
        
        #temos u-1 por que falamos para ir na linha do U e acrescentar o V
        self.grafo[u-1].append(v)
        
        #Para grafos não direcionados
        
        #self.grafo[v-1].append(u) 
        
        #Por que estamos falando que tem uma outra aresta que sai do V e chega no U
        
    def mostra_lista(self):
        #vamos imprimir cada linha
        
        #o for vai percorrer as linhas, ele vai até um número menor que self.vertives -1 e para corrigir vamos aumentar 1
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            
            #Esse for vai ser para cada elemento da linha
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            #Quando ele terminar toda a linha ai ele vai para o proxímo
            print('')
            
g = Grafo(4)

g.adciona_aresta(1,2)
g.adciona_aresta(1,3)
g.adciona_aresta(1,4)
g.adciona_aresta(2,3)

g.mostra_lista()