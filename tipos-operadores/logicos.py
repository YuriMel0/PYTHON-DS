saldo = 1000
saque = 250
limite = 200
contaEspecial = True

exp = saldo >= saque and saque <= limite or contaEspecial and saldo >= saque
print(exp)


exp2 = (saldo >= saque and saque <= limite) or (contaEspecial and saldo >= saque)
print(exp2)