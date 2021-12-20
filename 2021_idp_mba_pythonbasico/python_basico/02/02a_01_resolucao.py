# Em 10.jul, a Folha deu uma reportagem interessante sobre queda na 
# letalidade policial após adoção de câmeras por policiais militares
# (https://www1.folha.uol.com.br/cotidiano/2021/07/no-1o-mes-de-uso-das-cameras-grava-tudo-pm-de-sp-atinge-menor-letalidade-em-8-anos.shtml).
#
# Vamos fazer algo inspirado nisso...
#
# Vocês têm acesso aos relatórios trimestrais da Secretaria de Segurança
# Pública de São Paulo (https://www.ssp.sp.gov.br/Estatistica/Trimestrais.aspx),
# bem como às projeções de população do IBGE 
# (https://www.ibge.gov.br/estatisticas/sociais/populacao/9109-projecao-da-populacao.html?=&t=downloads).
#
# Com essas informações, é possível calcular:
# 
# 1. a variação de pessoas mortas pela polícia nos primeiros trimestres
# de 2018, 2019, 2020 e 2021;

pm_1t2021_confronto = 159
pm_1t2021_folga = 33
pc_1t2021_confronto = 4
pc_1t2021_folga = 4
t1_2021 = pm_1t2021_confronto + pm_1t2021_folga + pc_1t2021_confronto + pc_1t2021_folga

pm_1t2020_confronto = 218
pm_1t2020_folga = 37
pc_1t2020_confronto = 2
pc_1t2020_folga = 5
t1_2020 = pm_1t2020_confronto + pm_1t2020_folga + pc_1t2020_confronto + pc_1t2020_folga

pm_1t2019_confronto = 179
pm_1t2019_folga = 28
pc_1t2019_confronto = 3
pc_1t2019_folga = 3
t1_2019 = pm_1t2019_confronto + pm_1t2019_folga + pc_1t2019_confronto + pc_1t2019_folga

pm_1t2018_confronto = 157
pm_1t2018_folga = 35
pc_1t2018_confronto = 1
pc_1t2018_folga = 4
t1_2018 = pm_1t2018_confronto + pm_1t2018_folga + pc_1t2018_confronto + pc_1t2018_folga

var_1t_21_20 = t1_2021/t1_2020 - 1
print(var_1t_21_20)
# OUTPUT: -0.23664122137404575

var_1t_20_19 = t1_2020/t1_2019 - 1
print(var_1t_20_19)
# OUTPUT: 0.2300469483568075

var_1t_19_18 = t1_2019/t1_2018 - 1
print(var_1t_19_18)
# OUTPUT: 0.08121827411167515

# 2. a evolução de mortos pela polícia nos anos de 2018, 2019 e 2020;

pm_2t2020_confronto = 217
pm_2t2020_folga = 26
pc_2t2020_confronto = 5
pc_2t2020_folga = 4
pm_3t2020_confronto = 125
pm_3t2020_folga = 27
pc_3t2020_confronto = 8
pc_3t2020_folga = 2
pm_4t2020_confronto = 99
pm_4t2020_folga = 31
pc_4t2020_confronto = 6
pc_4t2020_folga = 2
ano2020 = t1_2020 + pm_2t2020_confronto + pm_2t2020_folga + pc_2t2020_confronto + pc_2t2020_folga + pm_3t2020_confronto + pm_3t2020_folga + pc_3t2020_confronto + pc_3t2020_folga + pm_4t2020_confronto + pm_4t2020_folga + pc_4t2020_confronto + pc_4t2020_folga

pm_2t2019_confronto = 179
pm_2t2019_folga = 28
pc_2t2019_confronto = 6
pc_2t2019_folga = 0
pm_3t2019_confronto = 155
pm_3t2019_folga = 40
pc_3t2019_confronto = 3
pc_3t2019_folga = 2
pm_4t2019_confronto = 203
pm_4t2019_folga = 33
pc_4t2019_confronto = 5
pc_4t2019_folga = 0
ano2019 = t1_2019 + pm_2t2019_confronto + pm_2t2019_folga + pc_2t2019_confronto + pc_2t2019_folga + pm_3t2019_confronto + pm_3t2019_folga + pc_3t2019_confronto + pc_3t2019_folga + pm_4t2019_confronto + pm_4t2019_folga + pc_4t2019_confronto + pc_4t2019_folga

pm_2t2018_confronto = 164
pm_2t2018_folga = 41
pc_2t2018_confronto = 8
pc_2t2018_folga = 5
pm_3t2018_confronto = 156
pm_3t2018_folga = 46
pc_3t2018_confronto = 2
pc_3t2018_folga = 6
pm_4t2018_confronto = 165
pm_4t2018_folga = 57
pc_4t2018_confronto = 2
pc_4t2018_folga = 2
ano2018 = t1_2018 + pm_2t2018_confronto + pm_2t2018_folga + pc_2t2018_confronto + pc_2t2018_folga + pm_3t2018_confronto + pm_3t2018_folga + pc_3t2018_confronto + pc_3t2018_folga + pm_4t2018_confronto + pm_4t2018_folga + pc_4t2018_confronto + pc_4t2018_folga

var20_19 = ano2020/ano2019 - 1
print(var20_19)
# OUTPUT: -0.06113033448673588

var19_18 = ano2019/ano2018 - 1
print(var19_18)
# OUTPUT: 0.018801410105757865

# 3. a cada 1 milhão de paulistas, quantos morrem devido à ação das
# polícias civil e militar.

pop2020 = 46289333
pop2019 = 45919049
pop2018 = 45538936

mi_2020 = (ano2020/pop2020) * 1000000
print(mi_2020)
# OUTPUT: 17.585044917367895

mi_2019 = (ano2019/pop2019) * 1000000
print(mi_2019)
# OUTPUT: 18.88105304619876

mi_2018 = (ano2018/pop2018) * 1000000
print(mi_2018)
# OUTPUT: 18.68730529848128

# CONCLUSÃO: Dos três anos observados (2018 a 2020), 2019 foi o mais 
# letal: a cada milhão de habitantes, 19 perderam a vida devido à
# ação policial. Apesar de 2020 apresentar menos mortos por milhão
# de habitantes, o primeiro trimestre daquele ano apresentou 
# tendência de alta no número de óbitos: 23% a mais do que no mesmo 
# período de 2019. Supõe-se, portanto, que a pandemia (melhor ainda:
# o isolamento social) tenha freado a letalidade policial.