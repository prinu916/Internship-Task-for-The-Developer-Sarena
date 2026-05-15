import pandas as pd

df = pd.read_csv("sales_data.csv", sep="\t")

print("First 5 Rows of Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df["Total_Sales"] = df["Total_Sales"].fillna(0)

df = df.drop_duplicates()

total_revenue = df["Total_Sales"].sum()

best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

highest_sale = df["Total_Sales"].max()

average_sales = df["Total_Sales"].mean()

print("\n========== SALES REPORT ==========")
print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Best Selling Product: {best_product}")
print(f"Highest Sale        : ₹{highest_sale:,.2f}")
print(f"Average Sales       : ₹{average_sales:,.2f}")
print("==================================")