import pdfplumber
from pathlib import Path
import re

def load_pdf_rules(intent):
    rules = []

    for file in Path("data/pdf").glob("*.pdf"):
        with pdfplumber.open(file) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ""

                if intent["service"] in text.lower():
                    numbers = re.findall(r"\d+", text)
                    if len(numbers) >= 3:
                        rules.append({
                            "base_area": int(numbers[0]),
                            "base_price": float(numbers[1]),
                            "per_unit": int(numbers[2]),
                            "per_price": float(numbers[3]) if len(numbers) > 3 else 0,
                            "debris": 0,
                            "source": f"{file.name} → page {i+1}",
                            "confidence": 0.6
                        })

    return rules
