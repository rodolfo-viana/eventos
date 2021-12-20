# Na noite de 3 de julho, o painel de vacinação contra a covid-19 do 
# Ministério da Saúde apontava pouco mais de 97 milhões de doses de 
# vacina aplicadas na população brasileira.
# (Fonte: https://qsprod.saude.gov.br/extensions/DEMAS_C19Vacina/DEMAS_C19Vacina.html)
#
# Como os dados estão separados por estado, é possível calcular a 
# proporção de doses aplicadas em certo estado ou certa região em 
# relação ao total. É o que faremos aqui: calcularemos o percentual 
# de doses aplicadas na região sudeste em relação ao Brasil.
#
# O código, contudo, está embaralhado. Precisamos colocá-lo em ordem.
#
# Mesmo sem saber Python, usando apenas a lógica e a descrição de 
# cada bloco de código, você consegue ordená-los? 

# Primeiro atribuo valores a variáveis...
estados = [
    {"uf": "AC", "doses": 364906},
    {"uf": "AL", "doses": 1421213},
    {"uf": "AM", "doses": 1773255},
    {"uf": "AP", "doses": 271691},
    {"uf": "BA", "doses": 6152177},
    {"uf": "CE", "doses": 3270535},
    {"uf": "DF", "doses": 1283699},
    {"uf": "ES", "doses": 2219656},
    {"uf": "GO", "doses": 3111799},
    {"uf": "MA", "doses": 3106822},
    {"uf": "MG", "doses": 9357072},
    {"uf": "MS", "doses": 1615951},
    {"uf": "MT", "doses": 1351618},
    {"uf": "PA", "doses": 2890438},
    {"uf": "PB", "doses": 1834443},
    {"uf": "PE", "doses": 3750035},
    {"uf": "PI", "doses": 1391719},
    {"uf": "PR", "doses": 5830476},
    {"uf": "RJ", "doses": 8084518},
    {"uf": "RN", "doses": 1652963},
    {"uf": "RO", "doses": 688403},
    {"uf": "RR", "doses": 222025},
    {"uf": "RS", "doses": 6832516},
    {"uf": "SC", "doses": 3225600},
    {"uf": "SE", "doses": 923887},
    {"uf": "SP", "doses": 23887012},
    {"uf": "TO", "doses": 621308}
]

sudeste = ["SP", "RJ", "MG", "ES"]

# ...em seguida, somo as doses no total (salvando na variável 'total')
# e as doses do sudeste (salvando na variável vacinas_sudeste)...
total = 0
for i in estados:
    total += i["doses"]

vacinas_sudeste = 0
for i in estados:
    if i["uf"] in sudeste:
        vacinas_sudeste += i["doses"]

# ...em seguida, faço o cálculo e salvo em uma variável...
calculo = (vacinas_sudeste / total) * 100

# ...e, por fim, imprimo o resultado.
print("A região sudeste aplicou {}% do total de {} doses consumidas no Brasil".format(calculo, total))

# OUTPUT
# ------
# A região sudeste aplicou 44.83237513295442% do total de 97135737 doses consumidas no Brasil