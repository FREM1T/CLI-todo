#!/usr/bin/env python3
import typer
import json
import os
from pathlib import Path


if not os.path.exists("~/.config/todocli"):
    import install
    install.setup_first_run()

app = typer.Typer()
CFG_FILE = 
with open("config.json", "r", encoding="utf-8") as f:
    TODO_FILE = Path(f.)


def load_todos_list() -> list:
    if TODO_FILE.exists():
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def load_config() -> dict:
    if TODO_FILE.exists():
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

@app.command()
def init() -> None:
    with open("config.json", "a"):
        pass
    dir_path = input(
        "Введите путь до директории, в которой хотите хранить свои задачи (Пример: ~/tasks/task.json): "
    )

    with open("config.json", "w", encoding="utf-8") as f:
        conf = {"dir_path": dir_path}
        json.dump(conf, f, ensure_ascii=False, indent=4)


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
