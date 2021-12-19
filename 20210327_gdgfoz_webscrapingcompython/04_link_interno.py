import csv
import requests
from bs4 import BeautifulSoup as bs


domain_url = "http://cnes2.datasus.gov.br/"
path_url = "Mod_Ind_Tipo_Leito.asp?"
query_url = "VEstado=00"
url = domain_url + path_url + query_url

lista_final = list()

site = requests.get(url)
if site.ok:
    content = bs(site.content, "html.parser")
    tabela = content.find_all("table")[5]  # Sexta tabela do HTML
    links = tabela.find_all("a")
    for l in links:
        tipo = l.text.strip().replace("\t", "")  # Tiramos espaços e tabs

        # Vamos entrar em cada link e pegar o conteúdo
        link = domain_url + l["href"]
        link_interno = requests.get(link)
        link_content = bs(link_interno.content, "html.parser")
        link_tabela = link_content.find_all("table")[3]
        link_linhas = link_tabela.find_all("tr")[1:-2]
        for r in link_linhas:
            cnes = r.find_all("font")[0].text
            nome = r.find_all("font")[1].text.strip().replace("\t", "")
            leitos = r.find_all("font")[2].text
            leitos_sus = r.find_all("font")[3].text

            dicionario = dict(
                tipo=tipo, cnes=cnes, nome=nome, leitos=leitos, leitos_sus=leitos_sus
            )
            lista_final.append(dicionario)

with open("leitos.csv", "w") as file:
    writer = csv.DictWriter(
        file, fieldnames=["tipo", "cnes", "nome", "leitos", "leitos_sus"]
    )
    writer.writeheader()
    writer.writerows(lista_final)