# Desafio Python - Navi Summer
# Questão 1 : Pares, múltiplos de 37 e 49 de 1 a 5.000.000

# Podemos fazer de duas maneiras. A primeira maneira, que é a melhor, é utilizando matemática:
# Os números 2, 37 e 49 são dois a dois primos entre si, logo, podemos fazer:

print("Método 1 (matemática)")
print(int(5000000/(2*37*49)))

# A segunda maneira é uma maneira um tanto "bronca", mas é a que de fato se caracteriza como "algoritmo":

print("Método 2: (algoritmo)")

contador = 0
for i in range(5000000):
    if (i+1)%2 == 0 and (i+1)%37 ==  0 and (i+1)%49 == 0:
        contador+=1
print(contador)