class Mercado:
    def __init__(self, nome):
        self.nome = nome
        self.precos = {}

    def adicionar_preco_ingrediente(self, ingrediente, preco):
        """
        Adiciona o preço de um ingrediente neste mercado.
        """
        self.precos[ingrediente] = preco

    def obter_preco_ingrediente(self, ingrediente):
        """
        Retorna o preço de um ingrediente neste mercado.
        """
        return self.precos.get(ingrediente, None)
