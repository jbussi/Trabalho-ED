# 👨‍🚒 Brigadistas em Situações de Emergência  
**Disciplina:** SME0827 - Estrutura de Dados I  

Este projeto é uma implementação em Python que planeja a atuação de brigadistas em situações de emergência causadas por incêndios, utilizando grafos para modelar o cenário e alocar recursos de forma eficiente.

---

## 📌 Descrição

O objetivo do projeto é determinar uma estratégia viável para extinguir todos os focos de incêndio, considerando os seguintes fatores:

- A capacidade de combate dos postos de brigadistas;
- A taxa de crescimento dos focos de incêndio;
- O tempo de deslocamento entre postos e focos;
- A alocação diária de recursos, respeitando o limite de 12 horas por dia de operação.

---

## 🔧 Tecnologias Utilizadas

- **Python 3** — Linguagem de programação principal.
- **math** — Biblioteca padrão do Python, utilizada principalmente para cálculos logarítmicos.

---

## 📁 Estrutura do Projeto

A implementação segue uma estrutura modular, com cada componente funcional separado em arquivos específicos, facilitando a reutilização, manutenção e entendimento do código. O projeto foi desenvolvido com base nos TADs ensinados durante o curso.

### Estrutura de Arquivos:

- `grafo.py`:  
  Define a TAD Grafo, usada para armazenar as distâncias e conexões entre postos e focos de incêndio.

- `foco.py`:  
  Define a TAD Foco. Cada foco possui uma área inicial, um fator de crescimento, um histórico de combate e uma flag que indica se foi extinto.

- `posto.py`:  
  Define a TAD Posto, que armazena a capacidade de combate do posto e seu histórico de alocação diária.

- `missao.py`:  
  Coordena a alocação de postos para os focos, garantindo que o tempo máximo diário (12 horas) não seja ultrapassado. Importa `grafo.py` e `foco.py`.

- `score.py`:  
  Responsável por calcular a prioridade dos focos, considerando distância, crescimento e capacidade de combate, para auxiliar na alocação eficiente dos recursos.

- `simulacao.py`:  
  Integra todos os componentes, executando a simulação dia a dia, alocando postos aos focos com base nos scores calculados.

- `main.py`:  
  Ponto de entrada do programa. Realiza a leitura dos dados de entrada (.in) e inicia a simulação.

---

## ✅ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Execute o `main.py` com um arquivo de entrada no formato especificado:
   
## Participantes:
- Antonio Augusto dos Santos Daneze    n° USP: 14558993
- André dos Santos Porta    n° USP: 15674171
- Diego Deliberalli Reis    n° USP: 15574238
- João Paulo Bussi          n° USP: 15495612
- Patrick Neme Mesquita     n° USP: 6904833

