import sqlite3
import os

# --- Inicialização ---
def inicializar_banco():
    if not os.path.exists('data'):
        os.makedirs('data')
    conexao = sqlite3.connect('data/sistema.db')
    cursor = conexao.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

# --- FUNÇÃO DE CADASTRAR ---
def cadastrar_venda():
    print("\n" + "="*30)
    print("      NOVO CADASTRO")
    print("="*30)

    # 1. Coleta de dados do usuário
    nome_produto = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))
    preco = float(input("Valor unitário: "))
    data_venda = input("Data (ex: 31/03/2026): ")

    try:
        
        conexao = sqlite3.connect('data/sistema.db')
        cursor = conexao.cursor()

        # 3. Comando SQL para Inserir 
        sql = ''' INSERT INTO vendas (produto, quantidade, valor, data) VALUES (?, ?, ?, ?) '''
        
        # 4. Executar a ordem passando os dados coletados nos inputs
        cursor.execute(sql, (nome_produto, qtd, preco, data_venda))

        # 5. Salvar a alteração
        conexao.commit()
        print(f"\n✅ Sucesso: {nome_produto} adicionado ao sistema!")

    except Exception as e:
        print(f"\n❌ Erro ao salvar no banco: {e}")
    
    finally:
        
        conexao.close()

# Testando as duas funções
if __name__ == "__main__":
    inicializar_banco() 
    cadastrar_venda()   
