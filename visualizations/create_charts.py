
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/cleaned_sales.csv", encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"])

os.makedirs("visualizations", exist_ok=True)
sns.set_theme(style="whitegrid")

# Chart 1: Sales by Region
plt.figure(figsize=(8, 5))
df.groupby("Region")["Sales"].sum().sort_values().plot(kind="bar")
plt.title("Total Sales by Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("visualizations/sales_by_region.png")
plt.close()

# Chart 2: Profit by Category
plt.figure(figsize=(8, 5))
df.groupby("Category")["Profit"].sum().plot(kind="bar")
plt.title("Total Profit by Category")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig("visualizations/profit_by_category.png")
plt.close()

# Chart 3: Sales by Category
plt.figure(figsize=(8, 5))
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Total Sales by Category")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("visualizations/sales_by_category.png")
plt.close()

# Chart 4: Monthly Sales Trend
monthly = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
monthly.index = monthly.index.astype(str)

plt.figure(figsize=(12, 5))
monthly.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png")
plt.close()

# Chart 5: Sales by Segment
plt.figure(figsize=(8, 5))
df.groupby("Segment")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Segment")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/sales_by_segment.png")
plt.close()

print("All 5 charts created successfully!")
print("Check the visualizations folder.")
