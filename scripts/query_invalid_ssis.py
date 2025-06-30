import sqlite3
import pandas as pd

conn = sqlite3.connect("ssi_data.db")
result = pd.read_sql_query("SELECT * FROM validated_trades WHERE Valid_SSI_Format = 0", conn)
print(result)
conn.close()