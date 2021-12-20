# Pergunta 6: Comparando ago.2020 com 2012, qual classe econômica 
# teve maior aumento? E qual teve maior queda?

# 2012
atemeio2012 = 65800895
ate1sm2012 = 59990268
ate2sm2012 = 44343219
ate4sm2012 = 18125985
mais4sm2012 = 10054567
# agosto de 2020
atemeioagosto = 50176044
ate1smagosto = 76590769
ate2smagosto = 56859091
ate4smagosto = 19185258
mais4smagosto = 8930353

# Cálculos da proporções de cada faixa em 2012
total_trabalhadores_2012 = atemeio2012 + ate1sm2012 + ate2sm2012 + ate4sm2012 + mais4sm2012

prop_meio_2012 = atemeio2012 / total_trabalhadores_2012 # 33,17 = 65 mi
prop_1_2012 = ate1sm2012 / total_trabalhadores_2012 # 30,25 = 60 mi
prop_2_2012 = ate2sm2012 / total_trabalhadores_2012 # 22,36 = 44 mi
prop_4_2012 = ate4sm2012 / total_trabalhadores_2012 # 9,14 = 18 mi
prop_ricos_2012 = mais4sm2012 / total_trabalhadores_2012 # 5,07 = 10 mi

# Cálculos da proporções de cada faixa em agosto de 2020
total_trabalhadores_ago_20 = atemeioagosto + ate1smagosto + ate2smagosto + ate4smagosto + mais4smagosto

prop_meio_agosto = atemeioagosto / total_trabalhadores_ago_20 # 23,7 = 50 mi
prop_1_agosto = ate1smagosto / total_trabalhadores_ago_20 # 36,17 = 76 mi
prop_2_agosto = ate2smagosto / total_trabalhadores_ago_20 # 26,85 = 56 mi
prop_4_agosto = ate4smagosto / total_trabalhadores_ago_20 # 9,06 = 19 mi
prop_ricos_agosto = mais4smagosto / total_trabalhadores_ago_20 # 4,21 = 9 mi

# Cálculo da variação das proporções
var_meio = (prop_meio_agosto - prop_meio_2012) / prop_meio_2012 # -28
var_1sm = (prop_1_agosto - prop_1_2012) / prop_1_2012 # 19
var_2sm = (prop_2_agosto - prop_2_2012) / prop_2_2012 # 20
var_4sm = (prop_4_agosto - prop_4_2012) / prop_4_2012 # -0,8
var_ricos = (prop_ricos_agosto - prop_ricos_2012) / prop_ricos_2012 # -16
print(var_meio, var_1sm, var_2sm, var_4sm, var_ricos)