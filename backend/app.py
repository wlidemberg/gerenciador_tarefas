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
        conn.close() 

    nova_tarefa_criada = {
        "id": id_nova_tarefa,
        "titulo":titulo_tarefa,
        "descricao":descricao_tarefa,
        "status":"pendente"
    }                   

    return jsonify(nova_tarefa_criada), 201

if __name__=="__main__":
    print("Inicializando banco de dados (se necessario)...")
    database.create_tables()
    print("Inicializando servidor Flask em modo de desenvolvimento")
    app.run(debug=True, port=5000)    