from expense import run_expense_input
from analyze import run_analysis

while True:
    print("1. Add Expense")
    print("2. Analyze Expense")
    print("3. Exit")

    choice = input("Choose 1-3: ")
    
    if choice == "1":
        run_expense_input()
    elif choice == "2":
        run_analysis()
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option")
