import pandas as pd
import matplotlib.pyplot as plt
import os

try:
    os.makedirs("visualizations", exist_ok=True)

    df = pd.read_csv("data/sales_data.csv", sep="\t")

    print("First 5 Rows:")
    print(df.head())

    df = df.drop_duplicates()

    df["Total_Sales"] = df["Total_Sales"].fillna(0)

    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

    total_revenue = df["Total_Sales"].sum()

    best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

    product_sales = df.groupby("Product")["Total_Sales"].sum()

    df["Month"] = df["Date"].dt.month_name()
    monthly_sales = df.groupby("Month")["Total_Sales"].sum()

    plt.figure(figsize=(8,5))

    plt.bar(product_sales.index, product_sales.values)

    plt.title("Product Sales Comparison")
    plt.xlabel("Products")
    plt.ylabel("Sales")

    plt.savefig("visualizations/bar_chart.png")

    plt.figure(figsize=(8,5))

    plt.plot(monthly_sales.index,
             monthly_sales.values,
             marker='o')

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.savefig("visualizations/line_chart.png")
    plt.show()
    

    print("\n========== SALES REPORT ==========")
    print(f"Total Revenue       : ₹{total_revenue:,.2f}")
    print(f"Best Selling Product: {best_product}")
    print("Charts created successfully!")
    print("==================================")

except FileNotFoundError:
    print("Dataset file not found.")

except Exception as e:
    print("An error occurred:", e)