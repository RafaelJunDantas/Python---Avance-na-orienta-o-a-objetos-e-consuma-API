from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self._portas = portas
        self._cor = cor

    def __str__(self):
        return 'Carro: ' + super().__str__() + f'Portas: {self._portas} | Cor: {self._cor}'

    def ligar(self):
        self._ligado = True
    

carro1 = Carro('a', 'a', 5, 'a')

print(carro1)