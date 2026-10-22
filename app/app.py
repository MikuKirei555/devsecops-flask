"""Aplikasi To-Do List sederhana berbasis Flask."""
import os

from flask import Flask, jsonify, request

app = Flask(__name__)
TASKS = []


@app.route("/")
def index():
    """Halaman utama."""
    return jsonify(message="DevSecOps To-Do API", status="running")


@app.route("/health")
def health():
    """Endpoint untuk health check pipeline."""
    return jsonify(status="ok"), 200


@app.route("/tasks", methods=["GET"])
def list_tasks():
    """Menampilkan semua tugas."""
    return jsonify(TASKS)


@app.route("/tasks", methods=["POST"])
def add_task():
    """Menambah tugas baru."""
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify(error="title wajib diisi"), 400
    task = {"id": len(TASKS) + 1, "title": title, "done": False}
    TASKS.append(task)
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "5000")))
