# Brigadistas em Situações de Emergência (SME0827 - Estrutura de Dados I)

Este projeto é uma implementação em Python para planejar a atuação de brigadistas em emergências causadas por incêndios em diferentes regiões, utilizando grafos para modelar o cenário e alocar recursos de maneira eficiente.

## 📌 Descrição

O objetivo do projeto é determinar uma estratégia viável para extinguir todos os focos de incêndio, considerando:
- A capacidade dos postos de brigadistas.
- A taxa de crescimento dos incêndios.
- O tempo de deslocamento entre brigadistas e focos.
- A alocação diária de recursos para combate ao fogo.

## 🔧 Tecnologias Utilizadas

- **Python 3**: Linguagem de programação utilizada para implementar a solução.
- **math**: Biblioteca de python que possui operações matemáticas comuns (no nosso caso será utilizado o logaritmo)

## 📁 Estrutura do Projeto

Optamos por uma estrutura modular para facilitar a reutilização e a manutenção do código, além de facilitar a compreensão. Cada componente do sistema é representado por um módulo separado, permitindo que as funções sejam importadas diretamente no `main.py` para execução. , e o resto do projeto segue a utiliação TAD's ensinadas durante o curso.

A estrutura de nosso código ficou assim:
- `grafo.py`: Define a classe grafo, pois a forma como escolhemos para gravar as distâncias e relações entre nós foi por meio de grafos, adicionando arestas entre nossos nós com as distâncias dadas.
- `foco.py`: Define a classe foco, onde cada foco tem uma área inicial, um fator de crescimento e um histórico de combate. Além disso, é nela que guardamos se o foco foi extinto
- `missao.py`: Define a classe missão, a qual importa `focos.py` e `grafos.py` para determinar a alocação dos focos para os postos, sendo também responsável por marcar as horas gastas e não deixá-las ultrapassar o tempo máximo de cada dia(12h) para a missão.
- `posto.py`: Define a classe posto, guardando informações inerentes, como sua capacidade de combate, e informações de missão pra cada dia
- `score.py`: Calcula a prioridade de combate dos focos de incêndio, ajudando na alocação de focos para os postos de forma eficiente, considerando características do foco, distância da brigada até ele e o potencial de extinção
- `simulacao.py`: Une todas as classes descritas, desenvolvendo um método que simula o combate aos focos de incêndio a cada dia, alocando os postos de bombeiros para os focos, calculando os scores para tal.
- `main.py`: É quem faz a interação com usuário/recebe informações do arquivo .in que serão utilizadas na simulação.

## Participantes:
- Diego Deliberalli Reis    n° USP: 15574238
- João Paulo Bussi          n° USP: 15495612
- André dos Santos Porta    n° USP: 15674171
- Patrick Neme Mesquita     n° USP: 6904833
- Antonio Augusto dos Santos Daneze    n° USP: 14558993
