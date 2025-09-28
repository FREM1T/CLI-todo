import os
import json
import pathlib

CFG_DIR = os.path.join("~/.config/todocli")
CFG_FILE = os.path.join(CFG_DIR, "config.json")

def setup_first_run():
    if not os.path.exists(CFG_DIR):
        os.makedirs(CFG_DIR)
    
    # Создаём базовый конфиг
    default_cfg = {
        "todo_path": "~/Documents/"
    }
    with open(CFG_FILE, "w") as f:
        json.dump(default_cfg, f, indent=4)


    print("✅ Приложение успешно настроено!")
