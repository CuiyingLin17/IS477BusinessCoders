import pandas as pd

files = {
    "UNRATE": "data/filtered_10yrs/UNRATE_filtered.csv",
    "CPIAUCSL": "data/filtered_10yrs/CPIAUCSL_filtered.csv",
    "RSAFS": "data/filtered_10yrs/RSAFS_filtered.csv",
    "DSPI": "data/filtered_10yrs/DSPI_filtered.csv"
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
  
