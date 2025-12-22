import json
import time
from pathlib import Path

MEMORY_FILE = Path("memory/knowledge.json")

def save_learning(intent, rule, final_price):
    MEMORY_FILE.parent.mkdir(exist_ok=True)

    key = f"{intent['service']}|{intent['area']}|{intent['debris']}"

    data = {}
    if MEMORY_FILE.exists():
        data = json.loads(MEMORY_FILE.read_text())

    data[key] = {
        "base_area": rule["base_area"],
        "base_price": rule["base_price"],
        "per_unit": rule["per_unit"],
        "per_price": rule["per_price"],
        "debris": rule.get("debris", 0),
        "confidence": min(rule.get("confidence", 0.7) + 0.05, 0.99),
        "last_used": int(time.time())
    }

    MEMORY_FILE.write_text(json.dumps(data, indent=2))
