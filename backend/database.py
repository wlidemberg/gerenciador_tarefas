import sqlite3

DATABASE_FILE = 'tarefas.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)

    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    sql_create_tarefa_table = """
    CREATE TABLE IF NOT EXISTS tarefa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        status TEXT NOT NULL DEFAULT 'pendente'
    );
    """
    conn = None 
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(sql_create_tarefa_table)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        if conn:
            conn.close()  
def get_all_tarefas():
    conn = None
    tarefas = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM tarefa"

        cursor.execute(sql)

        resultados_row = cursor.fetchall()

        tarefas = [dict(row) for row in resultados_row]

    except sqlite3.Error as e:
        print(f"Erro ao buscar tarefas: {e}")
    finally:
        if conn:
            conn.close()
    return tarefas        


def add_tarefa(titulo, descricao, status='pendente'):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Comando SQL para inserir a tarefa
    sql_insert = """
    INSERT INTO tarefa (titulo, descricao, status)
    VALUES (?, ?, ?)
    """
    
    # 2. Executa o comando, passando a descrição como None se não for fornecida
    cursor.execute(sql_insert, (titulo, descricao or '', status))
    
    # 3. Commita a transação
    conn.commit()
    
    # 4. Obtém o ID da última linha inserida
    tarefa_id = cursor.lastrowid
    
    # 5. Obtém a tarefa completa (útil para retornar na API)
    cursor.execute("SELECT * FROM tarefa WHERE id = ?", (tarefa_id,))
    nova_tarefa = cursor.fetchone()
    
    conn.close()
    
    # Converte o objeto Row para dict antes de retornar (se necessário)
    if nova_tarefa:
        return dict(nova_tarefa) 
    return None

def update_tarefa(tarefa_id, titulo=None, descricao=None, status=None):
    """
    Atualiza uma tarefa no banco de dados e retorna a tarefa atualizada.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query SQL para atualizar a tarefa. 
    # Usamos WHERE id = ? para garantir que apenas a tarefa correta seja modificada.
    sql = "UPDATE tarefa SET titulo=?, descricao=?, status=? WHERE id=?"

    cursor.execute(sql, (titulo, descricao, status, tarefa_id))
    conn.commit()

    # Verificamos quantas linhas foram afetadas para saber se a tarefa existia
    rows_affected = cursor.rowcount

    if rows_affected == 0:
        conn.close()
        return None  # Tarefa não encontrada
    
    cursor.execute = ("SELECT * FROM tarefa WHERE id=?", (tarefa_id))
    tarefa_atualizada = cursor.fetchone()

    conn.close()

    if tarefa_atualizada:
        return dict(tarefa_atualizada)
    return None

def delete_tarefa(tarefa_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql_delete = "DELETE FROM tarefas WHERE id=?"
    cursor.execute(sql_delete, (tarefa_id,))
    conn.commit()

    # Retorna o número de linhas que foram excluídas
    rows_affected = cursor.rowcount

    conn.close()

    return rows_affected

def get_tarefa_by_id(tarefa_id):
    """ Busca uma única tarefa pelo seu ID """

    conn  =get_db_connection()
    cursor = conn.cursor()

    # Busca a tarefa pelo ID
    sql = "SELECT * FROM tarefa WHERE id=?"
    cursor.execute(sql, (tarefa_id))
    tarefa = cursor.fetchone()

    if tarefa:
        return dict(tarefa) # Retorna como dicionário
    return None # Retorna None se não encontar


if __name__=='__main__':
    print("Inicializando Banco de dados...")
    create_tables()
    print("Banco de dados inicializado com sucesso!")              