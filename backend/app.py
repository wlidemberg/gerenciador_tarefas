from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    dados_recebidos = request.get_json()

    if not dados_recebidos or 'titulo' not in dados_recebidos:
        return jsonify({'erro':'O campo titulo é obrigatorio'}), 400
        
    titulo_tarefa = dados_recebidos['titulo']
    descricao_tarefa = dados_recebidos.get('descricao')
    
    conn = None
    id_nova_tarefa = None
    try:

        sql = "INSERT INTO tarefa (titulo, descricao) VALUES (?, ?)"

        dados_inserir = (titulo_tarefa, descricao_tarefa)
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, dados_inserir)
        conn.commit()
        id_nova_tarefa = cursor.lastrowid
    
    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({'erro':f'Erro ao salvar no banco de dados:{e}'})
    finally:
        if conn:
            conn.close() 

    nova_tarefa_criada = {
        "id": id_nova_tarefa,
        "titulo":titulo_tarefa,
        "descricao":descricao_tarefa,   
        "status":"pendente"
    }                   

    return jsonify(nova_tarefa_criada), 201

@app.route('/tarefas/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    dados_recebidos = request.get_json()

    # Validação Básica: O PUT deve ter o título, ou pelo menos um campo para atualizar
    if not dados_recebidos:
        return jsonify({'Erro':'Nenhum dado fornecido para atualização'}), 400
    
    # Validação de campos obrigatórios (se necessário, mas para PUT, a presença é suficiente)
    titulo = dados_recebidos.get('titulo')
    descricao = dados_recebidos.get('descricao')
    status = dados_recebidos.get('status')

    # Busca a tarefa original (simulada aqui, mas em um sistema real faria uma busca)
    # Como não temos uma rota GET /tarefas/<id>, vamos assumir que os campos devem ser passados.

    # Chamamos a função de atualização.
    tarefa_atualizada = database.update_tarefa(tarefa_id=tarefa_id, titulo=titulo, descricao=descricao, status=status)

    if tarefa_atualizada:
        # 200 OK e retorna o objeto atualizado
        return jsonify(tarefa_atualizada), 200
    else:
        # 404 Not Found se a tarefa não existir
        return jsonify({'erro':f'Tarefa com ID {tarefa_id} não encontrada para atualização'}), 404  

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    print("Requisição GET /tarefas recebidas.")

    tarefas_recebidas = database.get_all_tarefas()

    return jsonify(tarefas_recebidas), 200

@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    # Chamamos a função de exclusão no módulo database
    linhas_afetadas = database.delete_tarefa(tarefa_id)

    if linhas_afetadas > 0:
        # 204 no Content é o status padrão para o DELETE bem-sucedido
        return '', 204
    else:
        return jsonify({'erro':f'Tarefa com ID {tarefa_id} não encontrada para exclusão.'}), 404

if __name__=="__main__":
    print("Inicializando banco de dados (se necessario)...")
    database.create_tables()
    print("Inicializando servidor Flask em modo de desenvolvimento")
    app.run(debug=True, port=5000)    