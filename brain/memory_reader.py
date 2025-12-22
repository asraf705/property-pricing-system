import json
from pathlib import Path

MEMORY_FILE = Path("memory/knowledge.json")

def load_memory_rules(intent):
    if not MEMORY_FILE.exists():
        return []

    data = json.loads(MEMORY_FILE.read_text())
    key = f"{intent['service']}|{intent['area']}|{intent['debris']}"

    if key not in data:
        return []

    rule = data[key]
    rule["source"] = "Learned Memory"
    return [rule]
