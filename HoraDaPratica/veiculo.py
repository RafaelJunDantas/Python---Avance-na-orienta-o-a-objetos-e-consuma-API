from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Ligado: {self._ligado} | '
    
    @abstractmethod
    def ligar(self):
        pass