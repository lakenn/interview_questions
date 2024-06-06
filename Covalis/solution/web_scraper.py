import io
import pandas as pd
import requests


def download_excel(url: str) -> io.BytesIO:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return io.BytesIO(response.content)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to download Excel file from {url}: {e}")


def scrape_fca(url: str, xls_sheet_prefix: str) -> pd.DataFrame:
    excel_file = download_excel(url)
    try:
        sheet_name = next(sheet for sheet in pd.ExcelFile(excel_file).sheet_names if sheet.startswith(xls_sheet_prefix))
        return pd.read_excel(excel_file, sheet_name, engine='openpyxl')
    except Exception as e:
        raise Exception(f"Failed to read the spreadsheet - {xls_sheet_prefix}")
