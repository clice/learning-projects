from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
current_id = 1

@app.get("/tasks")
def list_tasks():
    return jsonify(tasks)

@app.post("/tasks")
def create_task():
    global current_id
    data = request.get_json() or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "title é obrigatório"}), 400
    task = {"id": current_id, "title": title, "done": False}
    current_id += 1
    tasks.append(task)
    return jsonify(task), 201

@app.put("/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json() or {}
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            if "done" in data:
                task["done"] = bool(data["done"])
            return jsonify(task)
    return jsonify({"error": "task não encontrada"}), 404

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
