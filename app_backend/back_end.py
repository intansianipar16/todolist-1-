from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        tasks.append(task)
        return jsonify({"message": "Task added successfully!"}), 201
    return jsonify({"message": "Task content is missing!"}), 400

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)
        return jsonify({"message": f'Task "{task}" deleted successfully!'})
    return jsonify({"message": "Invalid task ID!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
