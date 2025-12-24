from brain.sources_excel import load_excel_tables
from brain.sources_pdf import load_pdf_rules
from brain.memory_reader import load_memory_rules

def find_best_rule(intent):
    candidates = []

    # Memory (highest confidence)
    candidates.extend(load_memory_rules(intent))

    # Excel tables
    tables = load_excel_tables()

    for table in tables:
        for row in table["rows"]:
            for cell in row.values():
                text = cell["value"].lower()

                if intent["service"] in text:
                    candidates.append({
                        "source": f'{table["file"]} → {table["sheet"]}',
                        "matched_text": cell["value"],
                        "row": cell["row"],
                        "confidence": 0.7,
                        "raw_row": row,
                        "headers": table["headers"]
                    })

    # PDF
    candidates.extend(load_pdf_rules(intent))

    if not candidates:
        return None

    candidates.sort(key=lambda x: x["confidence"], reverse=True)
    return candidates[0]
