import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/merged_dataset_cleaned.csv")
df["observation_date"] = pd.to_datetime(df["observation_date"])
df = df.sort_values("observation_date")

df.head()

plt.figure(figsize=(10,6))
plt.plot(df["observation_date"], df["retail_sales_millions"])
plt.title("Retail Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Retail Sales (Millions)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("results/retail_sales_over_time.png")
plt.show()

corr = df[[
    "unemployment_rate",
    "inflation_rate",
    "disposable_personal_income_millions",
    "retail_sales_millions"
]].corr()

print(corr)
corr.to_csv("results/correlation_matrix.csv")

import numpy as np

x = df["disposable_personal_income_millions"]
y = df["retail_sales_millions"]

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

plt.figure(figsize=(8,6))
plt.scatter(x, y)
plt.plot(x, p(x))
plt.title("Disposable Personal Income vs Retail Sales")
plt.xlabel("Disposable Personal Income (Millions)")
plt.ylabel("Retail Sales (Millions)")
plt.tight_layout()
plt.savefig("results/income_vs_retail_sales.png")
plt.show()

import numpy as np

plot_df = df[["unemployment_rate", "retail_sales_millions"]].dropna()

x = plot_df["unemployment_rate"]
y = plot_df["retail_sales_millions"]

plt.figure(figsize=(8,6))
plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x))

plt.title("Unemployment Rate vs Retail Sales")
plt.xlabel("Unemployment Rate")
plt.ylabel("Retail Sales (Millions)")
plt.tight_layout()
plt.savefig("results/unemployment_vs_retail_sales.png")
plt.show()


