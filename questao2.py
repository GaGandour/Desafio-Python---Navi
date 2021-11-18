# Desafio Python - Navi Summer
# Questão 2

import math

x = [[] for i in range(10)]

soma = 0
posicao_maior_valor = 0
maior_valor = 0

for i in range(10): # Constrói o vetor x ENQUANTO calcula a posição do maior valor e a média.
    x[i] = 3**i+7*math.factorial(i) if i%2 == 0 else 2**i+4*math.log(i)
    soma+=x[i]
    if i == 0:
        soma = x[0]
        maior_valor = x[0]
    if x[i] > maior_valor:
        posicao_maior_valor = i
        maior_valor = x[i]

print("A posição do maior valor de x é " + str(posicao_maior_valor))
print("A média dos valores de x é, aproximadamente, "+ str(round(soma/10, 2)))