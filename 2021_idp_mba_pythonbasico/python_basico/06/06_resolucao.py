dados = [
    {
        "estado": "Rondônia",
        "casos": "261632",
        "obitos": "6450",
        "populacao": "1639804"
    },
    {
        "estado": "Acre",
        "casos": "87638",
        "obitos": "1808",
        "populacao": "811558"
    },
    {
        "estado": "Amazonas",
        "casos": "422517",
        "obitos": "13645",
        "populacao": "3964796"
    },
    {
        "estado": "Roraima",
        "casos": "122373",
        "obitos": "1924",
        "populacao": "513963"
    },
    {
        "estado": "Pará",
        "casos": "579487",
        "obitos": "16324",
        "populacao": "8477847"
    },
    {
        "estado": "Amapá",
        "casos": "122199",
        "obitos": "1943",
        "populacao": "768780"
    },
    {
        "estado": "Tocantins",
        "casos": "215780",
        "obitos": "3637",
        "populacao": "1433929"
    },
    {
        "estado": "Maranhão",
        "casos": "345154",
        "obitos": "9892",
        "populacao": "7091235"
    },
    {
        "estado": "Piauí",
        "casos": "314151",
        "obitos": "6915",
        "populacao": "3456515"
    },
    {
        "estado": "Ceará",
        "casos": "928016",
        "obitos": "23921",
        "populacao": "9437695"
    },
    {
        "estado": "Rio Grande do Norte",
        "casos": "363231",
        "obitos": "7237",
        "populacao": "3501633"
    },
    {
        "estado": "Paraíba",
        "casos": "429430",
        "obitos": "9123",
        "populacao": "4110549"
    },
    {
        "estado": "Pernambuco",
        "casos": "602507",
        "obitos": "19224",
        "populacao": "9494048"
    },
    {
        "estado": "Alagoas",
        "casos": "233601",
        "obitos": "5990",
        "populacao": "3495825"
    },
    {
        "estado": "Sergipe",
        "casos": "277009",
        "obitos": "5958",
        "populacao": "2256723"
    },
    {
        "estado": "Bahia",
        "casos": "1212603",
        "obitos": "26226",
        "populacao": "15926940"
    },
    {
        "estado": "Minas Gerais",
        "casos": "2034478",
        "obitos": "52248",
        "populacao": "21752451"
    },
    {
        "estado": "Espírito Santo",
        "casos": "554543",
        "obitos": "12113",
        "populacao": "3769509"
    },
    {
        "estado": "Rio de Janeiro",
        "casos": "1097935",
        "obitos": "61090",
        "populacao": "16850577"
    },
    {
        "estado": "São Paulo",
        "casos": "4195466",
        "obitos": "143752",
        "populacao": "44104708"
    },
    {
        "estado": "Paraná",
        "casos": "1433191",
        "obitos": "36769",
        "populacao": "11557323"
    },
    {
        "estado": "Santa Catarina",
        "casos": "1139900",
        "obitos": "18453",
        "populacao": "6774628"
    },
    {
        "estado": "Rio Grande do Sul",
        "casos": "1395995",
        "obitos": "33887",
        "populacao": "11427941"
    },
    {
        "estado": "Mato Grosso do Sul",
        "casos": "364563",
        "obitos": "9224",
        "populacao": "2644457"
    },
    {
        "estado": "Mato Grosso",
        "casos": "507065",
        "obitos": "13036",
        "populacao": "3487380"
    },
    {
        "estado": "Goiás",
        "casos": "791823",
        "obitos": "21974",
        "populacao": "6683462"
    },
    {
        "estado": "Distrito Federal",
        "casos": "461925",
        "obitos": "9878",
        "populacao": "2977444"
    }
]

# Contadores para Brasil
total_obitos = 0
total_casos = 0
total_populacao = 0

for i in dados:
    # Conversão de dados para os tipos certos
    i["obitos"] = int(i["obitos"])
    i["casos"] = int(i["casos"])
    i["populacao"] = int(i["populacao"])

    # Cálculos para estados
    prop_obitos = i["obitos"] / i["casos"]
    taxa_100k = i["obitos"] / i["populacao"] * 100000

    # Atualização dos contadores para Brasil
    total_obitos += i["obitos"]
    total_casos += i["casos"]
    total_populacao += i["populacao"]

    # Adição ao dicionário
    i["proporcao_obitos"] = prop_obitos
    i["taxa_obitos_100k"] = taxa_100k

# Cálculos para Brasil
prop_obitos_br = total_obitos / total_casos
taxa_100k_br = total_obitos / total_populacao * 100000

# Neste momento temos números para cada estado e para Brasil

# Geração de duas listas vazias
prop_acima = list()
prop_abaixo = list()

# Adição de estados nas listas de acordo com condicional
for i in dados:
    if i["proporcao_obitos"] > prop_obitos_br:
        prop_acima.append(i["estado"])
    else:
        prop_abaixo.append(i["estado"])

# Geração de outras duas listas vazias
taxa_acima = list()
taxa_abaixo = list()

# Adição de estados nas listas de acordo com condicional
for i in dados:
    if i["taxa_obitos_100k"] > taxa_100k_br:
        taxa_acima.append(i["estado"])
    else:
        taxa_abaixo.append(i["estado"])

# Resultado
print("Estados com proporção maior que o Brasil: {}\nEstados com proporção menor que o Brasil: {}\nEstados com taxa maior que o Brasil: {}\nEstados com taxa menor que o Brasil: {}".format(prop_acima, prop_abaixo, taxa_acima, taxa_abaixo))