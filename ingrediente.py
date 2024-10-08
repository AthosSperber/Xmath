import mercado
from dados import GerenciadorDeDados

class Ingrediente:
    def __init__(self, nome, dados):
        self.nome = nome
        self.precos_por_mercado = dados.dados.get(nome, {})

    def adicionar_preco(self, mercado, preco, quantidade, unidade, gerenciador_de_dados):
        self.precos_por_mercado[mercado] = {
            "preco": preco,
            "quantidade": quantidade,
            "unidade": unidade
        }
        gerenciador_de_dados.editar_ingrediente(self.nome, self.precos_por_mercado)

    def mercado_mais_barato(self):
        """
        Retorna o mercado com o preço mais barato do ingrediente.
        """
        if not self.precos_por_mercado:
            return None, 0
        mercado_barato = min(self.precos_por_mercado, key=lambda x: self.precos_por_mercado[x]['preco'])
        return mercado_barato, self.precos_por_mercado[mercado_barato]["preco"]

def calcular_total_sanduiche(ingredientes_sanduiche, dados):
    total = 0
    detalhes_ingredientes = []
    
    for ingrediente_nome, quantidade_necessaria in ingredientes_sanduiche.items():
        ingrediente = Ingrediente(ingrediente_nome, dados)
        mercado, preco_unidade = ingrediente.mercado_mais_barato()
        
        if mercado:         
            unidade = ingrediente.precos_por_mercado[mercado]["unidade"]
            if unidade == "gramas":
                quantidade_comprada = float(ingrediente.precos_por_mercado[mercado]["quantidade"])
                preco_total = (preco_unidade / quantidade_comprada) * quantidade_necessaria            
            else:
                quantidade_comprada = int(ingrediente.precos_por_mercado[mercado]["quantidade"])
                preco_total = (preco_unidade / quantidade_comprada) * quantidade_necessaria
            
            total += preco_total
            detalhes_ingredientes.append((ingrediente_nome, mercado, preco_unidade, quantidade_necessaria, preco_total))
    
    lucro_total = total * 1.7 
    return detalhes_ingredientes, total, lucro_total

