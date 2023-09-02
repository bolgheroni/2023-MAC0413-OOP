class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        
    def __str__(self):
        return 'Rua: ' + self.rua + '\nNúmero: ' + self.numero + '\nBairro: ' + self.bairro + '\nCidade: ' + self.cidade + '\nEstado: ' + self.estado