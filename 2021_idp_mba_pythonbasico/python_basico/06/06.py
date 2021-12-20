# Abaixo estão dados reais de covid-19 referentes ao dia 20 de agosto. 
# As fontes são o Ministério da Saúde (para números de casos e óbitos) 
# e o IBGE (para a população estimada em cada estado).
#
# Com essas informações, preciso responder quatro perguntas:
#
# 1. Quais estados têm letalidade (ou seja, óbitos por casos) acima do
# geral nacional;
# 2. Quais estados têm letalidade abaixo;
# 3. Quais estados têm a taxa de óbitos por 100 mil habitantes maior
# do que o geral nacional;
# 4. Quais estados têm a taxa de óbitos por 100 mil habitantes menor.
#
# Reparem: eu não preciso de números nas respostas; apenas dos nomes
# dos estados. Algo como:
# Estados com letalidade maior que o Brasil: [A, B, C]
# Estados com letalidade menor que o Brasil: [X, Y, Z]
# Estados com taxa maior que o Brasil: [A, Y, Z]
# Estados com taxa menor que o Brasil: [X, B, C]
#
# Para fazer este exercício, além de tudo o que aprendeu, você 
# precisará saber o que é contador. Segue uma explicação em código:
#
# lista = [3, 8, 13]. # Como eu somo esses números? 
#
# soma = 0 # Começo com o valor zero...
# for n in lista: # ...e a cada item em lista...
#     soma = soma + n # ...adiciono o número
#
# Isso é um contador. Caso precise de mais explicação, me chame.

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