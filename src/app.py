from flask import Flask, jsonify, request 
import json 

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False }, { "label": "My second task", "done": False } ]

@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos', methods=['GET'])
def todo_get():
    json_text = jsonify(todos)
    return json_text

some_data = { "name": "Bobby", "lastname": "Rixer" }

@app.route('/blahblah', methods=['GET'])
def blahblah():
    json_text = jsonify(todos)

    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    # json_text = jsonify({"lista":todos, "message":"ok"})
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete", position)
    position = int(position)
    if position >= len(todos):
        return jsonify({"message":"índice inválido"})
    if position < 0:
        return jsonify({"message":"índice inválido"})
    if len(todos) == 0:
        return jsonify({"message":"índice inválido"})
 
    todos.pop(position)

    json_text = jsonify(todos)
    return json_text


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)