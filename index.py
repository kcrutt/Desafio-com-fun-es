def produto(numA, numB):
    diferenca = numA - numB
    return diferenca

resultado = produto(87, 15)
Ranking = ""

if resultado <= 10:
    Ranking = "Ferro"
elif resultado <= 20:
    Ranking = "Bronze"
elif resultado <= 50:
    Ranking = "Prata"
elif resultado <= 80:
    Ranking = "Ouro"
elif resultado <= 90:
    Ranking = "Diamante"
elif resultado <= 100:
    Ranking = "Lendário"
elif resultado >= 101:
    Ranking = "Imortal"

print("O Herói tem saldo de " + str(resultado) + " pontos e está no nível de " + Ranking)
