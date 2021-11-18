# Desafio Python - Navi Summer
# Questão 3


x = []

for i in range(5):
    nome = input("Nome do aluno " +str(i+1) + ": ")
    nota = float(input("Nota do aluno: "))
    x.append({"Nome": nome, "Nota": nota})

for i in range(5):
    if i == 0 or x[i]["Nota"] > maior_nota:
        maior_nota = x[i]["Nota"]
        posicao_maior_nota = i

print("Aluno com a maior nota: "+ x[posicao_maior_nota]["Nome"])
print("Nota do aluno: "+ str(x[posicao_maior_nota]["Nota"]))