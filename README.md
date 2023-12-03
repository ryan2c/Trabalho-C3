# Trabalho-C3

Formulário de Clientes.

Integrantes:
Ryan Cardoso Comper
Isabella Magnago

Descrição:
Este projeto consiste em um formulário de clientes implementado em Python, utilizando a biblioteca Tkinter para a interface gráfica e SQLite como banco de dados.

Funcionalidades:
Cadastro de clientes
Listagem de clientes
Consulta, ordenação e exclusão de clientes
Contagem total de clientes

Pré-requisitos:
Python 3.x instalado na máquina
Biblioteca Tkinter (geralmente já incluída na instalação padrão do Python)
Banco de dados SQLite

#Conectando banco de dados local 

Conectar ao Banco de Dados
conexao = sqlite3.connect('trabalho_C3.db')
c = conexao.cursor()

Exemplo de Operação no Banco de Dados
c.execute("SELECT * FROM clientes3;")
resultado = c.fetchall()

Fechar Conexão
conexao.close()
