from src import (
    Grafo, Foco, Posto, simular_combate,
    ErroLeituraEntrada, FormatoArquivoInvalido,
    ErroGrafo, NoNaoEncontrado, ArestaInvalida, 
    ParametroInvalido, ErroEntradaManual
)
import os
## Esse é o arquivo principal, o qual vai receber todos os dados de entrada e executar a simulação do incêndio ##

# Função para ler os dados de entrada de um arquivo .in
def ler_dados_entrada(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        # Linha 1: n_focos n_postos
        try:
            n_focos, n_postos = map(int, f.readline().split())
            if n_focos <= 0 or n_postos <= 0:
                raise ParametroInvalido("Os números devem ser inteiros positivos. Verifique a linha 1 do arquivo")
        except ValueError:
            raise FormatoArquivoInvalido("Esperado dois números inteiros na primeira linha (n_focos n_postos)")
        
        # Linha 2: capacidades dos postos
        try:
            capacidades = list(map(float, f.readline().split()))
            postos = [Posto(f"b{i+1}", capacidades[i]) for i in range(n_postos)]
            for capacidade in capacidades:
                if capacidade <= 0:
                    raise ParametroInvalido("A capacidade deve ser um decimal positivo. Verifique a linha 2 do arquivo")
        except ValueError:
            raise FormatoArquivoInvalido(f"Esperado {n_postos} números decimais na segunda linha (capacidades de combate dos postos).")
        
        # Linha 3: áreas iniciais dos focos
        try:
            areas_iniciais = list(map(float, f.readline().split()))
            for area in areas_iniciais:
                if area <= 0:
                    raise ParametroInvalido("A área deve ser um decimal positivo. Verifique a linha 3 do arquivo.")
        # Linha 4: alphas dos focos
            alphas = list(map(float, f.readline().split()))
            focos = [Foco(f"f{i+1}", areas_iniciais[i], alphas[i]) for i in range(n_focos)]
            for alpha in alphas:
                if alpha < 1 or alpha > 2:
                    raise ParametroInvalido("Alpha é um valor decimal entre 1 e 2. Verifique a linha 4 do arquivo.")
        except:
            raise FormatoArquivoInvalido(f"Esperado {n_focos} números decimais nas terceira e quarta linha (áreas iniciais e alphas).")

        grafo = Grafo()
        
        # Criar uma lista de todos os IDs dos nós na ordem em que aparecem na matriz de adjacência
        # Assumimos que os focos vêm primeiro, depois os postos, na ordem f1, f2..., b1, b2...
        todos_nos_ids = [foco.id for foco in focos] + [posto.id for posto in postos]

        # Adicionar todos os IDs dos nós ao grafo
        for no_id in todos_nos_ids:
            grafo.adicionar_no(no_id)

        # Ler a matriz de adjacência para adicionar as arestas
        try:
            for i in range(len(todos_nos_ids)):
                linha_distancias = list(map(float, f.readline().split()))
                for j in range(len(todos_nos_ids)):
                    # Adiciona aresta apenas se houver uma distância positiva
                    # E se não for a distância de um nó para ele mesmo (que deve ser 0 no .in)
                    if linha_distancias[j] > 0:
                        grafo.adicionar_aresta(todos_nos_ids[i], todos_nos_ids[j], linha_distancias[j])
        except ValueError:
            raise FormatoArquivoInvalido("A matriz de distâncias está com formato incorreto. Verifique o arquivo de entrada.")
    return focos, postos, grafo

# Função para ler os dados de entrada de um usuário manualmente
def entrada_manual():
    try:
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
            foco = Foco(f"f{i}", areas_iniciais[i-1], alphas[i-1])
            focos.append(foco)
            i += 1

        # Adiciona os nós ao grafo
        focos_e_postos = focos + postos
        for no in focos_e_postos:
            grafo.adicionar_no(no.id) # Passar o ID do nó

        # Adiciona as arestas com as distâncias (tempos) entre todos os pares
        for i_obj in focos_e_postos:
            pares = [f'{i_obj.id}-{j_obj.id}' for j_obj in focos_e_postos]
            texto_pares = ', '.join(pares)
            print(f'Digite as distâncias (tempo em horas de chegada) entre {texto_pares}, separadas por espaço:')
            
            linha_distancias = list(map(float, input().split()))
            for n, j_obj in enumerate(focos_e_postos):
                grafo.adicionar_aresta(i_obj.id, j_obj.id, linha_distancias[n]) # Passar os IDs dos nós
        return focos, postos, grafo
    except Exception:
        raise ErroEntradaManual("Erro na entrada manual dos dados. Tente novamente!")


def main():
    tempo_disponivel_diario = 12 # Horas
    num_dias_simulacao = 100 # Um número razoável de dias para a simulação

    while True:
        print('Escolha uma das opções abaixo:')
        print('1. Inserir entrada manualmente')
        print('2. Ler entrada por arquivo .in')
        print('3. Sair')
        opcao = input('')
        
        if opcao == '1':
            nome_saida = input("Digite o nome do arquivo de saída .out: ").strip()
            caminho_saida = os.path.join("saidas", nome_saida)
            focos, postos, grafo = entrada_manual()
            resultado = simular_combate(focos, postos, grafo, tempo_disponivel_diario, num_dias_simulacao)

            with open(caminho_saida, "w") as f_out:
                f_out.write(resultado)

            
            print(f"\nSimulação concluída. Resultados salvos em: {caminho_saida}")


        elif opcao == '2':
            nome_entrada = input("Digite o nome do arquivo .in: ").strip()
            nome_saida = input("Digite o nome do arquivo de saída .out: ").strip()
            
            # Correção: Extrair apenas o nome base do arquivo e juntar com o diretório 'entradas'
            base_nome_entrada = os.path.basename(nome_entrada)
            caminho_entrada = os.path.join("entradas", base_nome_entrada) 
            caminho_saida = os.path.join("saidas", nome_saida)

            try:
                focos, postos, grafo = ler_dados_entrada(caminho_entrada)
                resultado = simular_combate(focos, postos, grafo, tempo_disponivel_diario, num_dias_simulacao)
                with open(caminho_saida, "w") as f_out:
                    f_out.write(resultado)

                print(f"\nSimulação concluída. Resultados salvos em: {caminho_saida}")
            except FileNotFoundError:
                print(f"Arquivo de entrada '{caminho_entrada}' não encontrado. Verifique o caminho e tente novamente.")
            except Exception as e:
                print(f"Ocorreu um erro ao processar o arquivo de entrada: {e}")
        
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


main()