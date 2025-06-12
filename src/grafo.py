import heapq
class Grafo:
    def __init__(self):
        self.nos = {}
    
    def adicionar_no(self, no_id: str):
        if no_id not in self.nos:
            self.nos[no_id] = {}

    def adicionar_aresta(self, origem_id: str, destino_id: str, tempo: float):
        # Garante que os nós existem antes de adicionar a aresta
        self.adicionar_no(origem_id)
        self.adicionar_no(destino_id)
        self.nos[origem_id][destino_id] = tempo
        self.nos[destino_id][origem_id] = tempo # Grafo não direcionado
    
    def custo(self, origem_id: str, destino_id: str):
        # Verifica se os nós existem no grafo
        if origem_id not in self.nos or destino_id not in self.nos:
            return float("inf") # Retorna infinito se um dos nós não existe

        visitados = set()
        # (custo acumulado, nó atual_id)
        fila = [(0, origem_id)]  
        distancias = {no_id: float("inf") for no_id in self.nos}
        distancias[origem_id] = 0

        while fila:
            custo_atual, atual_id = heapq.heappop(fila)

            if atual_id in visitados:
                continue
            visitados.add(atual_id)

            if atual_id == destino_id:
                return custo_atual

            for vizinho_id, tempo in self.nos[atual_id].items():
                if vizinho_id not in visitados:
                    novo_custo = custo_atual + tempo
                    if novo_custo < distancias[vizinho_id]:
                        distancias[vizinho_id] = novo_custo
                        heapq.heappush(fila, (novo_custo, vizinho_id))
        
        return float("inf")  # Se o destino não for alcançável