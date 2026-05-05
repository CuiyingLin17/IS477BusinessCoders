import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/merged_dataset_cleaned.csv")
df["observation_date"] = pd.to_datetime(df["observation_date"])
df = df.sort_values("observation_date")

df.head()

print("Dataset shape:")
print(df.shape)

print("\nMissing values by column:")
print(df.isna().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nDate range:")
print(df["observation_date"].min(), "to", df["observation_date"].max())

print("\nSummary statistics:")
print(df.describe())
