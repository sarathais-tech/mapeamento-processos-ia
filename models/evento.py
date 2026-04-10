from dataclasses import dataclass
from datetime import datetime


@dataclass
class Evento:
    usuario: str
    contexto: str
    acao: str
    data_hora: str
    tela: str
    sequencia: int

    @staticmethod
    def criar(usuario, contexto, acao, tela, sequencia):
        return Evento(
            usuario=usuario,
            contexto=contexto,
            acao=acao,
            data_hora=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            tela=tela,
            sequencia=sequencia
        )