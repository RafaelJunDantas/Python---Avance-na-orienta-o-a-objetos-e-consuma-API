from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        return 'Moto: ' + super().__str__() + f'Tipo: {self._tipo}'
    
    def ligar(self):
        return super().ligar()
    

moto1 = Moto('a', 'a', 'a')

print(moto1)