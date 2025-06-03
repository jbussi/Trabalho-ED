class Grafo:
    def __init__(self):
        self.arestas = {}
    
    def adicionar_aresta(self, origem, destino, custo):
        self.arestas