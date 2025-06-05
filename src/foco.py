#Classe foco de incêndio e suas funções
class Foco:
    def __init__(self, id: str, area_inicial: float, alpha: float):
        self.id = id
        self.area = area_inicial
        self.alpha = alpha
        self.extinto = False
        self.data_extincao = None
        self.historico_combate = {}

    def sofrer_combate(self, dia: int, posto_id: str, tempo: float, recursos: float):
        if self.extinto:
            return

        if dia not in self.historico_combate:
            self.historico_combate[dia] = {}
        if posto_id not in self.historico_combate[dia]:
            self.historico_combate[dia][posto_id] = {'horas': 0, 'recursos': 0}

        self.historico_combate[dia][posto_id]['horas'] += tempo
        self.historico_combate[dia][posto_id]['recursos'] += recursos

        # Combate
        self.area = max(0, self.area - tempo * recursos)

        if self.area == 0 and not self.extinto:
            self.extinto = True
            self.data_extincao = dia

    def crescer_fogo(self):
        self.area = self.alpha * self.area