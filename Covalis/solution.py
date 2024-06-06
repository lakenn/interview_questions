from functools import reduce

import pandas as pd

# Set display options
pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)
pd.set_option('display.width', 999)

data = {
    'Position Holder': ['A', 'A', 'B'],
    'Name of Share Issuer': ['Company 1', 'Company 1', 'Company 1'],
    'ISIN': ['ISIN_1', 'ISIN_1', 'ISIN_1'],
    'Net Short Position (%)': [0.5, 1, 2],
    'Position Date': ['20/4/2023', '10/4/2023', '17/4/2023']
}

data2 = {
    'Position Holder': ['A', 'B'],
    'Name of Share Issuer': ['Company 1', 'Company 1'],
    'ISIN': ['ISIN_2', 'ISIN_2'],
    'Net Short Position (%)': [0.5, 2],
    'Position Date': ['01/5/2023', '31/5/2023']
}

df = pd.concat([pd.DataFrame(data), pd.DataFrame(data2)])
df['Position Date'] = pd.to_datetime(df['Position Date'], format='%d/%m/%Y')
df = df[['ISIN', 'Position Holder', 'Position Date', 'Net Short Position (%)']]

for ISIN, df_by_isin in df.groupby(['ISIN']):
    start_date, end_date = df_by_isin['Position Date'].min(), df_by_isin['Position Date'].max()
    business_days = pd.date_range(start=start_date, end=end_date, freq='B')
    all_series = []
    for position_holder, series in df_by_isin.groupby(['Position Holder']):
        series = series.set_index('Position Date').reindex(business_days)
        series['Net Short Position (%)'].interpolate(method='pad', limit_area='inside', inplace=True)
        series['Net Short Position (%)'].fillna(0, inplace=True)
        all_series.append(series)
    print(1)

df2 = pd.pivot_table(df, values="Net Short Position (%)", index=["ISIN", "Position Date"], columns=["Position Holder"])

start_date, end_date = df['Position Date'].min(), df['Position Date'].max()
business_days = pd.date_range(start=start_date, end=end_date, freq='B')
df2 = df2.reindex(pd.MultiIndex.from_product([df2.index.levels[0], business_days], names=df2.index.names))

# Function to apply interpolation
def interpolate_group(group):
    return group.interpolate(method='pad', limit_area='inside').fillna(0)

# Reset the index to perform interpolation
pivot_reset = df2.reset_index()

# Interpolate each value column
pivot_reset[df2.columns] = pivot_reset[df2.columns].apply(
    lambda col: col.interpolate(method='pad', limit_area='inside').fillna(0)
)
# for column in df2.columns:
#     pivot_reset[column].interpolate(method='pad', limit_area='inside', inplace=True)
#     pivot_reset.fillna(0, inplace=True)


pivot_reset['Aggregated Short'] = pivot_reset[df2.columns].sum(axis=1)

# Define a function to add two Series
def add_series(series1, series2):
    return series1.add(series2, fill_value=0)


for ISIN, df_by_isin in df.groupby(['ISIN']):
    start_date, end_date = df_by_isin['Position Date'].min(), df_by_isin['Position Date'].max()
    business_days = pd.date_range(start=start_date, end=end_date, freq='B')
    series_array = []
    for position_holder, series in df_by_isin.groupby(['Position Holder']):
        series = series[['Position Date', 'Net Short Position (%)']]
        series = series.set_index('Position Date').reindex(business_days)
        series['Net Short Position (%)'].interpolate(method='pad', limit_area='inside', inplace=True)
        series['Net Short Position (%)'].fillna(0, inplace=True)
        series_array.append(series)

    result = reduce(add_series, series_array)
    result.index.name = 'Position Date'
    result['ISIN'] = ISIN[0]
    print(result)

# Reindex the DataFrame with the new business dates
df2_reindexed = df2.reindex(pd.MultiIndex.from_product([df2.index.levels[0], business_days], names=df2.index.names))

for ISIN, group_df in df2_reindexed.groupby(level=[0,1]):
    print(ISIN, group_df)
#
#
#
# df3 = df2_reindexed.ffill()
#
# # Reindex with a complete date range for each 'ISIN'
# idx = pd.MultiIndex.from_product([df.index, df['ISIN'].unique()], names=['Position Date', 'ISIN'])
# df = df.reindex(idx)
#
#
#
# df2 = df.set_index('Position Date').reindex(business_days, method='ffill')
#
#
# # Assume that the position is closed the next business day after the last disclosure
# df2['Net Short Position (%)'] = df2['Net Short Position (%)'].shift(-1, fill_value=0)
# print(1)