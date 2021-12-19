import csv
from datetime import timedelta, datetime, date
import requests
from bs4 import BeautifulSoup as bs


domain_url = "https://www.gov.br/"
path_url = "planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/"

dia_um = date(2019, 1, 1)
hoje = date.today()
qt_dias = hoje - dia_um

calendario = list()
for i in range(qt_dias.days + 1):
    dia = dia_um + timedelta(days=i)
    calendario.append(dia.strftime("%Y-%m-%d"))

lista_final = list()
for d in calendario:
    url = domain_url + path_url + d
    site = requests.get(url)

    if site.ok:
        content = bs(site.content, "html.parser")
        lista = content.find("ul", class_="list-compromissos")
        itens = lista.find_all("li", class_="item-compromisso-wrapper")

        for i in itens:
            if i.find("time", class_="compromisso-inicio"):
                inicio = i.find("time", class_="compromisso-inicio").text
            else:
                inicio = ""
            if i.find("time", class_="compromisso-fim"):
                fim = i.find("time", class_="compromisso-fim").text
            else:
                fim = ""
            if i.find("h4", class_="compromisso-titulo"):
                compromisso = i.find("h4", class_="compromisso-titulo").text
            else:
                compromisso = ""
            if i.find("div", class_="compromisso-local"):
                local = i.find("div", class_="compromisso-local").text
            else:
                local = ""

            # Para não repetir if-else, eu poderia criar uma função:
            #
            # FUNÇÃO
            # ------
            # def elemento_existe(html, css):
            #     if i.find(html, class_=css):
            #         var = i.find(html, class_=css).text
            #     else:
            #         var = ""
            #     return var
            #
            # USO
            # ---
            # inicio = elemento_existe("time", "compromisso-inicio")
            # fim = elemento_existe("time", "compromisso-fim")
            # compromisso = elemento_existe("h4", "compromisso-titulo")
            # local = elemento_existe("div", "compromisso-local")

            dicionario = dict(
                data=d, inicio=inicio, fim=fim, compromisso=compromisso, local=local
            )
            lista_final.append(dicionario)

with open("agenda_pres.csv", "w") as file:
    writer = csv.DictWriter(
        file, fieldnames=["data", "inicio", "fim", "compromisso", "local"]
    )
    writer.writeheader()
    writer.writerows(lista_final)