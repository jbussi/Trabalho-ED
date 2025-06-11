#Missão realizada por cada posto (para possibilitar a divisão da capacidade do posto)
from .foco import Foco
from .grafo import Grafo

class Missao:
    def __init__(self, posto_id: str, capacidade: float, dia: int):
        self.posto_id = posto_id
        self.dia = dia
        self.capacidade = capacidade
        self.alocacoes = {}
    
    # Aloca o foco de incêncio a certo posto
    def adicionar_alocacao(self, foco_id: str, tempo: float):
        if foco_id not in self.alocacoes:
            self.alocacoes[foco_id] = {'tempo': 0, 'recursos': 0}
        self.alocacoes[foco_id]['tempo'] += tempo
        self.alocacoes[foco_id]['capacidade'] += self.capacidade
    
    # O posto combate o foco de incêndio alocado
    def executar(self):
        for foco_id, dados in self.alocacoes.items():
            foco: Foco = self.alocacoes[foco_id]
            foco.sofrer_combate(
                dia = self.dia,
                posto_id = self.posto_id,
                tempo = dados['tempo'],
                recursos = dados['recursos']
            )
    
    #Contabiliza o tempo total gasto, para não exceder as 12 horas disponíveis por dia
    def tempo_total(self, grafo: Grafo):
        tempo_total = 0
        local_atual = self.posto_id

        for foco_id, dados in self.alocacoes.items():
            # Deslocamento do local atual até o próximo foco
            tempo_deslocamento = grafo.adjacencias[local_atual][foco_id]

            # Tempo de combate
            tempo_combate = dados['tempo']

            # Soma deslocamento + combate
            tempo_total += tempo_deslocamento + tempo_combate

            # Atualiza local atual
            local_atual = foco_id

        return tempo_total