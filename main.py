import minerador
import bot
import json


def executar_sistema():

    print('executando minerador')
    minerador.rodar()

    print('executando bot')
    bot.rodar()


if (__name__ == "__main__"):
    executar_sistema()