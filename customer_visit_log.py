# Alexander Piotrowski
# Dr. Marshall CBIS 4210
# 8/30/2024
def main():
    # Given data: number of customer visits for each day of the week
    visits = [50, 45, 60, 70, 65, 55, 40]

    # 1. Calculate the Total Visits
    total_visits = sum(visits)

    # 2. Calculate the Average Visits Per Day
    average_visits = total_visits / len(visits)

    # 3. Display the results
    print(f"Total Visits: {total_visits}")
    print(f"Average Visits Per Day: {average_visits:.2f}")


if __name__ == "__main__":
    main()
