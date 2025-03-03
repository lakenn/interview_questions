# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: foo\__init__.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2024-12-12 16:02:35 UTC (1734019355)

import threading
import time
from datetime import datetime
from typing import Callable
import pandas as pd
import logging
TimeStamp = datetime | pd.Timestamp | str
logger = logging.getLogger(__name__)
CURRENT_TIME = pd.Timestamp('2024-11-01 09:00')

class LiveDataSource:
    """
    A class to represent a live data source that provides real-time data.
    """

    def __init__(self, start_time: TimeStamp):
        """
        Constructs all the necessary attributes for the LiveDataSource object.

        Parameters:
        -----------
        start_time: timestamp
            The start time from which to read the live data.
        """
        self._data = pd.read_csv('live_data.csv', index_col=0, parse_dates=True).loc[start_time:]
        self._running = False
        self._current_time = CURRENT_TIME

    def subscribe(self, symbols: [str], subscriber: Callable[[TimeStamp, pd.Series], None]) -> None:
        """
        Subscribes to the live data stream and calls the subscriber with each data point.

        Parameters:
        -----------
        symbols : List[str]
            List of symbols to subscribe to.
        subscriber: Callable[[timestamp, pd.Series], None]
            Function to call with each data point.
        """

        def data_stream() -> None:
            self._running = True
            for index, row in self._data.iterrows():
                if not self._running:
                    return
                subscriber(row.name, row.loc[symbols].copy())
                if row.name > self._current_time:
                    time.sleep(1)
        thread = threading.Thread(target=data_stream)
        time.sleep(1)
        thread.start()

    def stop(self) -> None:
        """Stops the live data stream."""
        self._running = False

class HistoricalDataSource:
    """
    A class to represent a historical data source.
    """

    def __init__(self):
        """Constructs all the necessary attributes for the HistoricalDataSource object."""
        self._data = pd.read_csv('historic_data.csv', index_col=0, parse_dates=True)

    def get(self, symbols: [str], start_time: TimeStamp, end_time: TimeStamp) -> pd.DataFrame:
        """
        Retrieves historical data for the specified symbols and time range.

        Parameters:
        -----------
        symbols : List[str]
            List of symbols to retrieve data for.
        start_time: TimeStamp
            The start time of the data range.
        end_time: TimeStamp
            The end time of the data range.

        Returns:
        --------
            DataFrame containing the historical data for the specified symbols and time range.
        """
        payload = self._data.loc[start_time:end_time, symbols].copy()
        time.sleep(0.0001 * len(payload))
        return payload

def process_data(timestamp: TimeStamp, data_point: pd.Series) -> None:
    """
    Simulates the processing of a data point.

    Parameters:
    -----------
    timestamp : TimeStamp
        The timestamp of the data point.
    data_point : pd.Series
        The data point to process.
    """
    time.sleep(0.0001)