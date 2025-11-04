# backend/tests/test_database.py (Versão Inversa e Funcional)

import pytest
import sqlite3
from unittest.mock import patch, MagicMock
import database 

# ------------------------------------------------------------
# 1. FIXTURE (Conexão REAL para verificação)
# ------------------------------------------------------------

@pytest.fixture
def real_conn():
    """Cria uma conexão real na memória para usarmos na verificação dos dados."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close() 

# ------------------------------------------------------------
# 2. FIXTURE (Mock da Conexão para a função sob teste)
# ------------------------------------------------------------

@pytest.fixture
def mock_conn(real_conn):
    """Cria um Mock que simula a conexão e usa o .cursor() da conexão real."""
    
    # Criamos um Mock que simula ter um método cursor() e commit()
    conn_mock = MagicMock()
    
    # 1. Mock do .cursor(): Garantimos que o cursor é o cursor da conexão REAL
    conn_mock.cursor.return_value = real_conn.cursor()
    
    # 2. Mock do .commit(): Garantimos que o commit é o commit da conexão REAL
    conn_mock.commit.side_effect = real_conn.commit
    
    # 3. Controlamos o .close() para verificarmos se foi chamado
    conn_mock.close = MagicMock()
    
    yield conn_mock

# ----------------------------------------------------------------------------------
# 3. TESTES: Funções de Banco de Dados
# ----------------------------------------------------------------------------------

# MOCKAMOS o get_db_connection para que ele retorne o Mock da Conexão
@patch('database.get_db_connection')
def test_create_tables_sucesso(mock_get_conn, real_conn, mock_conn):
    
    # 1. SETUP: get_db_connection sempre retorna o Mock da Conexão
    mock_get_conn.return_value = mock_conn

    # Ação: Chamamos a função (ela usa o mock_conn, mas o cursor é real)
    database.create_tables()

    # Verificação: Consultamos a conexão REAL para ver se a tabela existe
    cursor = real_conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tarefa'")
    tabela_existe = cursor.fetchone()

    # Assertivas
    assert tabela_existe is not None, "A tabela 'tarefa' não foi encontrada."
    assert tabela_existe['name'] == 'tarefa'
    
    # Verifica se o .close() foi chamado
    mock_conn.close.assert_called_once() 


# ADICIONAMOS OS OUTROS DOIS TESTES
@patch('database.get_db_connection')
def test_get_all_tarefas_com_dados(mock_get_conn, real_conn, mock_conn):
    mock_get_conn.return_value = mock_conn

    # Inserimos a tabela (usando o mock para a função, mas a conexão real para a verificação)
    database.create_tables()
    
    # Inserção direta na conexão REAL (para simular o estado inicial)
    cursor = real_conn.cursor()
    sql_insert = "INSERT INTO tarefa (titulo, descricao, status) VALUES (?, ?, ?)"
    cursor.execute(sql_insert, ("Pagar Contas", "Aluguel e energia", "pendente"))
    real_conn.commit()

    # Ação: Chamamos a função sob teste
    tarefas = database.get_all_tarefas()
    
    assert len(tarefas) == 1
    assert tarefas[0]['titulo'] == "Pagar Contas"
    
    # Asserção de Chamadas: get_db_connection() foi chamado uma vez em create_tables e uma vez em get_all_tarefas
    assert mock_conn.close.call_count == 2


@patch('database.get_db_connection')
def test_get_all_tarefas_vazio(mock_get_conn, real_conn, mock_conn):
    mock_get_conn.return_value = mock_conn
    
    # Cria a tabela
    database.create_tables() 
    
    # Ação
    tarefas = database.get_all_tarefas()
    
    assert len(tarefas) == 0
    
    # Asserção de Chamadas
    assert mock_conn.close.call_count == 2