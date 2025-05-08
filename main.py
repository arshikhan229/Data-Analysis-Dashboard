import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
try:
    df = pd.read_csv("sales_data.csv", parse_dates=["Order Date"])
    print("✅ Data loaded successfully!")
except Exception as e:
    print("❌ Error loading sales_data.csv:", e)
    exit()

print("📊 Columns:", df.columns.tolist())
print("🔍 Sample Data:\n", df.head())

# Group by Product
product_sales = df.groupby("Product")["Revenue"].sum()

# Group by Region
region_sales = df.groupby("Region")["Revenue"].sum()

# Time-series revenue trend
daily_revenue = df.groupby("Order Date")["Revenue"].sum()

# Plot 1: Revenue by Product
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar", color="skyblue")
plt.title("Total Revenue by Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

# Plot 2: Revenue by Region
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar", color="salmon")
plt.title("Total Revenue by Region")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.show()

# Plot 3: Daily Revenue Trend
plt.figure(figsize=(10, 5))
daily_revenue.plot(marker='o', linestyle='-', color='green')
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("daily_revenue_trend.png")
plt.show()
