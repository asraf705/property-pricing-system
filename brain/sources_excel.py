
import pandas as pd
from pathlib import Path

def load_excel_rules(intent):
    rules = []

    for file in Path("data/excel").glob("*.xlsx"):
        xls = pd.ExcelFile(file)

        for sheet in xls.sheet_names:
            df = xls.parse(sheet)
            df.columns = [str(c).lower().strip() for c in df.columns]

            for _, row in df.iterrows():
                service = str(row.get("service", "")).lower()

                if intent["service"] in service:
                    rules.append({
                        "base_area": int(row.get("base_area", 0)),
                        "base_price": float(row.get("base_price", 0)),
                        "per_unit": int(row.get("per_unit", 100)),
                        "per_price": float(row.get("per_price", 0)),
                        "debris": float(row.get("debris", 0)),
                        "source": f"{file.name} → {sheet}",
                        "confidence": 0.7
                    })

    return rules
