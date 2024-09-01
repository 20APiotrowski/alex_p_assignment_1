# Alexander Piotrowski
# Dr. Marshall CBIS 4210
# 8/30/2024
def main():
    # Given employee data
    employees = [
        {"name": "Alice", "base_salary": 50000, "bonus": 5000},
        {"name": "Bob", "base_salary": 60000, "bonus": 8000},
        {"name": "Charlie", "base_salary": 45000, "bonus": 3000},
        {"name": "Diana", "base_salary": 55000, "bonus": 7000},
    ]

    # Initialize the overall payroll cost
    overall_payroll = 0

    # Calculate and display each employee's total salary
    for employee in employees:
        total_salary = employee["base_salary"] + employee["bonus"]
        overall_payroll += total_salary
        print(f"Name: {employee['name']}, Total Salary: ${total_salary:.2f}")

    # Display the overall payroll cost
    print(f"Overall Payroll Cost: ${overall_payroll:.2f}")


if __name__ == "__main__":
    main()
