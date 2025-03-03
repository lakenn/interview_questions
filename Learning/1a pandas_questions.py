import pandas as pd

# Sample DataFrame
data = {
    "customer_id": ["A", "A", "B", "C"],
    "purchase_time": [
        "2025-01-01 10:00:00",
        "2025-02-22 10:00:00",
        "2025-02-23 18:00:00",
        "2025-02-24 09:00:00",
    ],
    "amount": [40, 50, 30, 20],
    "amount2": [40, 50, 30, 20]
}

# create pandas dataframe
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['purchase_time'], errors='coerce').dt.date
print(df['date'])
df.set_index('date', inplace=True)

# add missing dates
bdates = pd.bdate_range('2025-01-01', '2025-02-28')
bdates = pd.bdate_range('2025-01-01', periods=60, freq='D')
df = df.reindex(bdates)
print(df)


# interpolate

df.interpolate(method='pad', limit_area='inside', inplace=True)
print(df)
# fillna
df.fillna(method='ffill', inplace=True)
print(df)

# get subset
customer = df[['customer_id']]

# groupby
df.groupby('customer_id').agg({'amount': 'sum'})
gb = df.groupby('customer_id')[['amount', 'amount2']].mean()
for name, group in gb.items():
    print(name, group)
print(gb)

idmax = df.groupby('customer_id')['amount'].idxmax()
print(idmax)

print(df.loc[idmax])

first = df.groupby('customer_id').agg(lambda x: x.iloc[0])
last = df.groupby('customer_id').agg({'amount': 'last'})
print(first)
print(last)

# print(df.groupby('customer_id').apply(lambda grp: grp.count()))

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar'],
                    'B' : ['one', 'one', 'two', 'three',
                          'two', 'two'],
                   'C' : [1, 5, 5, 2, 5, 5],
                 'D' : [2.0, 5., 8., 1., 2., 9.]})
grouped = df.groupby('A')[['C', 'D']]
max_value = grouped.transform(lambda x: x.max())


print(grouped)

# series
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print(series)

