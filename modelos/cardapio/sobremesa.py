from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho

    def __str__(self):
        return 'Sobremesa - ' + super().__str__() + f'Tipo: {self._tipo} | Tamanho: {self._tamanho}'
    
    def aplicar_desconto(self):
        return super().aplicar_desconto()