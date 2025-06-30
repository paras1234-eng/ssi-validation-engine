import pandas as pd
import sqlite3

# Step 1: Load the data
trades_df = pd.read_csv("trades.csv")
ssi_df = pd.read_csv("ssi_master.csv")

# Step 2: Connect to the SQLite DB
conn = sqlite3.connect("ssi_data.db")

# Step 3: Write to DB
trades_df.to_sql("trades", conn, if_exists="replace", index=False)
ssi_df.to_sql("ssi_master", conn, if_exists="replace", index=False)

# ✅ NEW Step: Print all table names to verify
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("✅ Tables in the database:", tables)

conn.close()