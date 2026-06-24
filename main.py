from Cliente import Cliente
from chamado_factory import ChamadoFactory
from sistema_chamados import SistemaChamados

cliente = Cliente(
    "Thomas",
    "thomas@email.com"
)

mensagem = input(
    "Digite sua solicitação: "
)

chamado = ChamadoFactory.criar_chamado(
    mensagem
)

cliente.adicionar_chamado(chamado)

sistema = SistemaChamados()

sistema.adicionar_chamado(chamado)

print("\nChamado criado!")

print(chamado.exibir_dados())

chamado.iniciar()

print("\nAtendimento iniciado.")

chamado.resolver()

chamado.finalizar()

print("\nChamado finalizado.")

sistema.listar_chamados()