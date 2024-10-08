import json

class GerenciadorDeDados:
    def __init__(self, arquivo_json):
        self.arquivo_json = arquivo_json
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        """
        Carrega os dados do arquivo JSON
        """
        try:
            with open(self.arquivo_json, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def salvar_dados(self):
        """
        Salva os dados no arquivo JSON
        """
        with open(self.arquivo_json, 'w') as file:
            json.dump(self.dados, file, indent=4)

    def editar_ingrediente(self, nome_ingrediente, precos_por_mercado):
        """
        adiciona um ingrediente no arquivo JSON
        """
        self.dados[nome_ingrediente] = precos_por_mercado
        self.salvar_dados()

    def deletar_ingrediente(self, nome_ingrediente):
        """
        Remove ingrediente do arquivo JSON.
        """
        if nome_ingrediente in self.dados:
            del self.dados[nome_ingrediente]
            self.salvar_dados()
