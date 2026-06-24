class SistemaChamados:

    __instancia = None

    def __new__(cls):

        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
            cls.__instancia.chamados = []

        return cls.__instancia

    def adicionar_chamado(self, chamado):
        self.chamados.append(chamado)

    def listar_chamados(self):

        print("\n===== CHAMADOS =====")

        for chamado in self.chamados:
            print(
                f"{chamado.titulo} - {chamado.status.name}"
            )