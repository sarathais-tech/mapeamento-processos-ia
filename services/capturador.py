import json
from models.evento import Evento


class Capturador:

    def __init__(self):
        self.caminho = "data/eventos.json"

    def salvar(self, evento: Evento):
        try:
            with open(self.caminho, "r") as f:
                dados = json.load(f)
        except:
            dados = []

        dados.append(evento.__dict__)

        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=4)

    def listar(self):
        try:
            with open(self.caminho, "r") as f:
                return json.load(f)
        except:
            return []