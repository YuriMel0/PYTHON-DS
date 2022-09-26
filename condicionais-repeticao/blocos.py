def sacar(valor):
    saldo = 500
    if saldo >= valor:
        saldo -= valor
        print("saque realizado com sucesso")

    print(f"saldo atual: {saldo}")


def depositar(valor):
    saldo = 500
    saldo += valor
    print("deposito realizado com sucesso")
    print(f"saldo atual: {saldo}")


sacar(100)
depositar(100)