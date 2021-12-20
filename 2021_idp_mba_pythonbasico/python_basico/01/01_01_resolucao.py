# Para calcular a área de um círculo, usamos a fórmula A = π×r², onde:
# 
# π: valor constante (aqui usaremos 3,14159)
# r: raio
# 
# Já o perímetro do círculo (comprimento da circunferência que limita o círculo) 
# segue a fórmula P = 2×π×r.
#
# O código abaixo deve calcular área e perímetro de um círculo de 12,7 metros 
# de raio, porém as linhas estão embaralhadas.
#
# Mesmo sem saber Python, consegue ordená-las seguindo apenas a lógica?

# Primeiro atribuo valores a variáveis...
pi = 3.14159
raio = 12.7

# ...em seguida faço os cálculos usando as variáveis e salvando os resultados 
# em outras variáveis...
area = pi * (raio**2)
perimetro = 2 * pi * raio

# ...e, por fim, imprimo os resultados.
print("A área é {} m²".format(area))
print("O perímetro é {} m".format(perimetro))

# OUTPUT
# ------
# A área é 506.70705109999994 m²
# O perímetro é 79.796386 m