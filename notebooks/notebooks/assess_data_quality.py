import pandas as pd

files = {
    "UNRATE": "UNRATE (1).csv",
    "CPIAUCSL": "CPIAUCSL.csv",
    "RSAFS": "RSAFS.csv",
    "DSPI": "DSPI.csv"
}

for name, path in files.items():
    print(f"\n=== {name} ===")
    df = pd.read_csv(path)

    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Data types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isna().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

    first_col = df.columns[0]
    df[first_col] = pd.to_datetime(df[first_col], errors="coerce")
    print("Date range:", df[first_col].min(), "to", df[first_col].max())
    print("\nFirst 5 rows:")
    print(df.head())
  
