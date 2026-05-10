import sqlite3

def conectar():
    """Função auxiliar para conectar ao banco de dados."""
    return sqlite3.connect('data/sistema.db')

# --- FUNÇÃO DE DELETAR (Sua parte: Remoção) ---
def deletar_venda():
    print("\n" + "="*30)
    print("      EXCLUIR REGISTRO")
    print("="*30)

    # Solicita o ID (que o Helys vai exibir na lista dele)
    id_venda = input("Digite o ID da venda que deseja deletar: ")

    # Validação de segurança: Essencial para não apagar por erro
    confirmar = input(f"Tem certeza que deseja excluir o ID {id_venda}? (s/n): ").lower()

    if confirmar == 's':
        try:
            conexao = conectar()
            cursor = conexao.cursor()

            # Executa o comando SQL DELETE
            cursor.execute("DELETE FROM vendas WHERE id = ?", (id_venda,))
            
            # Verifica se o ID realmente existia no banco
            if cursor.rowcount > 0:
                conexao.commit()
                print(f"\n✅ Registro {id_venda} removido com sucesso!")
            else:
                print(f"\n⚠️ ID {id_venda} não encontrado.")

        except Exception as e:
            print(f"\n❌ Erro ao deletar: {e}")
        finally:
            conexao.close()
    else:
        print("\n❌ Operação cancelada.")

# --- FUNÇÃO DE EDITAR (Sua parte: Atualização) ---
def editar_venda():
    print("\n" + "="*30)
    print("      EDITAR REGISTRO")
    print("="*30)

    id_venda = input("Digite o ID da venda que deseja editar: ")

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        # Primeiro, buscamos os dados atuais para mostrar ao usuário
        cursor.execute("SELECT * FROM vendas WHERE id = ?", (id_venda,))
        venda = cursor.fetchone()

        if venda:
            print(f"\nDados atuais: {venda[1]} | Qtd: {venda[2]} | Valor: {venda[3]}")
            
            # Coleta novos dados (se deixar vazio, mantém o atual)
            novo_nome = input("Novo nome (ou Enter para manter): ") or venda[1]
            nova_qtd = input("Nova quantidade (ou Enter para manter): ") or venda[2]
            novo_valor = input("Novo valor (ou Enter para manter): ") or venda[3]

            # Comando SQL UPDATE
            sql = "UPDATE vendas SET produto = ?, quantidade = ?, valor = ? WHERE id = ?"
            cursor.execute(sql, (novo_nome, int(nova_qtd), float(novo_valor), id_venda))
            
            conexao.commit()
            print("\n✅ Registro atualizado com sucesso!")
        else:
            print("\n⚠️ ID não encontrado.")

    except Exception as e:
        print(f"\n❌ Erro ao editar: {e}")
    finally:
        conexao.close()