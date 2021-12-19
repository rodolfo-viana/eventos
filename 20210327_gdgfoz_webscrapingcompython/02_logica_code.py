import csv
import requests
from bs4 import BeautifulSoup as bs


domain_url = "https://www.gov.br/"
path_url = "planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/"
query_url = "2021-03-19"
url = domain_url + path_url + query_url

site = requests.get(url)

content = bs(site.content, "html.parser")
lista = content.find("ul", class_="list-compromissos")
itens = lista.find_all("li", class_="item-compromisso-wrapper")

lista_final = list()
for i in itens:
    inicio = i.find("time", class_="compromisso-inicio").text
    fim = i.find("time", class_="compromisso-fim").text
    compromisso = i.find("h4", class_="compromisso-titulo").text
    local = i.find("div", class_="compromisso-local").text
    dicionario = dict(inicio=inicio, fim=fim, compromisso=compromisso, local=local)
    lista_final.append(dicionario)

with open("agenda_pres.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["inicio", "fim", "compromisso", "local"])
    writer.writeheader()
    writer.writerows(lista_final)