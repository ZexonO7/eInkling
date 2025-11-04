import threading
import time
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import REFRESH_MINUTES
from .renderer import render_and_push
from .storage import load_json, save_json

_refresh_thread = None
_stop_event = threading.Event()

def _loop_refresh():
    while not _stop_event.is_set():
        try:
            render_and_push()
        except Exception as e:
            print("[renderer] error:", e)
        for _ in range(REFRESH_MINUTES * 60):
            if _stop_event.is_set():
                break
            time.sleep(1)

def create_app():
    app = Flask(__name__)

    @app.before_first_request
    def start_bg():
        global _refresh_thread
        if _refresh_thread is None:
            _refresh_thread = threading.Thread(target=_loop_refresh, daemon=True)
            _refresh_thread.start()

    @app.route("/")
    def index():
        notes = load_json("notes.json", default={"items": []})
        todos = load_json("todos.json", default={"items": []})
        return render_template("index.html", notes=notes, todos=todos, now=datetime.now())

    @app.route("/notes", methods=["GET", "POST"])
    def notes():
        if request.method == "POST":
            body = request.form.get("body", "").strip()
            data = load_json("notes.json", default={"items": []})
            if body:
                data["items"].insert(0, {"text": body, "ts": datetime.now().isoformat(timespec='seconds')})
                save_json("notes.json", data)
            return redirect(url_for("notes"))
        data = load_json("notes.json", default={"items": []})
        return render_template("notes.html", notes=data)

    @app.route("/todos", methods=["GET", "POST"])
    def todos():
        data = load_json("todos.json", default={"items": []})
        if request.method == "POST":
            body = request.form.get("body", "").strip()
            if body:
                data["items"].append({"text": body, "done": False})
                save_json("todos.json", data)
            return redirect(url_for("todos"))
        return render_template("todos.html", todos=data)

    @app.post("/api/todos/toggle")
    def api_toggle():
        idx = int(request.form.get("index", -1))
        data = load_json("todos.json", default={"items": []})
        if 0 <= idx < len(data["items"]):
            data["items"][idx]["done"] = not data["items"][idx].get("done", False)
            save_json("todos.json", data)
            return jsonify(ok=True)
        return jsonify(ok=False), 400

    @app.post("/refresh")
    def manual_refresh():
        try:
            render_and_push()
            return redirect(url_for("index"))
        except Exception as e:
            return f"Error: {e}", 500

    return app
