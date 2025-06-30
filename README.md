# SSI Validation Engine – Python + Pandas

This project simulates a **Standing Settlement Instruction (SSI) validation tool** that checks for completeness and correctness of settlement data in securities operations.

---

##  Goal

Validate SSI data for trades to catch:

- Missing SSIs
- Incorrect or malformed SSIs
- Format compliance (SWIFT/BIC-like structure)

---

## Data Used

- `trades.csv`: Contains Trade ID, Security, and Amount
- `ssi_master.csv`: Contains valid SSIs for each security

---

## What the Code Does (So Far)

1. **Reads** both CSVs (trade data and SSI reference)
2. **Merges** them using the `Security` column
3. **Flags trades** with:
   - Missing SSI
   - Invalid SSI format (e.g., wrong length, lowercase, special chars)
4. **Prints results** to terminal in readable table format

---

##  How to Run

From the project root:

```bash
python scripts/validate_ssi.py


Example Output

Merged Trade with SSI:
  TradeID Security  Amount          SSI
0     T1      IBM    1000  CITIUS33XXX
1     T2     AAPL    2000  BOFAUS3NXXX
2     T3     TSLA    3000          NaN

Trades with Missing SSIs:
  TradeID Security  Amount  SSI
2     T3     TSLA    3000  NaN

Trades with Invalid SSI Format:
  TradeID Security  Amount  SSI  Valid_SSI_Format
2     T3     TSLA    3000  NaN              False