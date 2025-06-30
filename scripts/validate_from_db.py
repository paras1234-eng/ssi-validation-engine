import pandas as pd
import sqlite3
import re

# Step 1: Connect to DB and read tables
conn = sqlite3.connect("ssi_data.db")
trades_df = pd.read_sql_query("SELECT * FROM trades", conn)
ssi_df = pd.read_sql_query("SELECT * FROM ssi_master", conn)

# Step 2: Merge trades with SSIs
merged_df = trades_df.merge(ssi_df, on="Security", how="left")

# Step 3: Validate SSIs using regex for BIC format
def is_valid_bic(bic):
    if pd.isna(bic):
        return False
    return bool(re.match(r"^[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?$", bic))

merged_df["Valid_SSI_Format"] = merged_df["SSI"].apply(is_valid_bic)

# Step 4: Display results
print("\n🔍 Merged Data:")
print(merged_df)

print("\n🚫 Trades with Missing SSIs:")
print(merged_df[merged_df["SSI"].isna()])

print("\n⚠️ Trades with Invalid SSIs:")
print(merged_df[merged_df["Valid_SSI_Format"] == False])

# Step 5: Export to CSV
merged_df.to_csv("validated_trades.csv", index=False)
print("\n✅ File 'validated_trades.csv' has been saved.")

conn.close()
