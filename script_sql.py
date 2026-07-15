import sqlite3

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