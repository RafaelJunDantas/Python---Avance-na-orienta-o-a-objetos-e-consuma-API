from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self ,nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
    
    def __str__(self):
        return 'Bebida - ' + super().__str__() + f'Tamanho: {self._tamanho}'
    
    def aplicar_desconto(self, desconto):
        self._preco = self._preco * (1 - desconto)