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

if __name__=='__main__':
    print("Inicializando Banco de dados...")
    create_tables()
    print("Banco de dados inicializado com sucesso!")              