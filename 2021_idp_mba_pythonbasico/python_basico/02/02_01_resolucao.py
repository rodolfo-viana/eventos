# AFIRMAÇÃO:
# Levantamento de classes econômicas brasileiras realizado a partir de dados factuais
# coletados durante a pandemia mostra que o número de pobres no Brasil (renda
# domiciliar per capita até ½ salário mínimo) caiu 15 milhões entre 2019 e agosto de
# 2020.

# PERGUNTA 1: Essa informação é verdadeira?
p2019_meio = 65229668
pago_meio = 50176044
diferenca = pago_meio - p2019_meio
print(diferenca)
# OUTPUT: -15053624
# RESPOSTA: Sim. Houve queda de 15.053.624 no número de pobres.
 
# PERGUNTA 2: Qual foi a queda percentual?
diferenca_perc = diferenca / p2019_meio
print(diferenca_perc)
# OUTPUT: -0.23077879225140316
# RESPOSTA: Queda de 23,07%.

# AFIRMAÇÃO:
# Já os estratos mais abastados com renda acima de dois salários mínimos per capita
# perderam 4,8 milhões de pessoas em plena pandemia.

# PERGUNTA 3: Essa informação é verdadeira?
p2019_4sm = 21519066
p2019_4smmais = 11410989
abastados_2019 = p2019_4sm + p2019_4smmais
pago_4sm = 19185258
pago_4smmais = 8930353
abastados_ago2020 = pago_4sm + pago_4smmais
diferenca = abastados_ago2020 - abastados_2019
print(diferenca)
# OUTPUT: -4814444
# RESPOSTA: Sim. Houve queda de 4.814.444 pessoas com 2 ou mais salários mínimos no período.

# PERGUNTA 4: Qual foi a queda percentual?
diferenca_perc = diferenca / abastados_2019
print(diferenca_perc)
# OUTPUT: -0.14620212447261324
# RESPOSTA: Queda de 14,62%.

# PERGUNTA 5: Qual foi a variação em cada faixa da pirâmide entre jul.2020 e ago.2020?
# LÓGICA: Para saber a variação, uso regra de três entre diferença entre os meses e o
# mês de base de comparação
pjul_meio = 52127922
pjul_1sm = 76318115
pjul_2sm = 56215080
pjul_4sm = 18646895
pjul_4smmais = 8447679
pago_1sm = 76590769
pago_2sm = 56859091
meio = (pago_meio - pjul_meio) / pjul_meio # Forma convencional de fazer regra de três
umsm = (pago_1sm - pjul_1sm) / pjul_1sm
doissm = (pago_2sm - pjul_2sm) / pjul_2sm
quatrosm = (pago_4sm - pjul_4sm) / pjul_4sm
quatrosmmais = (pago_4smmais - pjul_4smmais) / pjul_4smmais
print(meio, umsm, doissm, quatrosm, quatrosmmais)
# OUTPUT: -0.037444001700278784 0.0035725987205003687 0.01145619645120135 0.02887145554259838 0.05713687747841745
# RESPOSTA: Houve queda de 3,74% no universo com renda até ½ salário mínimo,
# aumento de 0,35% no número de pessoas com renda entre ½ e 1 salário,
# aumento de 1,14% de pessoas com renda de 1 a 2 salários, aumento de 2,88%
# no universo de pessoas com renda entre 2 e 4 salários, e aumento de 5,71%
# no número de pessoas com renda acima de 4 salários mínimos.

# PERGUNTA 6: Comparando ago.2020 com 2012, qual classe econômica teve maior aumento? E qual
# teve maior queda?
# LÓGICA: Aqui preciso saber:
# 1. a proporção de cada faixa de renda na população total em 2012
# 2. a proporção de cada faixa de renda na população total em agosto de 2020
# 3. fazer uma regra de três para calcular a variação percentual entre as proporções
p2012_meio = 65800895
p2012_1sm = 59990268
p2012_2sm = 44343219
p2012_4sm = 18125985
p2012_4smmais = 10054567
total_2012 = p2012_meio + p2012_1sm + p2012_2sm + p2012_4sm + p2012_4smmais
prop_2012_meio = p2012_meio / total_2012
prop_2012_1sm = p2012_1sm / total_2012
prop_2012_2sm = p2012_2sm / total_2012
prop_2012_4sm = p2012_4sm / total_2012
prop_2012_4smmais = p2012_4smmais / total_2012
total_ago = pago_meio + pago_1sm + pago_2sm + pago_4sm + pago_4smmais
prop_ago_meio = pago_meio / total_ago
prop_ago_1sm = pago_1sm / total_ago
prop_ago_2sm = pago_2sm / total_ago
prop_ago_4sm = pago_4sm / total_ago
prop_ago_4mais = pago_4smmais / total_ago
meio = prop_ago_meio / prop_2012_meio - 1 # Forma alternativa de fazer regra de três
umsm = prop_ago_1sm / prop_2012_1sm - 1
doissm = prop_ago_2sm / prop_2012_2sm - 1
quatrosm = prop_ago_4sm / prop_2012_4sm - 1
quatrosmmais = prop_ago_4mais / prop_2012_4smmais - 1
print(meio, umsm, doissm, quatrosm, quatrosmmais)
# OUTPUT: -0.28580957997505974 0.19576278100601696 0.20094218241735473 -0.00867643215561642 -0.16813154233372274
# Resposta: A faixa até ½ teve queda de 28,58%; de ½ a 1 salário, crescimento 
# de 19,57%; de 1 a 2 salários, crescimento de 20,09%; de 2 a 4 salários,
# queda de 0,86%; e superior a 4 salários mínimos, queda de 16,81%.

# CONCLUSÃO: Tivemos queda no número de muito pobres, mas também nas faixas mais abastadas,
# concentrando a população na faixa entre 1 e 2 salários mínimos.