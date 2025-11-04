import json
import os
from config import DATA_DIR

def _path(name: str) -> str:
    return os.path.join(DATA_DIR, name)

def load_json(name: str, default):
    p = _path(name)
    if not os.path.exists(p):
        return default
    with open(p, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return default

def save_json(name: str, data):
    p = _path(name)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
