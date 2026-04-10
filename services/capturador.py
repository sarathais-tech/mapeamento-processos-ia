import json
from pathlib import Path
from models.evento import Evento


class Capturador:
    def __init__(self):
        self.caminho = Path("data/eventos.json")

    def salvar(self, evento: Evento):
        dados = self.listar()
        dados.append(evento.__dict__)

        with self.caminho.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def listar(self):
        if not self.caminho.exists():
            return []

        try:
            with self.caminho.open("r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return []