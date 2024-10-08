# Xmath - Projeto de Álgebra Linear

O **Xmath** é uma aplicação desenvolvida em Python que permite o gerenciamento de preços de lanches, calculando automaticamente o custo de cada lanche com base nos ingredientes e nos diferentes preços em mercados. O sistema ajusta os preços com uma margem de lucro e oferece uma interface para editar e cadastrar novos ingredientes.

## Funcionalidades Principais
- Cadastro e edição de ingredientes.
- Cálculo de preços de lanches (X-Determinante e X-Identidade) com base no mercado mais barato.
- Interface para visualizar os preços ajustados com margem de lucro.
- Integração com arquivos JSON para armazenamento dos dados de mercados e ingredientes.

## Tecnologias Utilizadas
- **Python 3.x**: Linguagem de programação principal.
- **Tkinter**: Para criação da interface gráfica.
- **JSON**: Para armazenamento de dados de ingredientes e mercados.

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Python 3.x](https://www.python.org/downloads/)
- Um editor de código, como [Visual Studio Code](https://code.visualstudio.com/) ou [PyCharm](https://www.jetbrains.com/pycharm/).

## Instalação

### 1. Clone o repositório

Use o comando `git clone https://github.com/AthosSperber/Xmath.git` para clonar o repositório.

### 2. Navegue até o diretório do projeto

Utilize `cd Xmath` para entrar na pasta do projeto.

### 3. Execute a aplicação

Para iniciar a aplicação, execute `python main.py`.

## Como Utilizar

1. **Cadastro de Ingredientes**: Na interface, você pode adicionar novos ingredientes e seus respectivos preços em mercados diferentes. A aplicação faz o cálculo automático para encontrar o mercado mais barato.
2. **Visualização dos Lanches**: Na tela principal, você pode visualizar os ingredientes de cada lanche (X-Determinante e X-Identidade), o mercado mais barato para cada ingrediente, e o preço total com margem de lucro.
3. **Gerenciamento de Dados**: Todos os dados inseridos são armazenados em um arquivo JSON, permitindo fácil acesso e manipulação futura.

## Estrutura de Arquivos

- `main.py`: Arquivo principal que executa a aplicação.
- `gerenciador_de_dados.py`: Classe responsável por gerenciar o arquivo JSON de ingredientes e mercados.
- `interface.py`: Implementação da interface gráfica com Tkinter.
- `ingredientes.json`: Arquivo JSON para armazenar os dados dos ingredientes e mercados.

