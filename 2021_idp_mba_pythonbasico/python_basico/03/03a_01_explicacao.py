# 2012
atemeio2012 = 65800895
ate1sm2012 = 59990268
ate2sm2012 = 44343219
ate4sm2012 = 18125985
mais4sm2012 = 10054567
# 2019
atemeio2019 = 65229668
ate1sm2019 = 61909343
ate2sm2019 = 50078060
ate4sm2019 = 21519066
mais4sm2019 = 11410989
# julho de 2020
atemeiojulho = 52127922
ate1smjulho = 76318115
ate2smjulho = 56215080
ate4smjulho = 18646895
mais4smjulho = 8447679
# agosto de 2020
atemeioagosto = 50176044
ate1smagosto = 76590769
ate2smagosto = 56859091
ate4smagosto = 19185258
mais4smagosto = 8930353

# Segundo o release do estudo,
#
# "Levantamento de classes econômicas brasileiras realizado a partir de 
# dados factuais coletados durante a pandemia mostra que o número de 
# pobres no Brasil (renda domiciliar per capita até ½ salário mínimo) 
# caiu 15 milhões entre 2019 e agosto de 2020.
#
# Pergunta 1: Essa informação é verdadeira?
diff2020_2019 = atemeioagosto - atemeio2019
print(diff2020_2019)

# Pergunta 2: Qual foi a queda percentual?
print(diff2020_2019 / atemeio2019)

# Também segundo o release,
# 
# "Já os estratos mais abastados com renda acima de dois salários 
# mínimos per capita perderam 4,8 milhões de pessoas em plena 
# pandemia."
# 
# Pergunta 3: Essa informação é verdadeira?
abastados2020 = ate4smagosto + mais4smagosto
abastados2019 = ate4sm2019 + mais4sm2019
diff_abastados = abastados2020 - abastados2019
print(diff_abastados)

# Pergunta 4: Qual foi a queda percentual?
print(diff_abastados / abastados2019) # variável diff_abastados
# print((abastados2020 - abastados2019) / abastados2019) # não usei variável
# print(abastados2020 / abastados2019 - 1) # não usei a subtração
#
# EXPLICAÇÃO DE REGRA DE TRÊS
# ---------------------------
# um botijão de gás em 2020 ---> 85 -----> 85 ----> 100 -------------> 1
# um botijão de gás em 2021 ---> 112 ----> 27 ----> x ----> 31.76 ---> 0.3176
#
# No nosso contexto...
# abastados2019 ----> 32.930.055 ----> 32.930.055 ---> 100 ----------------> 1
# abastados2020 ----> 28.115.611 ----> -4.814.444 ---> x -----> -14.62 ----> -0.1462
#
# 32930055x = -4814444 * 100
# x = -4814444 * 100 / 32930055 ---> output: -14.6202124473
# ou...
# x = -4814444 / 32930055 ---------> output: -0.14620212447

# Pergunta 5: Qual foi a variação em cada faixa da pirâmide entre 
# jul.2020 e ago.2020?

# Pergunta 6: Comparando ago.2020 com 2012, qual classe econômica 
# teve maior aumento? E qual teve maior queda?
# 1. população total no ano
# 2. qts % cada faixa representa
# 3. fazer regra de três

#
# 2012 = 50%
# 2020 = 70% ---> 40%


