valores = input().split()

tempoGasto = int(valores[0])
velocidadeMedia = int(valores[1])

combustivelGasto = (tempoGasto * velocidadeMedia) / 12

print(f"{combustivelGasto:.3f}")