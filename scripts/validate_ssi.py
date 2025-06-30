import pandas as pd

# Corrected paths — point to the file inside scripts folder
trades_df = pd.read_csv("trades.csv")
# Comment out or remove the line below for now
# ssi_df = pd.read_csv("scripts/ssi_master.csv")

print("Trades:")
print(trades_df)