from abc import ABC, abstractmethod
# Consiste em isolar apenas os aspectos essenciais de um 
# objeto do mundo real, ignorando detalhes complexos e
# desnecessários para o sistema.

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class Pix(Pagamento):
    def pagar(self, valor):
        print("Pagamento de R$", valor, "realizado via Pix")

class Cartao(Pagamento):
    def pagar(self, valor):
        print("Pagamento de R$", valor, "realizado via cartão")

pagamento1 = Pix()
pagamento2 = Cartao()

pagamento1.pagar(100)
pagamento2.pagar(250)