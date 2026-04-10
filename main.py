from models.evento import Evento
from services.capturador import Capturador


def main():
    capturador = Capturador()

    evento = Evento.criar(
        usuario="Sara",
        contexto="Brasil",
        acao="Login no sistema",
        tela="Tela de login",
        sequencia=1
    )

    capturador.salvar(evento)

    print("Eventos registrados:")
    for e in capturador.listar():
        print(e)


if __name__ == "__main__":
    main()