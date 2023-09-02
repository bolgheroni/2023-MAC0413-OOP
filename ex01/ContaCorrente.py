from Cliente import Cliente
from enum import Enum

class TipoConta(Enum):
    INDIVIDUAL = "Individual"
    CONJUNTA = "Conjunta"

class ContaCorrente:
    def __init__(self, titulares: list[Cliente], saldoInicial = 0):
        self.titulares = titulares
        self.saldo = saldoInicial
        
        
    def tipoConta(self):
        if (len(self.titulares) > 1):
            return TipoConta.CONJUNTA.value
        
        return TipoConta.INDIVIDUAL.value
        
    def __str__(self): 
        return 'Tipo da conta: ' + self.tipoConta() + '\n' 'Titulares: \n' + ''.join(map(str, self.titulares)) + 'Saldo: ' + str(self.saldo)  + '\n'