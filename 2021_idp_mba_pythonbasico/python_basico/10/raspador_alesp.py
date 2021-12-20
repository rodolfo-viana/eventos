import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

tempo = list()
anos = ["2019", "2020", "2021"]
for i in anos:
    if i == "2019": # True or False
        meses = ["08", "09", "10", "11", "12"]
        for x in meses:
            tempo.append("{}-{}".format(i, x))
    elif i == "2021":
        meses = ["01", "02", "03", "04", "05", "06", "07"]
        for x in meses:
            tempo.append("{}-{}".format(i, x))
    else:
        meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        for x in meses:
            tempo.append("{}-{}".format(i, x))
lista = list()
for u in tempo:
    url = "https://www.al.sp.gov.br/repositorio/folha-de-pagamento/folha-{}-detalhada.html".format(u)
    conteudo = requests.get(url)
    interpret = bs(conteudo.content, "html.parser")
    tbody = interpret.find("tbody")
    tr = tbody.find_all("tr")
    for i in tr:
        dicionario = dict()
        dicionario["periodo"] = u
        dicionario["nome"] = i.find_all("td")[0].text.strip()
        dicionario["rem_bruta"] = float(i.find_all("td")[1].text.strip().replace(".", "").replace(",", "."))
        dicionario["rem_liquida"] = float(i.find_all("td")[2].text.strip().replace(".", "").replace(",", "."))
        dicionario["tributos"] = float(i.find_all("td")[3].text.strip().replace(".", "").replace(",", "."))
        dicionario["abono_permanencia"] = float(i.find_all("td")[4].text.strip().replace(".", "").replace(",", "."))
        dicionario["ferias_bruto"] = float(i.find_all("td")[5].text.strip().replace(".", "").replace(",", "."))
        dicionario["ferias_desc"] = float(i.find_all("td")[6].text.strip().replace(".", "").replace(",", "."))
        dicionario["ferias_liq"] = float(i.find_all("td")[7].text.strip().replace(".", "").replace(",", "."))
        dicionario["13_bruto"] = float(i.find_all("td")[8].text.strip().replace(".", "").replace(",", "."))
        dicionario["13_desconto"] = float(i.find_all("td")[9].text.strip().replace(".", "").replace(",", "."))
        dicionario["13_liquido"] = float(i.find_all("td")[10].text.strip().replace(".", "").replace(",", "."))
        dicionario["retro_bruto"] = float(i.find_all("td")[11].text.strip().replace(".", "").replace(",", "."))
        dicionario["retro_desconto"] = float(i.find_all("td")[12].text.strip().replace(".", "").replace(",", "."))
        dicionario["retro_liquido"] = float(i.find_all("td")[13].text.strip().replace(".", "").replace(",", "."))
        dicionario["outros_bruto"] = float(i.find_all("td")[14].text.strip().replace(".", "").replace(",", "."))
        dicionario["outros_desc"] = float(i.find_all("td")[15].text.strip().replace(".", "").replace(",", "."))
        dicionario["indeniza"] = float(i.find_all("td")[16].text.strip().replace(".", "").replace(",", "."))
        lista.append(dicionario)
df = pd.DataFrame.from_dict(lista)
df.to_csv("trabalho_final.csv", index=False)