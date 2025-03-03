import pandas as pd
pd.options.display.max_rows = 99999
pd.options.display.max_columns = 9999

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)

# iloc
df = pd.DataFrame({'date': ['2024-06-30', '2024-06-01', '2024-06-02', '2024-07-01'], 'price': [40.3, 100.0, 99.3, 80.4]})
print(df)

# convert str to datetime
df['date'] = pd.to_datetime(df['date'], "coerce")

# df.set_index('date', inplace=True)
# df.sort_index(inplace=True)
df.sort_index(ascending=False)

df['month'] = df['date'].dt.month
for name, group in df.groupby('month')['price']:
    print(f"Group: {name}")
    print(group)
    print(group.idxmax(), group[group.idxmax()])
    print('-------------')


for name, group in df.groupby('month'):
    print(name, group)

# # # Group by year and find the max close price for each year
# max_close = df.groupby('year')['price'].max()
# max_close_dates = pd.DataFrame()
#
# # Loop through each year to find all occurrences of the max close price
# for year, max_price in max_close.items():
#     # Filter the original DataFrame to find all occurrences of the max close
#     occurrences = df[(df['year'] == year) & (df['close'] == max_price)]
#     max_close_dates = pd.concat([max_close_dates, occurrences[['date', 'close']]], ignore_index=True)
#


import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)



import pandas as pd

# Sample DataFrame
data = {
    'month': [6, 6, 7, 7],
    'price': [100, 150, 200, 250],
    'close': [90, 140, 190, 240],
    'item': ['A', 'B', 'C', 'D']
}
df = pd.DataFrame(data)


# Get the indices of the rows with the maximum 'price' and 'close' for each 'month'
idx = df.groupby('month')[['price', 'close']].idxmax()

# Use .loc[] to select these rows
max_price_rows = df.loc[idx['price']]
max_close_rows = df.loc[idx['close']]

print("Rows with maximum 'price' for each 'month':")
print(max_price_rows)
print("\nRows with maximum 'close' for each 'month':")
print(max_close_rows)

import pandas as pd

#create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points': [30, 22, 19, 14, 14, 11, 20, 28]})

#view DataFrame
print(df)

#create new column called mean_points
df['mean_points'] = df.groupby('team')['points'].transform('mean')

#view updated DataFrame
print(df)


import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
# Group by 'Category' and 'Subcategory'
grouped = df.groupby(['Category', 'Subcategory'])

# Iterate through each group
for (category, subcategory), group in grouped:
    print(f"Category: {category}, Subcategory: {subcategory}")
    print(group)
    print()

# importing the pandas library
import pandas as pd

# making data for dataframing
data = {
    'series': ['Peaky blinders', 'Sherlock', 'The crown',
               'Queens Gambit', 'Friends'],

    'Ratings': [4.5, 5, 3.9, 4.2, 5],

    'Date': [2013, 2010, 2016, 2020, 1994]
}

# Dataframing the whole data created
df = pd.DataFrame(data)

# setting first and the second name
# as index column
df.set_index(["series", "Ratings"], inplace=True,
             append=True, drop=False)
# display the dataframe
print(df)


# bdate_range = pd.bdate_range(start=start_date, end=end_date)

import pandas as pd

# holidays = ['2023-01-05', '2023-01-06']
date_range = pd.bdate_range(start='2023-01-01', end='2023-01-10')
print(date_range)


import pandas as pd

# Create a Series
series = pd.Series([10, 20, 30, 40, 50], name="Values")

# Convert it into a DataFrame
df = pd.DataFrame(series)

print(df)


import pandas as pd

# Sample DataFrame
data = {
    "customer_id": ["A", "B", "A", "C", "B", "A"],
    "purchase_time": [
        "2025-02-22 10:00:00",
        "2025-02-23 15:30:00",
        "2025-02-23 18:00:00",
        "2025-02-24 09:00:00",
        "2025-02-24 10:30:00",
        "2025-02-24 11:00:00"
    ],
    "amount": [50, 30, 20, 40, 100, 25]
}

# Find purchases in the last 48 hours for each customer?

df = pd.DataFrame(data)
df['purchase_time'] = pd.to_datetime(df['purchase_time'])
df['cutoff'] = df['purchase_time'].max() - pd.Timedelta('48h')
df = df[df['purchase_time'] >= df['cutoff']]
df_sum = df.groupby('customer_id')['amount'].sum()
print(df_sum)