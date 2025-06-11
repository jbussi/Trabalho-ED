#Classe posto e seus métodos
# Importa os dados da missão e as distâncias estabelecidas pelo grafo
from .missao import Missao
from .grafo import Grafo

class Posto:
    # Cria os postos
    def __init__(self, id: str, capacidade: float):
        self.id = id
        self.capacidade = capacidade
        self.capacidade_disponivel = self.capacidade
        self.horas_disponiveis = 12
        self.missoes = []
    
    # Cria as missões para cada posto de bombeiros
    def criar_missao(self, capacidade: float, dia: int):
        if capacidade > self.capacidade_disponivel:
            return #Erro
        
        missao = Missao(self.id, capacidade, dia)
        self.missoes.append(missao)
        self.capacidade_disponivel -= capacidade
        return missao
    
    # Garante que a missão vai ser executada em 12 horas ou menos
    def executar_missao(self, missao: Missao, grafo: Grafo):
        tempo = missao.tempo_total(grafo)
        if tempo > self.horas_disponiveis:
            return #Erro
        
        missao.executar()
        self.horas_disponiveis -= tempo
    
    # Reseta a capacidade e horas disponíveis ao final do dia
    def encerrar_dia(self):
        self.capacidade_disponivel = self.capacidade
        self.horas_disponiveis = 12