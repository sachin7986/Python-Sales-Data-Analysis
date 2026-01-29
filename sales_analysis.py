import pandas as pd

def perform_analysis(file_path):
    print("---  Sales Data Analysis Project ---")
    
    # 1. Load the Dataset
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("Error: sales_data.csv not found.")
        return

    # 2. Explore & Clean Data
    # Checking for missing values (Requirement)
    missing_data = df.isnull().sum().sum()
    if missing_data > 0:
        df = df.fillna(0) # Handling missing values
        print(f" Cleaned {missing_data} missing values.")
    else:
        print(" No missing values detected.")

    # 3. Calculate Metrics (Requirement: At least 3 metrics)
    total_revenue = df['Total_Sales'].sum()
    total_units_sold = df['Quantity'].sum()
    avg_order_value = df['Total_Sales'].mean()
    
    # Finding the Best-Selling Product
    best_product = df.groupby('Product')['Quantity'].sum().idxmax()
    top_region = df.groupby('Region')['Total_Sales'].sum().idxmax()

    # 4. Display the Clean Formatted Report
    print("\n" + "="*30)
    print(" FINAL SALES REPORT")
    print("="*30)
    print(f" Total Revenue:       ₹{total_revenue:,.2f}")
    print(f" Total Units Sold:    {total_units_sold:,}")
    print(f" Average Order Value: ₹{avg_order_value:,.2f}")
    print(f" Best Selling Item:   {best_product}")
    print(f" Top Performing Region: {top_region}")
    print("="*30)

    # 5. Exporting results for GitHub documentation
    with open('analysis_report.md', 'w', encoding='utf-8') as f:
        f.write("# Sales Analysis Summary\n")
        f.write(f"- **Total Revenue:** ₹{total_revenue:,.2f}\n")
        f.write(f"- **Total Units Sold:** {total_units_sold}\n")
        f.write(f"- **Top Product:** {best_product}\n")

if __name__ == "__main__":
    perform_analysis('sales_data.csv')