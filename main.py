import tkinter as tk
from tkinter import ttk, messagebox
from dados import GerenciadorDeDados
from ingrediente import Ingrediente


dados = GerenciadorDeDados("ingredientes.json")

def calcular_total_sanduiche(ingredientes_sanduiche):
    total = 0
    detalhes_ingredientes = []
    
    for ingrediente_nome, quantidade_necessaria in ingredientes_sanduiche.items():
        ingrediente = Ingrediente(ingrediente_nome, dados)
        mercado, preco_unidade = ingrediente.mercado_mais_barato()
        
        if mercado:
            quantidade_comprada = float(ingrediente.precos_por_mercado[mercado]["quantidade"])
            unidade = ingrediente.precos_por_mercado[mercado]["unidade"]
            
            if unidade == "gramas":
                preco_total = (preco_unidade / quantidade_comprada) * quantidade_necessaria
            else:
                preco_total = (preco_unidade / quantidade_comprada) * quantidade_necessaria
            
            total += preco_total
            detalhes_ingredientes.append((ingrediente_nome, mercado, preco_unidade, quantidade_necessaria, preco_total))
    
    lucro_total = total * 1.7 
    return detalhes_ingredientes, total, lucro_total


def atualizar_tabela_sanduiches():
    tabela_sanduiches.delete(*tabela_sanduiches.get_children())
    
    # Ingredientes de cada sanduíche
    xDeterminante = {"pão": 1, "carne": 2, "queijo": 60, "presunto": 80, "ovo": 1}
    xIdentidade = {"pão": 1, "carne": 1, "queijo": 30, "presunto": 40, "ovo": 0}

    # Calculando totais e mercados mais baratos para cada sanduíche
    detalhes_1, total_1, lucro_1 = calcular_total_sanduiche(xDeterminante)
    detalhes_2, total_2, lucro_2 = calcular_total_sanduiche(xIdentidade)

    tabela_sanduiches.insert('', 'end', values=("Preço Total", f"R$ {total_1:.2f}", f"R$ {total_2:.2f}"))
    tabela_sanduiches.insert('', 'end', values=("Preço com Lucro", f"R$ {lucro_1:.2f}", f"R$ {lucro_2:.2f}"))

# Função para atualizar a tabela de ingredientes
def atualizar_tabela_ingredientes():
    tabela_ingredientes.delete(*tabela_ingredientes.get_children())

    xDeterminante = {"pão": 1, "carne": 2, "queijo": 60, "presunto": 80, "ovo": 1}
    xIdentidade = {"pão": 1, "carne": 1, "queijo": 30, "presunto": 40, "ovo": 0}
    
    # Unindo todos os ingredientes utilizados nos sanduíches
    todos_ingredientes = {**xDeterminante, **xIdentidade}

    for ingrediente_nome in todos_ingredientes.keys():
        ingrediente = Ingrediente(ingrediente_nome, dados)
        mercado, preco_unidade = ingrediente.mercado_mais_barato()
        
        if mercado:
            quantidade_comprada = float(ingrediente.precos_por_mercado[mercado]["quantidade"])
            unidade = ingrediente.precos_por_mercado[mercado]["unidade"]
            preco_pago = preco_unidade

            # Quantidade usada em cada sanduíche
            quantidade_uso_determinante = xDeterminante.get(ingrediente_nome, 0)
            quantidade_uso_identidade = xIdentidade.get(ingrediente_nome, 0)
            
            # Adicionando os dados na tabela
            tabela_ingredientes.insert('', 'end', values=(
                ingrediente_nome, mercado, f"{quantidade_comprada} {unidade}", f"R$ {preco_pago:.2f}",
                quantidade_uso_determinante, quantidade_uso_identidade
            ))

# Função para mostrar/ocultar o formulário de cadastro de ingredientes
def toggle_cadastro_ingrediente():
    if frame_cadastro.winfo_ismapped():
        frame_cadastro.grid_remove()
    else:
        frame_cadastro.grid(row=8, column=0, columnspan=6)



def adicionar_ingrediente():
    nome = nome_ingrediente.get()
    quantidade = quantidade_ingrediente.get()
    unidade = unidade_compra.get()
    mercado = mercado_ingrediente.get()
    preco = preco_ingrediente.get()

    if nome and quantidade and unidade and mercado and preco:
        try:
            preco = float(preco)
            quantidade = float(quantidade)
            ingrediente = Ingrediente(nome, dados)
            ingrediente.adicionar_preco(mercado, preco, quantidade, unidade, dados)
            messagebox.showinfo("Sucesso", f"Ingrediente '{nome}' adicionado com sucesso!")
            atualizar_tabela_sanduiches()
            atualizar_tabela_ingredientes()
        except ValueError:
            messagebox.showerror("Erro", "O preço e a quantidade devem ser valores numéricos.")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos.")



def excluir_ingrediente():
    selecionado = tabela_ingredientes.selection()
    if not selecionado:
        messagebox.showwarning("Seleção Inválida", "Selecione um ingrediente para excluir.")
        return

    ingrediente_nome = tabela_ingredientes.item(selecionado)["values"][0]

    # Remover o ingrediente do arquivo JSON
    dados.deletar_ingrediente(ingrediente_nome)
    messagebox.showinfo("Sucesso", f"Ingrediente '{ingrediente_nome}' excluído com sucesso!")

    atualizar_tabela_sanduiches()
    atualizar_tabela_ingredientes()


# Criando a janela principal
janela = tk.Tk()
janela.title("Lanchonete X-Math")

# Tabela de sanduíches
colunas_sanduiches = ('', 'X-Determinante', 'X-Identidade')
tabela_sanduiches = ttk.Treeview(janela, columns=colunas_sanduiches, show='headings', height=4)
for col in colunas_sanduiches:
    tabela_sanduiches.heading(col, text=col)
    tabela_sanduiches.column(col, width=150)
tabela_sanduiches.grid(row=0, column=0, columnspan=3)


# Tabela de ingredientes
colunas_ingredientes = ('Ingrediente', 'Mercado com melhor preço', 'Quantidade Comprada', 'Preço Pago', 'Qtde X-Determinante', 'Qtde X-Identidade')
tabela_ingredientes = ttk.Treeview(janela, columns=colunas_ingredientes, show='headings', height=10)
for col in colunas_ingredientes:
    tabela_ingredientes.heading(col, text=col)
    tabela_ingredientes.column(col, width=150)
tabela_ingredientes.grid(row=1, column=0, columnspan=6)


# Botão para mostrar/ocultar cadastro de ingrediente
btn_toggle_cadastro = tk.Button(janela, text="Cadastrar Ingrediente", command=toggle_cadastro_ingrediente)
btn_toggle_cadastro.grid(row=7, column=0, pady=10)


# Botão para excluir ingrediente
btn_excluir_ingrediente = tk.Button(janela, text="Excluir Ingrediente", command=excluir_ingrediente)
btn_excluir_ingrediente.grid(row=7, column=1, pady=10)


# Frame de cadastro de ingredientes
frame_cadastro = tk.Frame(janela)

tk.Label(frame_cadastro, text="Nome do Ingrediente:").grid(row=0, column=0)
nome_ingrediente = tk.Entry(frame_cadastro)
nome_ingrediente.grid(row=0, column=1)

tk.Label(frame_cadastro, text="Quantidade:").grid(row=1, column=0)
quantidade_ingrediente = tk.Entry(frame_cadastro)
quantidade_ingrediente.grid(row=1, column=1)

tk.Label(frame_cadastro, text="Unidade:").grid(row=2, column=0)
unidade_compra = ttk.Combobox(frame_cadastro, values=["unidade", "gramas", "litros"])
unidade_compra.grid(row=2, column=1)
unidade_compra.current(0)

tk.Label(frame_cadastro, text="Mercado:").grid(row=3, column=0)
mercado_ingrediente = tk.Entry(frame_cadastro)
mercado_ingrediente.grid(row=3, column=1)

tk.Label(frame_cadastro, text="Preço:").grid(row=4, column=0)
preco_ingrediente = tk.Entry(frame_cadastro)
preco_ingrediente.grid(row=4, column=1)

btn_adicionar_ingrediente = tk.Button(frame_cadastro, text="Adicionar Ingrediente", command=adicionar_ingrediente)
btn_adicionar_ingrediente.grid(row=5, column=0, pady=10, columnspan=2)

atualizar_tabela_sanduiches()
atualizar_tabela_ingredientes()



janela.mainloop()
