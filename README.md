# Sales Data Analytics Project

## Project Overview
This project analyzes Superstore sales data to identify sales trends, product performance, regional performance, and business opportunities using Python and Power BI.

## Project Objectives
- Inspect and clean the sales dataset.
- Perform Exploratory Data Analysis (EDA).
- Create visualizations to understand sales and profit patterns.
- Build an interactive Power BI dashboard.
- Identify business insights and provide recommendations.

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Power BI Desktop
- Git and GitHub

## Dataset
The project uses the Superstore sales dataset containing order dates, customer details, product categories, regions, sales, quantity, discounts, and profit.

## Project Structure
- `data/sales.csv` — Original dataset
- `data/cleaned_sales.csv` — Cleaned dataset
- `inspect_data.py` — Dataset inspection
- `clean_data.py` — Data cleaning
- `eda_analysis.py` — Exploratory data analysis
- `visualizations/` — Python visualization script and charts
- `powerbi/Sales_Analytics_Dashboard.pbix` — Power BI dashboard

## Key Findings
- Total Sales: 2,297,200.86
- Total Profit: 286,397.02
- Total Orders: 5,009
- West was the highest-sales region, with 725,457.82 in sales.
- Technology was the highest-sales category, with 836,154.03 in sales.
- The Canon imageCLASS 2200 Advanced Copier was the top product by sales, with 61,599.82.

## Recommendations
1. Analyze discounts and low-profit products in the Furniture category to identify opportunities to improve profitability.
2. Study successful sales strategies in the West region and evaluate whether they can be applied to other regions.

## Dashboard
The interactive Power BI dashboard includes KPI cards, sales and profit charts, a monthly sales trend, and slicers for filtering the data.

## How to Run
1. Install Python.
2. Install the required libraries:
   `pip install pandas matplotlib seaborn`
3. Run the data inspection script:
   `python inspect_data.py`
4. Run the cleaning script:
   `python clean_data.py`
5. Run the EDA script:
   `python eda_analysis.py`
6. Generate charts:
   `python visualizations/create_charts.py`
7. Open `powerbi/Sales_Analytics_Dashboard.pbix` in Power BI Desktop.

## Project Status
Core data cleaning, EDA, Python visualizations, and the Power BI dashboard have been completed.

## Author
Smita Powar