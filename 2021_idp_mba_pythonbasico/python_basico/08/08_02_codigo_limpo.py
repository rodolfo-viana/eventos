import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

endereco = "https://www6g.senado.leg.br/transparencia/sen/"
senador = "5894"
query_ano = "/?ano="
ano = "2021"
url = endereco + senador + query_ano + ano
site = requests.get(url)
content = bs(site.content, "html.parser")
tabela = content.find_all("table")[0]
tbody = tabela.find("tbody")
itens = tbody.find_all("tr")
dados = list()
for i in itens:
    dicionario = dict()
    dicionario["categoria"] = i.find_all('td')[0].text.strip()
    dicionario["valor"] = float(i.find_all('td')[1].text.strip().replace(".", "").replace(",", "."))
    dados.append(dicionario)
df = pd.DataFrame.from_dict(dados)
df.to_csv('teste.csv', index=False)