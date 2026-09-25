expenses = []
def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    expenses.append({
        "category": category,
        "amount": amount
    })
    print("Expense added successfully!")
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpense List")
    print("-" * 30)
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']:.2f}")
def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
      
OUTPUT:
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit
Enter your choice: 2
No expenses recorded.
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit
Enter your choice: 3
Total Expenses: ₹0.00
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit
Enter your choice: 1
Enter expense category: 4
Enter amount: 5000
Expense added successfully!
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit
Enter your choice: 4
Thank you for using Expense Tracker!
