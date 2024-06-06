import io
from datetime import datetime
from functools import reduce

import pandas as pd
import requests


def scrape_fca(url: str, sheet_name_prefix: str) -> pd.DataFrame:
    def download_excel():
        response = requests.get(url)
        response.raise_for_status()
        xls_content = io.BytesIO(response.content)
        return xls_content

    excel_file = download_excel()
    sheet_name = next(sheet for sheet in pd.ExcelFile(excel_file).sheet_names if sheet.startswith(sheet_name_prefix))
    return pd.read_excel(download_excel(), sheet_name, engine='openpyxl')


class ShortPositionCalculator:

    def __init__(self, url, sheet_name_prefix):
        self.url = url
        self.sheet_name_prefix = sheet_name_prefix

    def propagate_disclosures(self):
        df = scrape_fca(self.url, self.sheet_name_prefix)
        df.sort_values(by=['Position Holder', 'Position Date'], inplace=True)

        for ISIN, df_by_isin in df.groupby(['ISIN']):
            start_date, end_date = df_by_isin['Position Date'].min(), df_by_isin['Position Date'].max()
            business_days = pd.bdate_range(start=start_date, end=end_date)
            aggregated_series = pd.Series(0, index=business_days, dtype=float)  # Initialize aggregated series
            print(ISIN)
            for position_holder, series in df_by_isin.groupby(['Position Holder']):
                series = series[['Position Date', 'Net Short Position (%)']]
                series = series.set_index('Position Date')
                series = series.groupby(series.index).agg({'Net Short Position (%)': sum}).reindex(business_days)
                series['Net Short Position (%)'].interpolate(method='pad', limit_area='inside', inplace=True)
                series['Net Short Position (%)'].fillna(0, inplace=True)
                aggregated_series = aggregated_series.add(series['Net Short Position (%)'])

            # Convert aggregated series to DataFrame
            result_df = pd.DataFrame(aggregated_series, columns=['Aggregated short'])
            # Set name of the index
            result_df.index.name = 'Position Date'
            result_df.reset_index(inplace=True)
            result_df['ISIN'] = ISIN[0]
            yield result_df

# Usage
url = 'https://www.fca.org.uk/publication/data/short-positions-daily-update.xlsx'
sheet_prefix_name = 'Historic Disclosures'
calculator = ShortPositionCalculator(url, sheet_prefix_name)
for result in calculator.propagate_disclosures():
    print(result)

