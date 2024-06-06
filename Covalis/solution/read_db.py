from db_utils import create_connection, sql_query

conn = create_connection('short_positions.db')
df = sql_query(conn, "SELECT * FROM short_positions")
print(df)