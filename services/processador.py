from typing import List, Dict


class Processador:
    def __init__(self, eventos: List[Dict]):
        self.eventos = eventos

    def ordenar_eventos(self) -> List[Dict]:
        return sorted(self.eventos, key=lambda evento: evento["sequencia"])

    def reconstruir_fluxo(self) -> List[str]:
        eventos_ordenados = self.ordenar_eventos()
        fluxo = []

        for evento in eventos_ordenados:
            fluxo.append(evento["acao"])

        return fluxo

    def gerar_descricao_textual(self) -> str:
        fluxo = self.reconstruir_fluxo()

        if not fluxo:
            return "Nenhum processo foi identificado."

        if len(fluxo) == 1:
            return f"O usuário executou a seguinte ação: {fluxo[0]}."

        descricao = "O usuário realizou as seguintes etapas do processo: "
        descricao += ", depois ".join(fluxo[:-1])
        descricao += f" e, por fim, {fluxo[-1]}."

        return descricao