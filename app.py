from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)
tasks = []

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple To Do List</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
        .container { max-width: 500px; margin: 40px auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px #ccc; }
        h1 { text-align: center; }
        ul { list-style: none; padding: 0; }
        li { padding: 10px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; }
        button { background: #e74c3c; color: #fff; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; }
        button:hover { background: #c0392b; }
        input[type="text"] { width: 80%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
        .add-btn { background: #2ecc71; margin-left: 10px; }
        .add-btn:hover { background: #27ae60; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Task Manager</h1>
        <form id="taskForm">
            <input type="text" id="taskInput" placeholder="Add a new task..." required />
            <button type="submit" class="add-btn">Add</button>
        </form>
        <ul id="taskList"></ul>
    </div>
    <script>
        async function fetchTasks() {
            const res = await fetch('/tasks');
            const data = await res.json();
            const list = document.getElementById('taskList');
            list.innerHTML = '';
            data.forEach((task, idx) => {
                const li = document.createElement('li');
                li.textContent = task;
                const delBtn = document.createElement('button');
                delBtn.textContent = 'Delete';
                delBtn.onclick = async function() {
                    await fetch('/tasks/' + idx, { method: 'DELETE' });
                    fetchTasks();
                };
                li.appendChild(delBtn);
                list.appendChild(li);
            });
        }
        document.getElementById('taskForm').onsubmit = async function(e) {
            e.preventDefault();
            const input = document.getElementById('taskInput');
            await fetch('/tasks', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ task: input.value })
            });
            input.value = '';
            fetchTasks();
        };
        fetchTasks();
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task", "").strip()
    if task:
        tasks.append(task)
    return ("", 204)


@app.route("/tasks/<int:idx>", methods=["DELETE"])
def delete_task(idx):
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
    return ("", 204)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
