import sys

from db_utils import create_connection, insert_short_positions, close_connection, drop_table
from short_position_calculator import ShortPositionCalculator
from web_scraper import scrape_fca


def main():
    url = 'https://www.fca.org.uk/publication/data/short-positions-daily-update.xlsx'
    xls_sheet_prefix = 'Historic Disclosures'
    tbl_name = 'short_positions'
    conn = create_connection(f'{tbl_name}.db')
    drop_table(conn, tbl_name)

    try:
        short_position_df = scrape_fca(url, xls_sheet_prefix)
        for aggregated_short_pos in ShortPositionCalculator.aggregate_short_position(short_position_df):
            insert_short_positions(conn, aggregated_short_pos, tbl_name)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        close_connection(conn)


if __name__ == "__main__":
    main()