from Cliente import Cliente
from Endereco import Endereco
from ContaCorrente import ContaCorrente

def main():
    p1 = Cliente('João', '489847484444', '2350u2305u23', Endereco('Rua 1', '123', 'Bairro 1', 'Cidade 1', 'Estado 1'))
    p2 = Cliente('Maria', '489132123123', 'dfasadfasdfa', Endereco('Rua 1', '123', 'Bairro 1', 'Cidade 1', 'Estado 1'))
    p3 = Cliente('Jéssica', 'adasd12312a', 'df1213123fds', Endereco('Rua 2', '321', 'Bairro 3', 'Cidade 4', 'Estado 5'))
    
    conjunta = ContaCorrente([p1, p2], 1000)
    individual1 = ContaCorrente([p3])
    individual2 = ContaCorrente([p1], 1000000000)
    
    contas = [conjunta, individual1, individual2]
    
    print('\n'.join(map(str, contas)))
    
main()