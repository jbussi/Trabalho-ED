import math
class Score:
    def __init__(self, total_postos, efetividade_minima=1.0, beta=1.0):
        
        self.total_postos = total_postos
        self.efetividade_minima = efetividade_minima
        self.beta = beta       
        
    
    def retornar_score(self, alpha, area, distancia, capacidade, tempo_disponivel):
        if area == 0:
            return float('-inf') 
        if distancia == 0 or distancia >= tempo_disponivel:
            return float('-inf')
        
        tempo_efetivo = tempo_disponivel - distancia
        efetividade = tempo_efetivo * capacidade
        if efetividade < self.efetividade_minima:
            return float('-inf')
        
        urgencia = math.log(area + 1) * (alpha - 1)
        penalizador_distancia = (1 - (distancia / tempo_disponivel)) ** self.beta 
        score = efetividade * urgencia * penalizador_distancia

        return score
        