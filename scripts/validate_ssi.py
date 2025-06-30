import pandas as pd

# Read trade data
trades_df = pd.read_csv("trades.csv")

# Read SSI reference data
ssi_df = pd.read_csv("ssi_master.csv")

# ✅ Merge the two tables based on Security
merged_df = pd.merge(trades_df, ssi_df, on="Security", how="left")

# Show the merged table
print("Merged Trade with SSI:")
print(merged_df)

# ✅ Find trades where SSI is missing
missing_ssis = merged_df[merged_df["SSI"].isnull()]

print("\nTrades with Missing SSIs:")
print(missing_ssis)
# Step 6: Check if SSI format is valid

def is_valid_ssi(ssi):
    if pd.isnull(ssi):
        return False
    if len(ssi) not in [8, 11]:
        return False
    if not ssi[:4].isalpha():
        return False
    if not ssi[4:6].isalpha():
        return False
    if not ssi.isalnum():
        return False
    if not ssi.isupper():
        return False
    return True

# Apply validation to each row
merged_df["Valid_SSI_Format"] = merged_df["SSI"].apply(is_valid_ssi)

# Show invalid SSIs
invalid_format = merged_df[merged_df["Valid_SSI_Format"] == False]

print("\nTrades with Invalid SSI Format:")
print(invalid_format)
conn = sqlite3.connect("scripts/ssi_data.db")