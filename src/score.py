import math

# Calcula a prioridade de combate dos focos de incêndio, ajudando na alocação de focos para os postos
class Score:
    def __init__(self, total_postos, efetividade_minima=1.0, beta=1.0):
        self.total_postos = total_postos
        self.efetividade_minima = efetividade_minima
        self.beta = beta       
    
    def retornar_score(self, alpha, area, distancia, capacidade, tempo_disponivel):
        if area <= 0:  # Foco já extinto ou sem área
            return float('-inf') 
        
        # Se o tempo de deslocamento for maior ou igual ao tempo disponível, não há tempo para combate
        if distancia >= tempo_disponivel:
            return float('-inf')
        
        tempo_efetivo_combate = tempo_disponivel - distancia
        
        # Capacidade de combate que o posto pode aplicar neste foco
        capacidade_aplicavel = capacidade * tempo_efetivo_combate
        
        # Penaliza focos que o posto não consegue combater efetivamente
        if capacidade_aplicavel < self.efetividade_minima:
            return float('-inf')
        
        # Urgência: Combina o tamanho do foco com sua taxa de crescimento
        # Logaritmo para suavizar o impacto da área, e (alpha - 1) para dar peso ao crescimento
        urgencia = math.log(area + 1) * (alpha - 1.0)  # alpha - 1.0 para evitar log(0) se alpha for 1
        if urgencia < 0: # Se alpha for 1, urgencia pode ser 0 ou negativa, o que não faz sentido para um foco ativo
            urgencia = 0.1 # Valor mínimo para focos que não crescem, mas ainda precisam ser combatidos

        # Potencial de extinção: Quão rápido este posto pode reduzir a área do foco
        # Quanto maior a capacidade aplicável e menor a área, maior o potencial
        potencial_extincao = capacidade_aplicavel / (area + 1) # Adiciona 1 para evitar divisão por zero

        # Penalizador de distância: Quanto mais longe, menos atraente
        # Usa uma função exponencial para penalizar mais fortemente distâncias maiores
        penalizador_distancia = math.exp(-self.beta * distancia / tempo_disponivel)

        # Score final: Combinação ponderada dos fatores
        # Aumenta a importância da urgência e do potencial de extinção
        score = (urgencia * 2 + potencial_extincao * 3) * penalizador_distancia

        return score


