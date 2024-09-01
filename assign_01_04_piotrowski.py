# Alexander Piotrowski
# Dr. Marshall CBIS 4210
# 8/30/2024
def main():
    # Given sales data
    sales = [250.0, 450.5, 320.75, 560.0, 610.25, 485.0, 290.0, 600.0]

    # 1. Calculate the Total Sales
    total_sales = sum(sales)

    # 2. Calculate the Average Daily Sales
    average_sales = total_sales / len(sales)

    # 3. Identify the Highest Sales Day
    highest_sales = max(sales)

    # 4. Identify the Lowest Sales Day
    lowest_sales = min(sales)

    # 5. Calculate the Number of Days with Sales Above $500
    days_above_500 = len([sale for sale in sales if sale > 500])

    # Print the results
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Average Daily Sales: ${average_sales:.2f}")
    print(f"Highest Sales Day: ${highest_sales:.2f}")
    print(f"Lowest Sales Day: ${lowest_sales:.2f}")
    print(f"Days with Sales Above $500: {days_above_500}")


if __name__ == "__main__":
    main()
