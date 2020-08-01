import telepot
import json
# import funcao as func
import os
from time import sleep


def rodar():
    bot = telepot.Bot("1044300292:AAFwvSV7g50-8-lpNxYqCdAXHJsLQCrjPZs")
    chat_id = -1001383791263

    if os.path.exists('vagas.json'):

        a = open('vagas.json', 'r')
        vagas_geradas = json.loads(a.read())
        a.close()

        # filtragem para não pegar vagas repetidas
        arquivo_tmp = open('ultima_vaga_bot.tmp', 'r')
        ultima_vaga_bot = arquivo_tmp.read()
        arquivo_tmp.close()

        ultima_vaga_site = list(vagas_geradas[0].keys())[0]

        if (ultima_vaga_site != ultima_vaga_bot):
            lista_chaves = []

            for i in range(len(vagas_geradas)):
                chave = list(vagas_geradas[i].keys())[0]
                lista_chaves.append(chave)

            for i in range(len(vagas_geradas) - 1, -1, -1):
                print(i)
                vaga = (vagas_geradas[i][lista_chaves[i]])
                mensagem = "*{0}*\n \n_{1}_ \n\n{2}\n\n{3}\n\nEmpresa: {4}\n\nContratação: {5}".format(vaga[1], vaga[0],
                                                                                                       lista_chaves[i],
                                                                                                       vaga[2], vaga[3],
                                                                                                       vaga[4])

                bot.sendMessage(chat_id,mensagem,parse_mode="markdown")

            sleep(1)

            arquivo_tmp = open('ultima_vaga_bot.tmp', 'w')
            arquivo_tmp.write(list(vagas_geradas[i].keys())[0])
            arquivo_tmp.close()

        else:
            print('não há novas vagas')

        # apaga o arquivo de vagas.json
        os.remove('vagas.json')

if (__name__ == "__main__"):
    rodar()