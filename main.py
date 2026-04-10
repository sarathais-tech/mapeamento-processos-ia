from models.evento import Evento
from services.capturador import Capturador
from services.processador import Processador


def main():
    capturador = Capturador()

    # Criando eventos de exemplo
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

    evento3 = Evento.criar(
        usuario="Sara",
        contexto="Brasil",
        acao="Preencher formulário",
        tela="Módulo de cadastro",
        sequencia=3
    )

    evento4 = Evento.criar(
        usuario="Sara",
        contexto="Brasil",
        acao="Salvar dados",
        tela="Módulo de cadastro",
        sequencia=4
    )

    capturador.salvar(evento1)
    capturador.salvar(evento2)
    capturador.salvar(evento3)
    capturador.salvar(evento4)

    eventos = capturador.listar()

    processador = Processador(eventos)

    print("\nEventos ordenados:")
    for evento in processador.ordenar_eventos():
        print(evento)

    print("\nFluxo reconstruído:")
    print(processador.reconstruir_fluxo())

    print("\nDescrição textual do processo:")
    print(processador.gerar_descricao_textual())


if __name__ == "__main__":
    main()