import math
from .foco import Foco
from .posto import Posto
from .score import Score
from .grafo import Grafo
from .missao import Missao 

def simular_combate(focos: list[Foco], postos: list[Posto], grafo: Grafo, tempo_disponivel_diario: int, num_dias: int):
    score_calculator = Score(total_postos=len(postos))

    # Usaremos uma lista para acumular as linhas do relatório
    relatorio_linhas = []

    # Dicionário para armazenar o dia de extinção de cada foco
    focos_extintos_data = {}

    for dia in range(1, num_dias + 1):
        relatorio_linhas.append(f"\n--- Dia {dia} ---")
        focos_ativos = [f for f in focos if not f.extinto]

        if not focos_ativos:
            relatorio_linhas.append("Todos os focos foram extintos. Simulacao encerrada.")
            break

        # Resetar horas e capacidade disponíveis dos postos para o dia
        for posto in postos:
            posto.encerrar_dia()

        # Criar um objeto Missao para cada posto no início do dia
        # Este objeto Missao acumulará todas as alocações do posto para o dia
        missoes_do_dia = {posto.id: Missao(posto.id, posto.capacidade, dia) for posto in postos}

        # Loop de alocação dentro do dia, permitindo que postos atendam múltiplos focos
        # e que múltiplos postos atendam o mesmo foco.
        # Este loop continua enquanto houver focos ativos e postos com tempo disponível.
        while True:
            melhor_alocacao = None # (score, posto, foco, distancia, tempo_combate_sugerido)
            maior_score_global = -float('inf')

            for posto in postos:
                # Se o posto não tem mais horas disponíveis para novas viagens ou combate, pule
                # A verificação de tempo é feita considerando o tempo total da missão atual do posto
                # e o tempo que seria adicionado por uma nova alocação.
                current_mission_time = missoes_do_dia[posto.id].tempo_total(grafo)
                if current_mission_time >= tempo_disponivel_diario: # posto.horas_disponiveis é 12 no início do dia
                    continue

                # O local atual do posto para cálculo de distância é o último foco alocado na missão,
                # ou a base do posto se for a primeira alocação.
                local_atual_posto = posto.id
                if missoes_do_dia[posto.id].alocacoes:
                    # Pega o ID do último foco alocado na missão para calcular a próxima distância
                    # Isso assume que a ordem de alocação é a ordem de visita.
                    local_atual_posto = list(missoes_do_dia[posto.id].alocacoes.keys())[-1]

                for foco in focos_ativos:
                    # Calcular a distância do local atual do posto até o foco
                    distancia_deslocamento = grafo.custo(local_atual_posto, foco.id)
                    
                    # Tempo que o posto teria disponível para combate APÓS o deslocamento
                    tempo_disponivel_para_combate = tempo_disponivel_diario - (current_mission_time + distancia_deslocamento)

                    if tempo_disponivel_para_combate <= 0: # Não há tempo útil para combate
                        continue

                    # Sugerir um tempo de combate para esta alocação (e.g., 1 hora, ou o que restar)
                    # Isso é uma heurística para dividir o tempo.
                    tempo_combate_sugerido = min(tempo_disponivel_para_combate, 2) # Aloca no máximo 2 horas por vez
                    if tempo_combate_sugerido <= 0: # Garante que há tempo para combater
                        continue

                    # Calcular o score para esta potencial alocação
                    current_score = score_calculator.retornar_score(
                        alpha=foco.alpha,
                        area=foco.area,
                        distancia=distancia_deslocamento,
                        capacidade=posto.capacidade, # Capacidade total do posto, a Missao vai dividir
                        tempo_disponivel=tempo_disponivel_para_combate # Tempo que o posto pode dedicar a este foco
                    )

                    if current_score > maior_score_global:
                        maior_score_global = current_score
                        melhor_alocacao = (current_score, posto, foco, distancia_deslocamento, tempo_combate_sugerido)
            
            # Se não encontrou nenhuma alocação viável para nenhum posto, saia do loop de alocação do dia
            if melhor_alocacao is None or maior_score_global <= -float('inf'):
                break

            # Realizar a melhor alocação encontrada
            score_alocado, posto_alocado, foco_alocado, distancia_alocada, tempo_combate_alocado = melhor_alocacao
            
            # Adicionar esta alocação à missão do posto
            missoes_do_dia[posto_alocado.id].adicionar_alocacao(foco_alocado, tempo_combate_alocado)
            
            relatorio_linhas.append(f"Dia {dia}: Posto {posto_alocado.id} alocado ao Foco {foco_alocado.id} por {tempo_combate_alocado:.2f}h (dist: {distancia_alocada:.2f}h).")
            
            # Atualizar focos_ativos se um foco foi extinto por alocações anteriores no mesmo dia (improvável, mas para segurança)
            # Ou, mais importante, se um foco foi extinto em dias anteriores e ainda está na lista.
            focos_ativos = [f for f in focos_ativos if not f.extinto]

        # Executar todas as missões planejadas para o dia
        for posto in postos:
            missao_posto = missoes_do_dia[posto.id]
            if missao_posto.alocacoes: # Só executa se houver alocações na missão
                posto.executar_missao(missao_posto, grafo)

        # Crescimento dos focos e verificação de extinção ao final do dia
        for foco in focos:
            if not foco.extinto:
                foco.crescer_fogo()
                if foco.area <= 0:
                    foco.extinto = True
                    foco.data_extincao = dia
                    focos_extintos_data[foco.id] = dia
                    relatorio_linhas.append(f"Foco {foco.id} extinto no Dia {dia}!")
                else:
                    relatorio_linhas.append(f"Foco {foco.id} cresceu para {foco.area:.2f} km^2")

        # Relatório diário
        relatorio_linhas.append("\nEstado dos Focos ao final do dia:")
        for foco in focos:
            status = "Extinto" if foco.extinto else f"{foco.area:.2f} km^2"
            relatorio_linhas.append(f"Foco {foco.id}: {status}")

    # Relatório final após a simulação
    relatorio_linhas.append("\n--- Relatorio Final ---")
    todos_extintos = True
    tempo_total_simulacao = 0

    for foco in focos:
        if foco.extinto:
            relatorio_linhas.append(f"Foco {foco.id} extinto no Dia {foco.data_extincao}.")
            if foco.data_extincao > tempo_total_simulacao:
                tempo_total_simulacao = foco.data_extincao
        else:
            todos_extintos = False
            relatorio_linhas.append(f"Foco {foco.id} nao extinto. Area restante: {foco.area:.2f} km^2.")
    
    if todos_extintos:
        relatorio_linhas.append(f"Todos os focos foram extintos em {tempo_total_simulacao} dias.")
    else:
        relatorio_linhas.append("Nao foi possivel extinguir todos os focos com os recursos disponiveis.")

    return '\n'.join(relatorio_linhas)


