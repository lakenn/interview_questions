import sqlite3

import pandas as pd


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def drop_table(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    conn.commit()


def insert_short_positions(conn, df, table_name: str):
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.commit()


def sql_query(conn, sql_query) -> pd.DataFrame:
    return pd.read_sql_query(sql_query, conn)


def close_connection(conn):
    conn.close()
