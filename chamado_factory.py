from chamado_suporte import ChamadoSuporte
from chamado_financeiro import ChamadoFinanceiro
from chamado_comercial import ChamadoComercial

class ChamadoFactory:

    @staticmethod
    def criar_chamado(mensagem):

        texto = mensagem.lower()

        if "internet" in texto:
            return ChamadoSuporte(
                "Problema de Internet",
                mensagem
            )

        elif "boleto" in texto:
            return ChamadoFinanceiro(
                "Problema Financeiro",
                mensagem
            )

        else:
            return ChamadoComercial(
                "Contato Comercial",
                mensagem
            )