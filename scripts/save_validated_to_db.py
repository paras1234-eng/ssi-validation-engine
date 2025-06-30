import pandas as pd
import sqlite3
import re

# Connect to database
conn = sqlite3.connect("ssi_data.db")

# Read trades and SSI master tables
trades_df = pd.read_sql_query("SELECT * FROM trades", conn)
ssi_df = pd.read_sql_query("SELECT * FROM ssi_master", conn)

# Merge on Security
merged_df = trades_df.merge(ssi_df, on="Security", how="left")

# Validate format (BIC)
def is_valid_bic(bic):
    if pd.isna(bic):
        return False
    return bool(re.match(r"^[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?$", bic))

# Apply validation
merged_df["Valid_SSI_Format"] = merged_df["SSI"].apply(is_valid_bic)

# Save result to new table
merged_df.to_sql("validated_trades", conn, if_exists="replace", index=False)

print(" Data successfully saved to table: validated_trades")

conn.close()
