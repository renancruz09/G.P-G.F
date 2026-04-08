import sqlite3

def inicializar_banco ():
    conexao = sqlite3.connect('banco.db/database.db')
    cursor = conexao.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS vendas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    produto TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    valor REAL NOT NULL,
                    data TEXT NOT NULL
                   )
''')
                
