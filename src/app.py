from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todo = [{ "label": "My first task", "done": False },{ "label": "My first task", "done": False }]


@app.route('/todos', methods=['GET'])
def Get_todo():
    json_text = jsonify(todo);
    return json_text;


@app.route('/todos', methods=['POST'])
def post_todo():
    decoded_object = json.loads(request.data)
    todo.append(decoded_object)
    return jsonify({"msg":todo})

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todo.pop(position)
    print("This is the position to delete: ",position)
    return jsonify({"msg":todo})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)