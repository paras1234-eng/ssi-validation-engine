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