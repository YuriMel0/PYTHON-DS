MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("pode tirar CNH")
if idade < MAIOR_IDADE:
    print("Não pode tirar CNH")



if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar CNH")
else:
    print("Não pode tirar CNH")



if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas mas não pode fazer pratica!")
else:
    print("Não pode tirar CNH")

status = "Tem CNH" if idade >= MAIOR_IDADE else "Não tem CNH"
print(status)