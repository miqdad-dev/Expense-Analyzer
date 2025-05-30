import csv as csv
import os as os


class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount =  float(amount)
        self.category = category
        self.date = date

    def to_csv_row(self):
        return [self.name, self.amount, self.category, self.date]
    
expenses = []

categories = ("food","transport","shopping","bills", "others")
if not os.path.exists("data.csv"):
    with open("data.csv", "a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "amount", "category", "date"])


def add_expenses(name, amount, category, date):
    new_expense = Expense(name, float(amount), category, date)
    expenses.append(new_expense)
    with open("data.csv", "a", newline="") as file:
         writer = csv.writer(file)
         writer.writerow(expenses[-1].to_csv_row())
    print(f"Saved: {new_expense}")


def run_expense_input():
    while True:
        name = input("Enter an Item name: ")
        while True:
            try:
                amount = float(input("Whats the amount "))
                break
            except ValueError:
                print("Enter a valid number.")
                exit()

        date = input("Enter date (e.g. 2024-05-26): ")


        print(f"Pick a category from ", categories)
        for cat in categories:
            print(f"- {cat}")
        pick_category = input("Pick from above: ").strip().lower()
        if pick_category in categories:
                add_expenses(name, amount, pick_category, date)
                print("Item added successfully")
        else:
                print("Invalid category. Item not added.")
        print(f"Data saved Succesfully")

        cont = input("Do you want to add more: (yes/no): ").lower()
        if cont != "yes":
            break
