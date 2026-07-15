import sqlite3
from funcionarios import faz_cadastro

def cria_conexao_ou_tabela_sql():
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()

    script_sql = """
        CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        departamento TEXT NOT NULL
    );
    """
    cursor.execute(script_sql)
    conexao.commit()
    conexao.close()

def insere_dados_funcionario_na_tabela(tupla_de_funcionario):
    pass