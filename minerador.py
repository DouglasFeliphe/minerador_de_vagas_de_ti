from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


def rodar():
    url = 'https://hipsters.jobs/jobs/?q=&l=Bras%C3%ADlia+-+Brasilia%2C+Federal+District%2C+Brazil'

    # verifica se a url esta abrindo
    def pegaPagina(url):
        try:
            resposta = urlopen(url)
            soup = BeautifulSoup(resposta.read(), "html.parser")
            return soup
        except:
            print("erro na função pega pagina")

    # busca os titulos das vagas
    def pegaTitulo(soup):
        titulo = []
        for item in soup.select('.listing-item__title'):
            texto = item.get_text().strip()
            titulo.append(texto)
        return titulo

    # busca os links das vagas
    def pegaLink(soup):
        links = []
        for item in soup.select('.listing-item__title'):
            links.append(item.a.get('href'))
        return links

    # busca a data em que a vaga foi publicada
    def pegaData(soup):
        data = []
        for item in soup.select('.listing-item__date'):
            data.append(item.get_text().strip())
        return data

    # busca a descrição da vaga
    def pegaDescricao(soup):
        descricao = []
        for item in soup.select('.listing-item__desc'):
            descricao.append(item.get_text().strip())
        return descricao
        # busca o tipo de contratação da vaga

    # busca o tipo de contratação da vaga
    def pegaTipoContratacao(soup):
        tipoContratacao = []
        for item in soup.select('.listing-item__employment-type'):
            tipoContratacao.append(item.get_text().strip())
        return tipoContratacao

    # busca o nome da empresa da vaga
    def pegaEmpresa(soup):
        empresa = []
        for item in soup.select('.listing-item__info--item-company'):
            empresa.append(item.get_text().strip())
        return empresa

    soup = pegaPagina(url)
    data = pegaData(soup)
    titulo = pegaTitulo(soup)
    descricao = pegaDescricao(soup)
    link = pegaLink(soup)
    empresa = pegaEmpresa(soup)
    tipoContratacao = pegaTipoContratacao(soup)

    lista_data = []
    lista_imagem = []
    lista_titulo = []
    lista_imagem = []
    lista_descricao = []
    lista_link = []
    lista_empresa = []
    lista_tipo_contratacao = []

    for i in range(0, len(data)):
        lista_data.append(data[i].strip())
        lista_titulo.append(titulo[i])
        lista_descricao.append(descricao[i])
        lista_link.append(link[i])
        lista_empresa.append(empresa[i])
        lista_tipo_contratacao.append(tipoContratacao[i])

    lista_vagas = []
    for i in range(0, len(lista_titulo)):
        vaga = {
            lista_link[i]: (lista_data[i],
                            lista_titulo[i],
                            lista_descricao[i],
                            lista_empresa[i],
                            lista_tipo_contratacao[i])
        }
        lista_vagas.append(vaga)

    dados_json = json.dumps(lista_vagas, ensure_ascii=False, indent=2)
    arquivo = open('vagas.json', 'w')
    arquivo.write(dados_json)
    arquivo.close()


if (__name__ == "__main__"):
    rodar()
