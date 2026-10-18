
import pandas as pd

df = pd.read_csv("data/cleaned_sales.csv")

print("===== SALES DATA ANALYSIS =====")

print("\n1. Total Sales:")
print(round(df["Sales"].sum(), 2))

print("\n2. Total Profit:")
print(round(df["Profit"].sum(), 2))

print("\n3. Total Orders:")
print(df["Order ID"].nunique())

print("\n4. Total Quantity Sold:")
print(df["Quantity"].sum())

print("\n5. Sales by Region:")
print(df.groupby("Region")["Sales"].sum().round(2))

print("\n6. Sales by Category:")
print(df.groupby("Category")["Sales"].sum().round(2))

print("\n7. Profit by Category:")
print(df.groupby("Category")["Profit"].sum().round(2))

print("\n8. Top 5 Products by Sales:")
print(df.groupby("Product Name")["Sales"].sum()
      .sort_values(ascending=False).head(5).round(2))

print("\n9. Monthly Sales:")
df["Order Date"] = pd.to_datetime(df["Order Date"])
monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()
print(monthly_sales.round(2))
