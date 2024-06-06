import pandas as pd
from pandas import Series

POSITION_DATE = 'Position Date'
NET_SHORT_POSITION_PERCENTAGE = 'Net Short Position (%)'
IDENTIFIER = 'ISIN'
AGGR_SHORT = 'Aggregated short'


class ShortPositionCalculator:

    @classmethod
    def handle_duplicates(cls, series: Series) -> Series:
        return series.groupby(series.index).agg({NET_SHORT_POSITION_PERCENTAGE: sum})

    @classmethod
    def cleanse_data(cls, series: Series) -> Series:
        # Perform data cleansing operations here
        cleansed_series = cls.handle_duplicates(series)
        # Add more cleansing steps if necessary
        return cleansed_series

    @classmethod
    def aggregate_short_position(cls, short_position_df: pd.DataFrame):
        # short_position_df.sort_values(by=['Position Holder', POSITION_DATE], inplace=True)

        for ISIN, df_by_isin in short_position_df.groupby([IDENTIFIER]):
            start_date, end_date = df_by_isin[POSITION_DATE].min(), df_by_isin[POSITION_DATE].max()
            bdate_range = pd.bdate_range(start=start_date, end=end_date)
            aggregated_series = pd.Series(0, index=bdate_range, dtype=float)

            for position_holder, series in df_by_isin.groupby(['Position Holder']):
                series = series[[POSITION_DATE, NET_SHORT_POSITION_PERCENTAGE]]
                # Dates are reindexed to business days
                series = series.set_index(POSITION_DATE)
                series = cls.cleanse_data(series).reindex(bdate_range)

                # interpolate between data points
                series[NET_SHORT_POSITION_PERCENTAGE].interpolate(method='pad', limit_area='inside', inplace=True)
                series[NET_SHORT_POSITION_PERCENTAGE].fillna(0, inplace=True)

                # total % short
                aggregated_series = aggregated_series.add(series[NET_SHORT_POSITION_PERCENTAGE])

            # Convert aggregated series to DataFrame
            result_df = pd.DataFrame(aggregated_series, columns=[AGGR_SHORT])

            result_df.index.name = POSITION_DATE
            result_df.reset_index(inplace=True)
            result_df[POSITION_DATE] = result_df[POSITION_DATE].dt.date
            result_df[IDENTIFIER] = ISIN[0]
            yield result_df[[IDENTIFIER, POSITION_DATE, AGGR_SHORT]]
