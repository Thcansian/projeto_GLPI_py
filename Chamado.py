from Status import StatusChamado

class Chamado:

    def __init__(self, titulo, descricao):
        self._titulo = titulo
        self._descricao = descricao
        self._status = StatusChamado.ABERTO

    @property
    def titulo(self):
        return self._titulo

    @property
    def descricao(self):
        return self._descricao

    @property
    def status(self):
        return self._status

    def iniciar(self):
        self._status = StatusChamado.EM_ATENDIMENTO

    def finalizar(self):
        self._status = StatusChamado.FINALIZADO

    def resolver(self):
        raise NotImplementedError()

    def exibir_dados(self):
        return (
            f"Título: {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Status: {self.status.name}"
        )