from Endereco import Endereco

class Cliente:
    def __init__(self, nome, cpf, rg, endereco: Endereco):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        
    def __str__(self):
        return 'Nome: ' + self.nome + '\nCPF: ' + self.cpf + '\nRG: ' + self.rg + '\nEndereço: ' + str(self.endereco) + '\n'