from timeit import default_timer as timer
import time
import pandas as pd
import logging
from foo import LiveDataSource, HistoricalDataSource, process_data, TimeStamp, CURRENT_TIME

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s|%(name)s|%(levelname)s|%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

'''
Supporting functionality provided in the foo package:

class LiveDataSource:
    """
    A class to represent a live data source that provides real-time data.
    """
    def __init__(self, start_time: TimeStamp):
        """
        Constructs all the necessary attributes for the LiveDataSource object.

        Parameters:
        -----------
        start_time: The start time from which to read the live data.
        """
      
    def subscribe(self, symbols: [str], subscriber: Callable[[TimeStamp, pd.Series], None]) -> None:
        """
        Subscribes to the live data stream and calls the subscriber with each data point.

        Parameters:
        -----------
        symbols : List of symbols to subscribe to.
        subscriber: Function to call for each data point and corresponding timestamp.
        """

    def stop(self):
        """Stops the live data stream."""


class HistoricalDataSource:
    """
    A class to represent a historical data source.
    """

    def __init__(self):
        """Constructs all the necessary attributes for the HistoricalDataSource object."""

    def get(self, symbols: [str], start_time: TimeStamp, end_time: TimeStamp) -> pd.DataFrame:
        """
        Retrieves historical data points for the specified symbols and time range.

        Parameters:
        -----------
        symbols : List of symbols to retrieve data for.
        start_time: The start time of the data range.
        end_time: The end time of the data range.

        Returns:
        --------
            DataFrame containing the historical data for the specified symbols and time range.
        """

def process_data(timestamp: TimeStamp, data_point: pd.Series) -> None:
    """
    Simulates the processing of a data point.

    Parameters:
    -----------
    timestamp : The timestamp of the data point.
    data_point : The data point to process.
    """
'''


def consumer_example(timestamp: TimeStamp, data_point: pd.Series) -> None:
    """
    Consumes live data by logging it.

    Parameters:
    -----------
    timestamp : The timestamp of the data point.
    data_point : The data point to consume.

    """
    logger.info(f'{timestamp}|{data_point.to_dict()}')


def test_data_sources(symbols: [str]) -> None:
    """
    Tests the historical and live data sources.

    Parameters:
    -----------
    symbols : List of symbols to use for testing.
    """
    historical_data_source = HistoricalDataSource()
    logger.info('Loading historical data...')

    # !!!Important!!!: the retrieval time increases with the amount of historical data requested
    start = timer()
    historical_data = historical_data_source.get(symbols, CURRENT_TIME - pd.Timedelta('10D'), CURRENT_TIME)
    logger.info(f'Retrieving 10 days of historical data took {timer() - start} seconds:')

    start = timer()
    historical_data = historical_data_source.get(symbols, CURRENT_TIME - pd.Timedelta('100D'), CURRENT_TIME)
    logger.info(f'Retrieving 100 days of historical data took {timer() - start} seconds:')
    logger.info(historical_data)

    # Subscribe to live data with replay of the previous day of data
    live_data_source = LiveDataSource(CURRENT_TIME - pd.Timedelta('1D'))
    live_data_source.subscribe(symbols, consumer_example)
    logger.info('Live data stream started\n')
    time.sleep(5)
    live_data_source.stop()


class UnifiedDataAPI:

    def __init__(self, symbols: [str], start_time: TimeStamp):
        # your implementation here
        pass

    def get_next_data_point(self) -> tuple[TimeStamp, pd.Series] | None:
        # your implementation here
        pass


def main() -> None:
    """
    The main function to run the data source tests or the unified data API simulation.
    """
    # Simulated wall-clock time at start of run... please do not change.
    logging.info(f'Current time: {CURRENT_TIME}')

    historical_start_time = CURRENT_TIME - pd.Timedelta('100D')
    symbols = ['RND1', 'RND2', 'RND3', 'RND4']

    # test_data_sources(symbols)

    live_samples = 0
    start = timer()
    unified_data_api = UnifiedDataAPI(symbols, historical_start_time)
    while True:
        value = unified_data_api.get_next_data_point()
        if value is None:
            break
        timestamp, data_point = value
        if timestamp > CURRENT_TIME:
            if live_samples == 0:
                logging.info(f'Switching to live data mode after {timer() - start} seconds')
            live_samples += 1
        if live_samples >= 5:
            # Stop after 5 live samples
            break

        process_data(timestamp, data_point)
        logging.info(f'Processing {timestamp}|{data_point.to_dict()}')


if __name__ == '__main__':
    main()
