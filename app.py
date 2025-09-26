#!/usr/bin/env python3
import typer
import json
from pathlib import Path

app = typer.Typer()
tasks_path = Path("tasks.json")


def load_todo_list() -> list:
    if tasks_path.exists():
        with open(tasks_path, "r", encoding="UTF-8") as f:
            return json.loads(f)
    return []


@app.command()
def greetings(name: str, iq: int, show_iq: bool = False) -> None:
    print(f"Hello, {name}!")
    if show_iq:
        print(f"Your IQ is {iq}")


@app.command()
def goodbye() -> None:
    print("See you :)")


if __name__ == "__main__":
    app()
