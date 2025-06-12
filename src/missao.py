#Missão realizada por cada posto (para possibilitar a divisão da capacidade do posto)
from .foco import Foco
from .grafo import Grafo

class Missao:
    def __init__(self, posto_id: str, capacidade: float, dia: int):
        self.posto_id = posto_id
        self.dia = dia
        self.capacidade = capacidade
        self.alocacoes = {} # Stores {foco_id: {'foco_obj': Foco, 'tempo': float}}
    
    # Aloca o foco de incêncio a certo posto
    def adicionar_alocacao(self, foco: Foco, tempo: float):
        foco_id = foco.id
        if foco_id not in self.alocacoes:
            self.alocacoes[foco_id] = {'foco_obj': foco, 'tempo': 0}
        self.alocacoes[foco_id]['tempo'] += tempo
    
    # O posto combate o foco de incêndio alocado
    def executar(self):
        total_tempo_alocado = sum(dados['tempo'] for dados in self.alocacoes.values())
        if total_tempo_alocado == 0:
            return

        for foco_id, dados in self.alocacoes.items():
            foco_obj: Foco = dados['foco_obj']
            tempo_alocado_foco = dados['tempo']
            recursos_alocados_foco = (tempo_alocado_foco / total_tempo_alocado) * self.capacidade

            foco_obj.sofrer_combate(
                dia = self.dia,
                posto_id = self.posto_id,
                tempo = tempo_alocado_foco,
                recursos = recursos_alocados_foco
            )
    
    #Contabiliza o tempo total gasto, para não exceder as 12 horas disponíveis por dia
    def tempo_total(self, grafo: Grafo):
        tempo_total = 0
        local_atual = self.posto_id

        for foco_id, dados in self.alocacoes.items():
            # Deslocamento do local atual até o próximo foco
            tempo_deslocamento = grafo.custo(local_atual, foco_id)

            # Tempo de combate
            tempo_combate = dados['tempo']

            # Soma deslocamento + combate
            tempo_total += tempo_deslocamento + tempo_combate

            # Atualiza local atual
            local_atual = foco_id

        return tempo_total