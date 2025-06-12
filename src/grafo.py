#Grafo com distâncias entre cada par de nós interligados (Dado em horas)
import heapq
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
        visitados = set()
        fila = [(0, origem)]  # (custo acumulado, nó atual)
        distancias = {no: float('inf') for no in self.nos}
        distancias[origem] = 0

        while fila:
            custo_atual, atual = heapq.heappop(fila)

            if atual in visitados:
                continue
            visitados.add(atual)

            if atual == destino:
                return custo_atual

            for vizinho, tempo in self.nos[atual].items():
                if vizinho not in visitados:
                    novo_custo = custo_atual + tempo
                    if novo_custo < distancias[vizinho]:
                        distancias[vizinho] = novo_custo
                        heapq.heappush(fila, (novo_custo, vizinho))
        
        return 0  # Se o destino não for alcançável