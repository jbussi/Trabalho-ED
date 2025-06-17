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
- **heapq** — Biblioteca padrão do Python, para cálculo de menor distância entre dois pontos.
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
## 📦 Sobre a Biblioteca do Projeto

Para facilitar o desenvolvimento, distribuição e reutilização, o projeto está organizado como uma biblioteca Python instalável, com a pasta `src` contendo todo o código-fonte.

### O que isso significa?

- **Modularidade e Organização:** Todo código está dentro do diretório `src`, o que ajuda a manter o projeto organizado e claro, especialmente para projetos maiores.

- **Pacote Instalável:** Com o arquivo `pyproject.toml` configurado, o projeto pode ser instalado localmente usando ferramentas como `pip install -e .` ou até mesmo distribuído para repositórios públicos (ex: PyPI).

- **Gerenciamento de Dependências:** O arquivo `pyproject.toml` define quais pacotes externos seu projeto precisa, além de informações essenciais como nome, versão, autores, etc.

- **Importação Simples:** Depois de instalado, você pode importar seus módulos em outros projetos ou scripts simplesmente usando `from src import grafo` ou similar, sem precisar se preocupar com o caminho relativo.

### Sobre o arquivo `pyproject.toml`

Este arquivo é um padrão moderno para configuração de projetos Python, que substitui (ou complementa) arquivos antigos como `setup.py` e `setup.cfg`. Ele contém:

- **Metadados do projeto:** Nome, versão, descrição, autores, versão mínima do Python, etc.
- **Dependências:** Pacotes externos que seu projeto necessita (deixando claro para quem instalar o pacote o que precisa ser instalado).
- **Configuração do sistema de build:** Define que o projeto usa `setuptools` e `wheel` para construir o pacote.
- **Pacotes incluídos:** Aqui, configuramos para incluir todo código dentro da pasta `src`.

## ✅ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Execute o arquivo `main.py`.
3. Escolha entre inserir os dados de entrada manualmente ou via arquivo (`.in`)
4. Insira o arquivo `.in` dentro da pasta \entradas e insira o nome do arquivo (caso escolher a entrada via arquivo `.in`)
5. Escolha o nome do arquivo .out (ele será gerado na pasta \saidas)
6. Execute o programa novamente ou saia escolhendo a opção sair

## 📄 Formato do Arquivo `.in`

O arquivo `.in` contém os dados de entrada utilizados pelo programa. Ele deve seguir o seguinte formato:

Linha 1: número de focos de incêndio (F) e número de postos de brigadistas (B)
Linha 2: capacidade de combate ao fogo de cada posto brigadista por hora (B valores)
Linha 3: área inicial de cada foco de incêndio (F valores)
Linha 4: fator de crescimento diário de cada foco de incêndio (F valores)
Linhas seguintes: matriz de distâncias entre os nós do grafo (F + B linhas, com F + B valores cada)

> ℹ️ A matriz de distâncias representa as conexões entre focos e postos. As F primeiras linhas/colunas correspondem aos focos, e as B últimas, aos postos.

#### 🧾 Exemplo de entrada `.in`:

```in
4 3
10 15 12
100 80 120 90
1.1 1.2 1.05 1.3
0 5 7 9 10 12 15
5 0 6 8 11 14 17
7 6 0 4 13 16 19
9 8 4 0 14 18 20
10 11 13 14 0 3 5
12 14 16 18 3 0 4
15 17 19 20 5 4 0
```

   
## Participantes:
- Antonio Augusto dos Santos Daneze    n° USP: 14558993
- André dos Santos Porta    n° USP: 15674171
- Diego Deliberalli Reis    n° USP: 15574238
- João Paulo Bussi          n° USP: 15495612
- Patrick Neme Mesquita     n° USP: 6904833

