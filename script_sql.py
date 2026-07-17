import sqlite3
def cria_conexao_ou_tabela_sql():
    conexao = sqlite3.connect("empresa.db")
    cursor = conexao.cursor()
    script_sql = """
        CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        departamento TEXT NOT NULL
    );"""
    cursor.execute(script_sql)
    conexao.commit()
    conexao.close()

def insere_dados_funcionario_na_tabela(tupla_de_funcionario):
    try:
        conexao = sqlite3.connect("empresa.db")
        cursor = conexao.cursor()
        script_sql = """
        INSERT INTO funcionarios (nome, email, departamento)
        VALUES(?,?,?);"""
        cursor.execute(script_sql, tupla_de_funcionario)
        conexao.commit()

    except sqlite3.Error as erro:
        print(f"\n[ERRO SQL]: Não foi possível inserir os dados. DETALHE: {erro}")
        
    finally:
        conexao.close()

def esquecer():
    try:
        id_para_esquecer = input("Digite o id para remoção: ")
        conexao = sqlite3.connect("empresa.db")
        cursor = conexao.cursor()
        script_sql = F"""
        DELETE FROM funcionarios
        WHERE id = {id_para_esquecer}"""
        cursor.execute(script_sql)
        conexao.commit()
        print("A remoção completa foi realizada com sucesso")

    except sqlite3.Error as erro:
        print(f"\n[ERRO SQL]: Não foi possível remover os dados. DETALHE: {erro}")
        
    finally:
        conexao.close()