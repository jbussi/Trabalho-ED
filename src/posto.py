#Classe posto e suas funções

from .missao import Missao
from .grafo import Grafo
class Posto:
    def __init__(self, id: str, capacidade: float):
        self.id = id
        self.capacidade = capacidade
        self.capacidade_disponivel = self.capacidade
        self.horas_disponiveis = 12
        self.missoes = []
    
    def criar_missao(self, capacidade: float, dia: int):
        if capacidade > self.capacidade_disponivel:
            return #Erro
        
        missao = Missao(self.id, capacidade, dia)
        self.missoes.append(missao)
        self.capacidade_disponivel -= capacidade
        return missao
    
    def executar_missao(self, missao: Missao, grafo: Grafo):
        tempo = missao.tempo_total(grafo)
        if tempo > self.horas_disponiveis:
            return #Erro
        
        missao.executar()
        self.horas_disponiveis -= tempo
    
    def encerrar_dia(self):
        self.capacidade_disponivel = self.capacidade
        self.horas_disponiveis = 12