from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
todos.append({ "done": True, "label": "Sample Todo 1" })

@app.route('/todos', methods=['GET'])
def hello_world():
        json_text = jsonify(todos)
        return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
   
    request_body = request.get_json()
    if request_body is None:
        return jsonify({"error": "Invalid input"}), 400

    print("Incoming request with the following body", request_body)
    
    
    if not isinstance(request_body, dict):
        return jsonify({"error": "Invalid input format"}), 400

    todos.append(request_body)
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)
   
    



# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)