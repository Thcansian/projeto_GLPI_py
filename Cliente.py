from usuario import Usuario

class Cliente(Usuario):

    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.__chamados = []

    def adicionar_chamado(self, chamado):
        self.__chamados.append(chamado)

    @property
    def chamados(self):
        return self.__chamados