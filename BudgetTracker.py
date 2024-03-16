def main():
    print("Welcome to the Budget Tracker!")
    income = float(input("Enter your income for this month: "))
    expenses = []
    total_expenses = 0
    
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Remaining Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            expense = float(input("Enter the amount of expense: "))
            expenses.append(expense)
            total_expenses += expense
            print("Expense added successfully!")
        elif choice == '2':
            print("\nExpenses:")
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. ${expense:.2f}")
        elif choice == '3':
            remaining_balance = income - total_expenses
            print(f"\nRemaining Balance: ${remaining_balance:.2f}")
        elif choice == '4':
            print("Thank you for using Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
