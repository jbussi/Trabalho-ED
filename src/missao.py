#Missão realizada por cada posto (para possibilitar a divisão da capacidade do posto)
from .foco import Foco
from .grafo import Grafo

class Missao:
    def __init__(self, posto_id: str, capacidade: float, dia: int):
        self.posto_id = posto_id
        self.dia = dia
        self.capacidade = capacidade
        self.alocacoes = {}
    
    def adicionar_alocacao(self, foco_id: str, tempo: float):
        if foco_id not in self.alocacoes:
            self.alocacoes[foco_id] = {'tempo': 0, 'recursos': 0}
        self.alocacoes[foco_id]['tempo'] += tempo
        self.alocacoes[foco_id]['capacidade'] += self.capacidade
    
    def executar(self):
        for foco_id, dados in self.alocacoes.items():
            foco: Foco = self.alocacoes[foco_id]
            foco.sofrer_combate(
                dia = self.dia,
                posto_id = self.posto_id,
                tempo = dados['tempo'],
                recursos = dados['recursos']
            )
    
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

        # Volta para o posto
        tempo_volta = grafo.adjacencias[local_atual][self.posto_id]
        tempo_total += tempo_volta

        return tempo_total