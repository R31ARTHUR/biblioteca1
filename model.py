
class Livro:
    """
        Uma classe Livro com atributos: id, titulo, autor, categoria, editora, edicao, ano, indicacao
    """
    def __init__(
            self,
            id,
            titulo,
            categoria,
            editora,
            edicao,
            ano,
            indicacao):
        self._id = id
        self._titulo = titulo
        self._categoria = categoria
        self._editora = editora
        self._edicao = edicao
        self._ano = ano
        self._indicacao = indicacao
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, editora):
        self._editora = editora

    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, edicao):
        self._edicao = edicao

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def indicacao(self):
        return self._indicacao

    @indicacao.setter
    def indicacao(self, indicacao):
        self._indicacao = indicacao
