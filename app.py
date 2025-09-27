#!/usr/bin/env python3
import typer
import json
from pathlib import Path

app = typer.Typer()
TODO_FILE = Path("todos.json")

def load_todos_list() -> list:
    if TODO_FILE.exists():
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.command()
def add(task: str) -> None:
    todos_list = load_todos_list()
    new_task = {"task": task, "done": False}
    todos_list.append(new_task)
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos_list, f, ensure_ascii=False, indent=4)

@app.command()
def show() -> None:
    todo_list = load_todos_list()
    for i in range(len(todo_list)):
        print(f"{i + 1}) {todo_list[i]}")

if __name__ == "__main__":
    app()