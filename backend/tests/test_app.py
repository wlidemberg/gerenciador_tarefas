import pytest
import json
import sqlite3
from unittest.mock import patch, MagicMock
from app import app # importa o app Flask
import database # Importamos o módulo database para forçar o setup e mocking do DB

# ------------------------------------------------------------
# 1. FIXTURE (Conexão REAL para verificação)       
# ------------------------------------------------------------

@pytest.fixture
def client():
    """
    Cria um instância do Flask Test Client para fazermos requisições HTTP às rotas do app.
    O 'yield' garante que p contexto da aplicação seja desctruido após o teste.    
    """

    # Ativa o modo teste do Flask
    app.config['TESTING'] = True

    # Cria o cliente de teste
    with app.test_client() as client:
        # Executa o teste
        yield client

# ----------------------------------------------------------------------------------
# 2. FIXTURE: Mocking do banco de dados
# ----------------------------------------------------------------------------------

@pytest.fixture
def mock_db_data():
    """
    Mocka a função database.get_all_tarefas para retornar dados controlados
    em vez de acessar o banco de dados real.
    """

    # Dados de teste que o mock retornará
    dados_mockados = [
        {'id': 1, 'titulo': 'Comprar Pão', 'descricao': 'Pão francês', 'status': 'pendente'},
        {'id': 2, 'titulo': 'Pagar Água', 'descricao': 'Conta de novembro', 'status': 'concluída'}
    ]

    # Usamos o patch como um gerenciador de contexto (with)
    with patch('database.get_all_tarefas') as mock_get_all:
        mock_get_all.return_value = dados_mockados
        yield

# ----------------------------------------------------------------------------------
# 3. TESTE: GET /tarefas (com Mock de Dados)
# ----------------------------------------------------------------------------------

def test_get_tarefas_sucesso(client, mock_db_data):
    """
    Testa se a rota GET /tarefas retorna o código de status 200 e os dados mockados
    em formato JSON.
    """

    # Ação: Fazemos uma requisição GET simulada
    response = client.get('/tarefas')

    # Verificação (Assert):
    
    # 1. Status Code
    assert response.status_code == 200, f"Esperado 200, recebido {response.status_code}"

    # 2. Content Type
    assert response.content_type == 'application/json'

    # 3. Conteúdo dos Dados
    dados_retornados = json.loads(response.data)

    # Verifica a estrutura e o conteúdo dos dados mockados
    assert isinstance(dados_retornados, list)
    assert len(dados_retornados) == 2
    assert dados_retornados[0]['titulo'] == 'Comprar Pão'
    assert dados_retornados[1]['status'] == 'concluída'

# ----------------------------------------------------------------------------------
# 4. TESTE: POST /tarefas (Com Mock de Inserção)
# ----------------------------------------------------------------------------------

@patch('database.get_db_connection')
def test_post_tarefas_sucesso(mock_get_conn, client):
    """
    Testa se a rota POST /tarefas cria uma nova tarefa e retorna status 201,
    mockando a conexão para simular a inserção.
    """
    
    # 1. SETUP: Mock da Conexão
    mock_conn = MagicMock()
    mock_get_conn.return_value = mock_conn
    
    # Simula o retorno do ID da última linha inserida
    mock_conn.cursor.return_value.lastrowid = 99 # ID simulado
    
    # 2. SETUP: Dados que enviaremos no corpo da requisição
    dados_novatarefa = {
        'titulo': 'Fazer compras',
        'descricao': 'comprar ovos e leite'
    }

    # Ação: Fazemos uma requisição POST simulada
    response = client.post(
        '/tarefas', 
        data=json.dumps(dados_novatarefa), 
        content_type='application/json'
    )
    
    # Verificação (Assert):
    
    # 1. Status Code
    assert response.status_code == 201, f"Esperado 201, recebido {response.status_code}"
    
    # 2. Verifica se a lógica do banco de dados foi acionada
    mock_get_conn.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()
    
    # 3. Conteúdo da Resposta
    dados_retornados = json.loads(response.data)
    assert dados_retornados['id'] == 99 # Deve usar o ID simulado
    assert dados_retornados['titulo'] == 'Fazer compras'
    assert dados_retornados['status'] == 'pendente'


def test_post_tarefas_erro_validacao(client):
    """
    Testa se a rota POST /tarefas retorna erro 400 se o campo 'titulo' estiver faltando.
    """

    # SETUP: Dados inválidos (sem 'titulo')
    dados_invalidos = {
        'descricao':'tarefa sem titulo'
    }    

    # Ação: Requisição POST simulada
    response = client.post('/tarefas', data=json.dumps(dados_invalidos), content_type='application/json')

    # Verificação (Assert):
    # 1. Status Code
    assert response.status_code == 400, f'Esperado 400, recebido {response.status_code}'

    # 2. Mensagem de Erro
    dados_retornados = json.loads(response.data)
    assert 'erro' in dados_retornados
    assert 'O campo titulo é obrigatorio' in dados_retornados['erro']


# ----------------------------------------------------------------------------------
# 5. TESTE: PUT /tarefas/<id> (Atualização)
# ----------------------------------------------------------------------------------

@patch('database.update_tarefa')
def test_put_tarefa_sucesso(mock_update_tarefa, client):
    """
    Testa se a rota PUT /tarefas/<id> atualiza uma tarefa e retorna 200 OK.
    """  

    TAREFA_ID = 5

    # 1. SETUP: Dados que enviaremos para atualizar a tarefa
    dados_atualizacao = {
        'titulo':'Tarefa Atualizada',
        'descricao':'Descrição atualizada',
        'status':'concluída'
    }

    # 2. SETUP: Mockamos o retorno da função update_tarefa
    # Deve retornar o objeto completo atualizado
    tarefa_atualizada = {
        "id":TAREFA_ID,
        'titulo': dados_atualizacao['titulo'],
        'descricao':dados_atualizacao['descricao'],
        'status':dados_atualizacao['status']
    }

    mock_update_tarefa.return_value = tarefa_atualizada

    # Ação: Requisição PUT simulada
    response = client.put(
        f'/tarefas/{TAREFA_ID}',
        data=json.dumps(dados_atualizacao),
        content_type='application/json'
    )

    # Verificação (Assert)
    # 1. Status Code
    assert response.status_code == 200, f'Esperado 200, recebido {response.status_code}'

    # Verifica se a função de banco de dados foi chamada com os parametros corretos
    mock_update_tarefa.assert_called_once_with(
        tarefa_id=TAREFA_ID,
        titulo = dados_atualizacao['titulo'],
        descricao=dados_atualizacao['descricao'],
        status=dados_atualizacao['status']    
    )

    # 3. Conteúdo da Resposta
    dados_retornados = json.loads(response.data)
    assert dados_retornados['id'] == TAREFA_ID
    assert dados_retornados['titulo'] == 'Tarefa Atualizada'
    assert dados_retornados['status'] == 'concluída'

@patch('database.update_tarefa')
def test_put_tarefa_nao_encontrada(mock_update_tarefa, client):
    """
    Testa se a rota PUT /tarefas/<id> retorna 404 quando a tarefa não existe.
    """

    TAREFA_ID = 999

    # Arrange (prepara): Confugura o cenbario de teste (cria dados, inicializa objetos)
    # 1. SETUP: Mockamos(simulamos) o retorno como None, simulando que a terefa não foi encontrada 
    mock_update_tarefa.return_value = None

    # Act (ação): Executa o código que se quer testar
    # Requisição PUT simulada
    response = client.put(
        f'/tarefas/{TAREFA_ID}',
        data=json.dumps({'titulo':'Qualquer título'}),
        content_type='application/json'
    )

    # Assert (Afirma): Verifica se o  resultado da ação esta conforme esperado
    #  1. Status Code
    assert response.status_code == 404, f'Esperado 404, recebido {response.status_code}'

    # 2. Mensagem de Erro
    assert 'erro' in json.loads(response.data)
    assert f'Tarefa com ID {TAREFA_ID} não encontrada para atualização' in json.loads(response.data)['erro']

# ----------------------------------------------------------------------------------
# 6. TESTE: DELETE /tarefas/<id> (Exclusão)
# ----------------------------------------------------------------------------------
@patch('database.delete_tarefa')
def test_delete_tarefa_sucesso(mock_delete_tarefa, client):
    """ Testa se a rota DELETE /tarefas/<id> exclui a tarefa e retorna 204 no Content """
    TAREFA_ID = 10

    # SETUP: Mockamos o retorno com 1 (uma linha afetada, ou seja, sucesso)
    mock_delete_tarefa.return_value = 1

    # Ação: Requisição DELETE simulada
    response =client.delete(f"/tarefas/{TAREFA_ID}")

    # Verificação (Assert)
    # 1. Status Code
    assert response.status_code == 204, f"Esperado 204, obtido {response.status_code}"

    # 2. Verifica se a função de banco de dados foi chamada
    mock_delete_tarefa.assert_called_once_with(TAREFA_ID)

    # 3. Conteúdo de resposta (deve ser vazia para 204)
    assert response.data ==b''

@patch('database.delete_tarefa')
def test_delete_tarefa_nao_encontrada(mock_delete_tarefa, client):
    """ Testa se a rota DELETE /terefas/<id> retorna 404 quando a tarefa não existi """
    TAREFA_ID = 9999

    # SETUP: Mockamos o retorno com 0 (nenhuma linha afetda, ou seja, falha)
    mock_delete_tarefa.return_value = 0

    # Ação: Requisiçãp DELETE simulada
    response = client.delete(f"/tarefas/{TAREFA_ID}")

    # Verificação (Assert)

    # 1. Status Code
    assert response.status_code == 404, f"Esperado 404, obtido {response.status_code}"

    # 2. Mensagem de Erro
    dados_retornados = json.loads(response.data)
    assert 'erro' in dados_retornados
    assert f"Tarefa com ID {TAREFA_ID} não encontrada para exclusão." in dados_retornados['erro']


