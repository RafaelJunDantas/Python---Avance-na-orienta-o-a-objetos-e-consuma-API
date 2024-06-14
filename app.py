import os
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida

restaurante1 = Restaurante('pizza', 'pizza')
restaurante2 = Restaurante('sushi', 'sushi')

restaurante1.adicionar_avaliacao('a', 5)
restaurante1.adicionar_avaliacao('b', 10)
restaurante1.adicionar_avaliacao('c', 6)

restaurante1.alternar_estado()

bebida1 = Bebida('suco', 5, 'medio')
bebida1.aplicar_desconto(0.5)

prato1 = Prato('pizza', 10, 'pizza pizza')
prato1.aplicar_desconto()

sobremesa1 = Sobremesa('sorvete', 15, 'sorvete', 'grande')
sobremesa1.aplicar_desconto()

restaurante1.adicionar_item_cardapio(bebida1)
restaurante1.adicionar_item_cardapio(prato1)
restaurante1.adicionar_item_cardapio(sobremesa1)

def main():
    os.system('clear')

    Restaurante.listar_restaurantes()

    print('-' * 50)

    restaurante1.listar_cardapio()

if __name__ == '__main__':
    main()