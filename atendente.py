from usuario import Usuario

class Atendente(Usuario):

    def __init__(self, nome, email, setor):
        super().__init__(nome, email)
        self.__setor = setor

    @property
    def setor(self):
        return self.__setor