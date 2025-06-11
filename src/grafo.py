#Grafo com distâncias entre cada par de nós interligados (Dado em horas)
class Grafo:
    def __init__(self):
        self.nos = {}
    
    def adicionar_no(self, no):
        if no not in self.nos:
            self.nos[no] = {}
    def adicionar_aresta(self, origem, destino, tempo: float):
        self.nos[origem][destino] = tempo
        self.nos[destino][origem] = tempo 
    
    def custo(self, origem, destino):
        return self.arestas[(origem, destino)]