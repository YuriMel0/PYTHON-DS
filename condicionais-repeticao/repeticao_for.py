# 1 exemplo
vogais = "AEIOU"

for letra in vogais:
    if letra.upper() in vogais:
        print(letra, end=" ")
else:
    print() # adiciona quebra de linha

# 2 exemplo
for numero in range(0, 51, 5):
    print(numero, end=" ")