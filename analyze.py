import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])

if df.isnull().sum().any():
    print("Warning: Missing valies found:")
    print(df.isnull().sum())
else:
    print("No missing values found.")


def first_five():
    print(df.head(5))

def total_spent():
    print("Total spent:", df['amount'].sum())

def statistics():
    print("Mean:", round(np.mean(df["amount"])))
    print("Median:", round(np.median(df["amount"])))
    print("Standard Deviation:", round(np.std(df["amount"])))
    
def top_expenses():
    print("Top 5 biggest expenses:")
    print(df.sort_values(by = "amount", ascending=False).head(5))

def by_category():
    category_data = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    category_data.plot(kind = "bar")
    plt.title("Spending by Category")
    plt.show()


def by_date():
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        selected = df[df["date"] == pd.to_datetime(date)]
        if selected.empty:
            print("No records found for this date.")
        else:
            print(selected)
    except:
        print("❌ Invalid date format.")


def show_menu():
    print("\n💼 Expense Analyzer CLI")
    print("1. View First 5 Entries")
    print("2. View Total Spent")
    print("3. View Statistics (mean, median, std)")
    print("4. View Top 5 Expenses")
    print("5. View Spending by Category")
    print("6. View by Specific Date")
    print("7. Exit")

    
options_map = {
    "1": first_five,
    "2": total_spent,
    "3": statistics,
    "4": top_expenses,
    "5": by_category,
    "6": by_date
    }

def run_analysis():
    while True:
        show_menu()
        choice = input("Choose an option(1-7): ")
        if choice == "7":
            print("👋 Goodbye!")
            break
        elif choice in options_map:
            print()  # spacing
            options_map[choice]()
        else:
            print("Invalid option. Try again.")

        input("\nPress Enter to continue...")

