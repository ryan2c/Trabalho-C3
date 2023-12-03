import sqlite3
import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.geometry("330x450")
  

# Conectar ao banco de dados SQLite (será criado se não existir)
conexao = sqlite3.connect('trabalho_C3.db')

# Criar um cursor
c = conexao.cursor()

# Executar o comando SQL para criar a tabela
c.execute('''
    CREATE TABLE IF NOT EXISTS clientes3 (
        nome TEXT,
        sobrenome TEXT,
        endereco TEXT,
        cep TEXT,
        telefone TEXT,
        empresa TEXT,
        data_contratacao TEXT,
        foto TEXT,
        cidade TEXT,
        cargo TEXT,
        salario REAL,
        departamento TEXT
    )
''')

def cadastrar_cliente():
    conexao = sqlite3.connect('trabalho_C3.db')
    c = conexao.cursor()
    # Inserir dados na tabela:
    c.execute("""
        INSERT INTO trabalho_C3 (
            nome, sobrenome, endereco, cep, telefone,
            empresa, data_contratacao, foto, cidade,
            cargo, salario, departamento
        ) VALUES (
            :nome, :sobrenome, :endereco, :cep, :telefone,
            :empresa, :data_contratacao, :foto, :cidade,
            :cargo, :salario, :departamento
        )""",
        {
            'nome': entry_nome.get(),
            'sobrenome': entry_sobrenome.get(),
            'endereco': entry_endereco.get(),
            'cep': entry_cep.get(),
            'telefone': entry_telefone.get(),
            'empresa': entry_empresa.get(),
            'data_contratacao': entry_data_contratacao.get(),
            'foto': entry_foto.get(),
            'cidade': entry_cidade.get(),
            'cargo': entry_cargo.get(),
            'salario': entry_salario.get(),
            'departamento': entry_departamento.get(),
        })
    # Commit as mudanças:
    conexao.commit()
    # Apaga os valores das caixas de entrada
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_endereco.delete(0, "end")
    entry_cep.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_empresa.delete(0, "end")
    entry_data_contratacao.delete(0, "end")
    entry_foto.delete(0, "end")
    entry_cidade.delete(0, "end")
    entry_cargo.delete(0, "end")
    entry_salario.delete(0, "end")
    entry_departamento.delete(0, "end")

# ... (rest of your code)

# Rótulos Entradas:
# ... (previous labels)

# Novos Rótulos Entradas:
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)
label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)
label_endereco = tk.Label(janela, text='Endereço')
label_endereco.grid(row=5, column=0, padx=10, pady=10)
label_cep = tk.Label(janela, text='CEP')
label_cep.grid(row=6, column=0, padx=10, pady=10)
label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=7, column=0, padx=10, pady=10)
label_empresa = tk.Label(janela, text='Empresa')
label_empresa.grid(row=8, column=0, padx=10, pady=10)
label_data_contratacao = tk.Label(janela, text='Data Contratação')
label_data_contratacao.grid(row=9, column=0, padx=10, pady=10)
label_foto = tk.Label(janela, text='Foto')
label_foto.grid(row=10, column=0, padx=10, pady=10)
label_cidade = tk.Label(janela, text='Cidade')
label_cidade.grid(row=11, column=0, padx=10, pady=10)
label_cargo = tk.Label(janela, text='Cargo')
label_cargo.grid(row=12, column=0, padx=10, pady=10)
label_salario = tk.Label(janela, text='Salário')
label_salario.grid(row=13, column=0, padx=10, pady=10)
label_departamento = tk.Label(janela, text='Departamento')
label_departamento.grid(row=14, column=0, padx=10, pady=10)

# Novas Caixas Entradas:
entry_nome = tk.Entry(janela, width=35)
entry_nome.grid(row=0, column=1, padx=10, pady=10)
entry_sobrenome = tk.Entry(janela, width=35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)
entry_endereco = tk.Entry(janela, width=35)
entry_endereco.grid(row=5, column=1, padx=10, pady=10)
entry_cep = tk.Entry(janela, width=35)
entry_cep.grid(row=6, column=1, padx=10, pady=10)
entry_telefone = tk.Entry(janela, width=35)
entry_telefone.grid(row=7, column=1, padx=10, pady=10)
entry_empresa = tk.Entry(janela, width=35)
entry_empresa.grid(row=8, column=1, padx=10, pady=10)
entry_data_contratacao = tk.Entry(janela, width=35)
entry_data_contratacao.grid(row=9, column=1, padx=10, pady=10)
entry_foto = tk.Entry(janela, width=35)
entry_foto.grid(row=10, column=1, padx=10, pady=10)
entry_cidade = tk.Entry(janela, width=35)
entry_cidade.grid(row=11, column=1, padx=10, pady=10)
entry_cargo = tk.Entry(janela, width=35)
entry_cargo.grid(row=12, column=1, padx=10, pady=10)
entry_salario = tk.Entry(janela, width=35)
entry_salario.grid(row=13, column=1, padx=10, pady=10)
entry_departamento = tk.Entry(janela, width=35)
entry_departamento.grid(row=14, column=1, padx=10, pady=10)

def cadastrar_cliente():
    conexao = sqlite3.connect('trabalho_C3.db')
    c = conexao.cursor()
    c.execute("""
        INSERT INTO clientes3 (
            nome, sobrenome, endereco, cep, telefone,
            empresa, data_contratacao, foto, cidade,
            cargo, salario, departamento
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            entry_nome.get(),
            entry_sobrenome.get(),
            entry_endereco.get(),
            entry_cep.get(),
            entry_telefone.get(),
            entry_empresa.get(),
            entry_data_contratacao.get(),
            entry_foto.get(),
            entry_cidade.get(),
            entry_cargo.get(),
            entry_salario.get(),
            entry_departamento.get(),
        )
    )
    conexao.commit()
    limpar_campos()

# Function to clear entry fields after saving
def limpar_campos():
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_endereco.delete(0, "end")
    entry_cep.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_empresa.delete(0, "end")
    entry_data_contratacao.delete(0, "end")
    entry_foto.delete(0, "end")
    entry_cidade.delete(0, "end")
    entry_cargo.delete(0, "end")
    entry_salario.delete(0, "end")
    entry_departamento.delete(0, "end")

def ordenar_clientes():
    conexao = sqlite3.connect('trabalho_C3.db')
    c = conexao.cursor()
    c.execute("SELECT * FROM clientes3 ORDER BY nome ASC;")
    for linha in c.fetchall():
        print(linha)
    conexao.commit()
    conexao.close()


def listar_cliente():
    conexao = sqlite3.connect('trabalho_C3.db')
    c = conexao.cursor()
    c.execute("SELECT * FROM clientes3;")
    resultado = c.fetchall()
    colunas = [descricao[0] for descricao in c.description]  # Obtém os nomes das colunas
    conexao.close()

    # Criar e mostrar a segunda janela
    segunda_janela = tk.Toplevel(janela)
    segunda_janela.title("Lista de Todos os Clientes")
    segunda_janela.geometry("600x300")

    tree = ttk.Treeview(segunda_janela, columns=tuple(range(len(colunas))), show="headings")

    for i, coluna in enumerate(colunas):
        tree.heading(i, text=coluna)
        tree.column(i, width=100)

    for linha in resultado:
        tree.insert("", "end", values=linha)

    tree.pack(expand=True, fill='both')

def contar_clientes():
    conexao = sqlite3.connect('trabalho_C3.db')
    c = conexao.cursor()
    c.execute('SELECT COUNT(*) FROM clientes3')
    total_clientes = c.fetchone()[0]
    print("Total de clientes:", total_clientes)
    conexao.commit()
    conexao.close()

# ... (previous code)

# Function to consult a client
def consultar_cliente():
    # Criação da janela de consulta
    janela_consulta = tk.Toplevel(janela)
    janela_consulta.title("Consulta de Cliente")
    janela_consulta.geometry("400x200")

    # Rótulo e entrada para o nome
    label_nome_consulta = tk.Label(janela_consulta, text="Nome:")
    label_nome_consulta.grid(row=0, column=0, padx=10, pady=10)
    entry_nome_consulta = tk.Entry(janela_consulta)
    entry_nome_consulta.grid(row=0, column=1, padx=10, pady=10)

    # Botão para realizar a consulta
    botao_consultar = tk.Button(janela_consulta, text="Consultar", command=lambda: realizar_consulta(entry_nome_consulta.get()))
    botao_consultar.grid(row=1, column=0, columnspan=2, pady=10)

def realizar_consulta(nome_consulta):
    conexao = sqlite3.connect('trabalho_C3.db')
    c = conexao.cursor()
    c.execute("SELECT * FROM clientes3 WHERE nome = ?;", (nome_consulta,))
    resultado = c.fetchall()
    if resultado:
        criar_segunda_janela("Consulta de Cliente", [["Nome", "Sobrenome", "Endereço", "CEP", "Telefone",
                                                       "Empresa", "Data Contratação", "Foto", "Cidade",
                                                       "Cargo", "Salário", "Departamento"]] + resultado)
    else:
        print("Cliente não encontrado.")
    conexao.close()
def criar_segunda_janela(titulo, dados):
    segunda_janela = tk.Toplevel(janela)
    segunda_janela.title(titulo)
    segunda_janela.geometry("500x300")

    # Criar uma treeview para exibir os dados
    tree = ttk.Treeview(segunda_janela, columns=tuple(range(len(dados[0]))), show="headings")

    for i, coluna in enumerate(dados[0]):
        tree.heading(i, text=coluna)
        tree.column(i, width=100)  # Ajuste a largura da coluna conforme necessário

    # Preencher a treeview com os dados
    for linha in dados[1:]:
        tree.insert("", "end", values=linha)

    tree.pack(expand=True, fill='both')

# Function to delete a client
def excluir_cliente():
    # Criação da janela de exclusão
    janela_exclusao = tk.Toplevel(janela)
    janela_exclusao.title("Excluir Cliente")
    janela_exclusao.geometry("400x200")

    # Rótulo e entrada para o nome
    label_nome_exclusao = tk.Label(janela_exclusao, text="Nome:")
    label_nome_exclusao.grid(row=0, column=0, padx=10, pady=10)
    
    entry_nome_exclusao = tk.Entry(janela_exclusao)
    entry_nome_exclusao.grid(row=0, column=1, padx=10, pady=10)

    # Rótulo e entrada para o sobrenome
    label_sobrenome_exclusao = tk.Label(janela_exclusao, text="Sobrenome:")
    label_sobrenome_exclusao.grid(row=1, column=0, padx=10, pady=10)
    
    entry_sobrenome_exclusao = tk.Entry(janela_exclusao)
    entry_sobrenome_exclusao.grid(row=1, column=1, padx=10, pady=10)

    # Botão para realizar a exclusão
    botao_excluir = tk.Button(janela_exclusao, text="Excluir", command=lambda: realizar_exclusao(entry_nome_exclusao.get(), entry_sobrenome_exclusao.get()))
    botao_excluir.grid(row=2, column=0, columnspan=2, pady=10)

def realizar_exclusao(nome_exclusao, sobrenome_exclusao):
    conexao = sqlite3.connect('trabalho_C3.db')
    c = conexao.cursor()
    c.execute("DELETE FROM clientes3 WHERE nome = ? AND sobrenome = ?;", (nome_exclusao, sobrenome_exclusao))
    if c.rowcount > 0:
        print(f"Cliente {nome_exclusao} {sobrenome_exclusao} excluído com sucesso.")
        listar_cliente()  # Atualizar a lista após excluir
    else:
        print(f"Cliente {nome_exclusao} {sobrenome_exclusao} não encontrado.")
    conexao.commit()
    conexao.close()




# Botão de Gravar (Save)
botao_gravar = tk.Button(text='Gravar no Banco', command=cadastrar_cliente)
botao_gravar.grid(row=15, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

# Botão de Listar (List)
botao_listar = tk.Button(text='Listar Clientes', command=listar_cliente)
botao_listar.grid(row=16, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Botão de Consultar (Query)
botao_consultar = tk.Button(text='Consultar Clientes', command=consultar_cliente)
botao_consultar.grid(row=17, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Botão de Ordenar (Sort)
botao_ordenar = tk.Button(text='Ordenar Clientes', command=ordenar_clientes)
botao_ordenar.grid(row=18, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Botão de Excluir (Delete)
botao_excluir = tk.Button(text='Excluir Cliente', command=excluir_cliente)
botao_excluir.grid(row=19, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# Botão de Contar (Count)
botao_contar = tk.Button(text='Total de Clientes', command=contar_clientes)
botao_contar.grid(row=20, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

# ... (rest of your code)


janela.mainloop()
