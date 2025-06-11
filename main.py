#Arquivo principal, interage com o usuário
from src.grafo import Grafo
from src.foco import Foco
from src.posto import Posto
from src.missao import Missao

def main():
    grafo = Grafo()  # Cria o grafo que representará conexões entre focos e postos
    postos = [] # Lista de nossos postos de bombeiros
    focos = [] # Lista de nossos focos de incêndio

    # Entrada do número de focos e de postos
    print("Digite o numero de focos de incêndio e o numero de postos brigadistas separados por espaço:")
    n_focos, n_postos = map(int, input().split())
    
    # Entrada da capacidade de cada posto
    print("Digite a capacidade de combate ao fogo (km^2/h) de cada posto brigadista separadas por espaço: ")
    capacidades = list(map(float, input().split()))
    i = 1
    while i <= n_postos:
        posto = Posto(f"p{i}", capacidades[i-1])
        postos.append(posto)
        i += 1
    
    # Entrada das áreas iniciais dos focos
    print("Digite a área inicial (km^2) de cada foco de incêncdio separadas por espaço:")
    areas_iniciais = list(map(float, input().split()))
    
    # Entrada dos fatores de crescimento dos focos
    print("Digite o fator de crescimento de cada foco de incêncio (multiplicador aplicado ao fim de cada dia) separados por espaço:")
    alphas = list(map(float, input().split()))
    
    # Aloca os focos de incêndio
    i = 1
    while i <= n_focos:
        foco = Foco(f'f{i}', areas_iniciais[i-1], alphas[i-1])
        focos.append(foco)
        i += 1

    # Adiciona os nós ao grafo
    focos_e_postos = focos + postos
    for no in focos_e_postos:
        grafo.adicionar_no(no)

    # Adiciona as arestas com as distâncias (tempos) entre todos os pares
    for i in focos_e_postos:
        pares = [f'{i.id}-{j.id}' for j in focos_e_postos]
        texto_pares = ', '.join(pares)
        print(f'Digite as distâncias (tempo em horas de chegada) entre {texto_pares}, separadas por espaço:')
        
        linha_distancias = list(map(float, input().split()))
        for n, j in enumerate(focos_e_postos):
            grafo.adicionar_aresta(i, j, linha_distancias[n])
    
main()
