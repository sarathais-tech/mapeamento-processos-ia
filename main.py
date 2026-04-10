from models.evento import Evento
from services.capturador import Capturador


def main():
    capturador = Capturador()

    evento1 = Evento.criar(
        usuario="Sara",
        contexto="Brasil",
        acao="Acessar sistema",
        tela="Tela inicial",
        sequencia=1
    )

    evento2 = Evento.criar(
        usuario="Sara",
        contexto="Brasil",
        acao="Realizar login",
        tela="Tela de login",
        sequencia=2
    )

    capturador.salvar(evento1)
    capturador.salvar(evento2)

    print("Eventos registrados:")
    for evento in capturador.listar():
        print(evento)


if __name__ == "__main__":
    main()