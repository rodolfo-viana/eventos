import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

senads = list()
url2 = "https://www25.senado.leg.br/web/transparencia/sen/em-exercicio/-/e/por-nome"
pg_senadores = requests.get(url2)
senadores = bs(pg_senadores.content, "html.parser")
tbody_s = senadores.find("tbody")
for tr in tbody_s.find_all("tr"):
    dicio = dict()
    td = tr.find_all("td")[0]
    dicio["nome"] = td.find("a").text
    dicio["matr"] = td.find("a").get("href").replace("https://www6g.senado.leg.br/transparencia/sen/", "")
    senads.append(dicio)
anos = ["2019", "2020", "2021"]
lista = list()
for a in anos:
    for s in senads:
        url = "https://www6g.senado.leg.br/transparencia/sen/{}/?ano={}".format(s["matr"], a)
        fonte = requests.get(url)
        conteudo = bs(fonte.content, "html.parser")
        lista_tbody = conteudo.find_all("tbody")
        tbody_escolhido = lista_tbody[0]  
        for tr in tbody_escolhido.find_all("tr"):
            dicionario = dict()
            dicionario["ano"] = a
            dicionario["nome"] = s["nome"]
            dicionario["descr"] = tr.find_all("td")[0].text.strip()
            dicionario["valor"] = float(tr.find_all("td")[1].text.strip().replace(".", "").replace(",", "."))
            lista.append(dicionario)
df = pd.DataFrame.from_dict(lista)
df.to_csv("auladamanha.csv", index=False)