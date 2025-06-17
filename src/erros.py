class ErroEntradaManual(Exception):
    pass
class ErroLeituraEntrada(Exception):
    #Exceção para erros de leitura na entrada
    pass

class FormatoArquivoInvalido(ErroLeituraEntrada):
    def __init__(self, mensagem = "Formato do arquivo de entrada inválido.", linha = None):
        super().__init__(mensagem)
        self.linha = linha

class ErroGrafo(Exception):
    pass

class NoNaoEncontrado(ErroGrafo):
    def __init__(self, mensagem = "Nó não encontrado no grafo.", no_id = None):
        super().__init__(mensagem)
        self.no_id = no_id

class ArestaInvalida(ErroGrafo):
    def __init__(self, mensagem = "Aresta inválida.", origem = None, destino = None, tempo = None):
        super().__init__(mensagem)
        self.origem = origem
        self.destino = destino
        self.tempo = tempo

class ParametroInvalido(Exception):
    def __init__(self, mensagem = "Parâmetro inválido.", parametro = None, valor = None):
        super().__init__(mensagem)
        self.parametro = parametro
        self.valor = valor