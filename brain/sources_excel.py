import pandas as pd
from pathlib import Path
import string

EXCEL_DIR = Path("data/excel")

def _col_letter(n):
    """Convert column index to Excel-style letters"""
    result = ""
    while n >= 0:
        result = chr(n % 26 + 65) + result
        n = n // 26 - 1
    return result

def load_excel_tables():
    """
    Loads ALL excel tables as raw data blocks.
    No assumptions about column names.
    """
    tables = []

    for file in EXCEL_DIR.glob("*.xlsx"):
        xls = pd.ExcelFile(file)

        for sheet in xls.sheet_names:
            df = xls.parse(sheet, header=None)

            if df.empty:
                continue

            headers = df.iloc[0].fillna("").astype(str).tolist()
            body = df.iloc[1:]

            table = {
                "file": file.name,
                "sheet": sheet,
                "headers": headers,
                "rows": [],
            }

            for row_idx, row in body.iterrows():
                row_data = {}

                for col_idx, cell in enumerate(row):
                    col_letter = _col_letter(col_idx)
                    row_data[col_letter] = {
                        "value": str(cell).strip(),
                        "row": row_idx + 1,
                        "col": col_letter,
                        "header": headers[col_idx] if col_idx < len(headers) else ""
                    }

                table["rows"].append(row_data)

            tables.append(table)

    return tables
