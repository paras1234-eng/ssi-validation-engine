# SSI Validation Automation Project (Python + SQL)

 **What this project does:**  
This project reads trade data and Standing Settlement Instructions (SSIs), validates them for missing or incorrect records, and outputs a clean report showing any mismatches or format issues.

---

##  Technologies Used

- Python 
- pandas (for data analysis)
- SQLite (for database storage and SQL queries)
- VS Code + Terminal (to run the scripts)

---

##  File Structure

<pre> ``` scripts/ ├── validate_ssi.py # Reads CSVs, merges, validates, outputs issues ├── load_to_db.py # Loads CSVs into SQLite database ├── read_from_db.py # Reads from DB using SQL ├── validate_from_db.py # Full validation using SQL + Python ├── save_validated_to_db.py # Saves validated results back to DB ├── query_invalid_ssis.py # SQL query for only invalid SSIs ├── trades.csv # Sample trade data ├── ssi_master.csv # Reference SSI data ├── validated_trades.csv # Output file with results ssi_data.db # SQLite database file (auto-created) LICENSE # License file README.md # You are here ``` </pre>

##  How to Run the Scripts


You can run each file in the terminal like this:

```bash
python scripts/validate_ssi.py
python scripts/load_to_db.py
python scripts/read_from_db.py
python scripts/validate_from_db.py
python scripts/save_validated_to_db.py
python scripts/query_invalid_ssis.py
---

----
How to Test the Output

python scripts/query_invalid_ssis.py

  TradeID   Security  Amount   SSI  Valid_SSI_Format
0    T3       TSLA     3000  None                 0

---
----
## SQL automation project.

This is my first Python + SQL automation project.

It is designed to show:
- How trade and SSI data can be read, validated, and reported
- How Python and SQL can be used together to automate real-world data checks
- A basic simulation of how actual securities operations handle instruction mismatches

---
