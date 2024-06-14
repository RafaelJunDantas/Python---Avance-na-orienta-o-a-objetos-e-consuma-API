import os
from carro import Carro
from moto import Moto

carro1 = Carro('teste1', 'teste1', 5, 'teste1')
carro2 = Carro('teste2', 'teste2', 10, 'teste2')

carro1.ligar()

moto1 = Moto('teste3', 'teste3', 'teste3')
moto2 = Moto('teste4', 'teste4', 'teste4')

def main():
    os.system('cls')

    print(carro1)
    print(carro2)
    print(moto1)
    print(moto2)


if __name__ == '__main__':
    main()