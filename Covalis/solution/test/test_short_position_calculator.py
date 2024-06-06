from unittest import TestCase

import pandas as pd

from short_position_calculator import ShortPositionCalculator


class TestShortPositionCalculator(TestCase):

    def setUp(self):
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
        self.df = df[['ISIN', 'Position Holder', 'Position Date', 'Net Short Position (%)']]

    def test_aggregate_short_position(self):
        calculator = ShortPositionCalculator()
        result_df = next(calculator.aggregate_short_position(self.df))

        expected_df = pd.DataFrame({
            'ISIN': ['ISIN_1', 'ISIN_1', 'ISIN_1', 'ISIN_1', 'ISIN_1', 'ISIN_1', 'ISIN_1', 'ISIN_1', 'ISIN_1'],
            'Position Date': ['10/04/2023', '11/04/2023', '12/04/2023', '13/04/2023', '14/04/2023', '17/04/2023', '18/04/2023', '19/04/2023', '20/04/2023'],
            'Aggregated short': [1.0, 1.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0, 0.5]
        })
        expected_df['Position Date'] = pd.to_datetime(expected_df['Position Date'], format='%d/%m/%Y')

        pd.testing.assert_frame_equal(result_df, expected_df)

