import pandas as pd
import numpy as np

# Sample DataFrame with a time series
data = {'value': [None, 5, None, None, 10, None, None, 15, 20, None]}
index = pd.date_range(start='2022-01-01', periods=len(data['value']), freq='D')
series = pd.Series(data['value'], index=index)
series.interpolate(method='pad', limit_area='inside')

# Find positions of non-zero values
non_zero_positions = series[series != 0].index

# Mark positions to forward fill
for i, pos in enumerate(non_zero_positions[:-1]):
    next_pos = non_zero_positions[i + 1]
    series.loc[pos:next_pos] = series.loc[pos]

# Forward fill NaN values
series_filled = series.ffill()

print(series_filled)