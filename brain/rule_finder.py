from pathlib import Path
from brain.sources_excel import load_excel_rules
from brain.sources_pdf import load_pdf_rules
from brain.memory_reader import load_memory_rules

def find_best_rule(intent):
    rules = []

    rules.extend(load_memory_rules(intent))
    rules.extend(load_excel_rules(intent))
    rules.extend(load_pdf_rules(intent))

    if not rules:
        return None

    # Simple confidence sort (can improve later)
    rules.sort(key=lambda x: x.get("confidence", 0), reverse=True)
    return rules[0]
