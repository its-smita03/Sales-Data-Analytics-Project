
import pandas as pd

df = pd.read_csv("data/sales.csv", encoding="latin1")

print("Duplicate rows:", df.duplicated().sum())

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df = df.drop_duplicates()

df.to_csv("data/cleaned_sales.csv", index=False)

print("\nCleaned Dataset Shape:", df.shape)
print("Total Missing Values:", df.isnull().sum().sum())
print("\nCleaned dataset saved successfully!")
