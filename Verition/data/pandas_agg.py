import numpy as np
import pandas
import pandas as pd


def solution(files):
    # files - any of available files, i.e:
    files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
               "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
               "./data/twerche.csv", "./data/veeme.csv"]

    files = ["./data/throwsh.csv"]

    # write your solution here
    results = []
    for file in files:
        df = pd.read_csv(file)
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].dt.year

        # Group by year and find the max volume and corresponding date
        max_vol_dates = df.loc[df.groupby('year')['vol'].idxmax(), ['date', 'vol']]

        # Group by year and find the rows with the maximum 'close' for each year
        max_close_dates = df[df.groupby('year')['close'].transform('max') == df['close']][['date', 'close']]

        # # Group by year and find the max close price for each year
        # max_close = df.groupby('year')['close'].max()
        # max_close_dates = pd.DataFrame()
        #
        # # Loop through each year to find all occurrences of the max close price
        # for year, max_price in max_close.items():
        #     # Filter the original DataFrame to find all occurrences of the max close
        #     occurrences = df[(df['year'] == year) & (df['close'] == max_price)]
        #     max_close_dates = pd.concat([max_close_dates, occurrences[['date', 'close']]], ignore_index=True)

        results.append([max_vol_dates, max_close_dates])


    return results

solution([])

"""
import numpy as np
import pandas as pd


def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here
    results = []
    for file in files:
        df = pd.read_csv(file)
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].dt.year

        # Group by year and find the max volume and corresponding date
        max_vol_dates = df.loc[df.groupby('year')['vol'].idxmax(), ['date', 'vol']]
        
        # Group by year and find the rows with the maximum 'close' for each year
        max_close_dates = df[df.groupby('year')['close'].transform('max') == df['close']][['date', 'close']]

        # # Group by year and find the max close price for each year
        # max_close = df.groupby('year')['close'].max()
        # max_close_dates = pd.DataFrame()

        # # Loop through each year to find all occurrences of the max close price
        # for year, max_price in max_close.items():
        #     occurrences = df[(df['year'] == year) & (df['close'] == max_price)]
        #     max_close_dates = pd.concat([max_close_dates, occurrences[['date', 'close']]], ignore_index=True)

        results.append([max_vol_dates, max_close_dates])

    
    return results


"""