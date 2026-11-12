class ContaBancaria:
    # É o ato de proteger e ocultar os
    #dados internos de um objeto,
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def consultar_saldo(self):
        print("Saldo R$", self.__saldo)

    def despositar(self, valor):
        if valor >0:
            self.__saldo += valor
            print("Depósito de R$", valor, "realizado!")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque de R$", valor, "realizado!")
        else:
            print("Saldo insuficiente!")

conta = ContaBancaria("João R$", 500)

conta.consultar_saldo()
conta.despositar(200)
conta.sacar(100)
conta.consultar_saldo()