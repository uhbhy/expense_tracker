import csv
import os
from datetime import datetime

EXPENSE_FILE = "expenses.csv"

expenses = []
monthly_budget = 0.0

# Utility Validation Functions

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_amount(amount_text):
    try:
        value = float(amount_text)
        return value >= 0
    except ValueError:
        return False


# 1. Add Expense

def add_expense():
    print("\n--- Add Expense ---")

    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if validate_date(date):
            break
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

    category = input("Enter category (Food, Travel, etc.): ").strip()
    if not category:
        print("❌ Category cannot be empty.")
        return

    while True:
        amount = input("Enter amount: ")
        if validate_amount(amount):
            amount = float(amount)
            break
        print("❌ Invalid amount. Please enter a valid number.")

    description = input("Enter description: ").strip()
    if not description:
        print("❌ Description cannot be empty.")
        return

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    print("✅ Expense added successfully!")


# 2. View Expenses

def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for idx, expense in enumerate(expenses, start=1):
        if not all(key in expense for key in ("date", "category", "amount", "description")):
            print(f"⚠ Skipping incomplete entry #{idx}")
            continue

        print(f"""
Expense #{idx}
Date       : {expense['date']}
Category   : {expense['category']}
Amount     : ₹{expense['amount']:.2f}
Description: {expense['description']}
""")

# 3. Budget Tracking

def set_budget():
    global monthly_budget
    while True:
        budget_input = input("Enter your monthly budget: ")
        if validate_amount(budget_input):
            monthly_budget = float(budget_input)
            print(f"✅ Monthly budget set to ₹{monthly_budget:.2f}")
            break
        print("❌ Invalid amount. Try again.")


def calculate_total_expenses():
    return sum(expense["amount"] for expense in expenses)


def track_budget():
    if monthly_budget == 0:
        print("⚠ Please set your monthly budget first.")
        set_budget()

    total_spent = calculate_total_expenses()
    remaining = monthly_budget - total_spent

    print(f"\nTotal Spent: ₹{total_spent:.2f}")
    print(f"Monthly Budget: ₹{monthly_budget:.2f}")

    if remaining < 0:
        print("🚨 You have exceeded your budget!")
    else:
        print(f"✅ You have ₹{remaining:.2f} left for the month.")


# 4. Save & Load Expenses

def save_expenses():
    with open(EXPENSE_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)

    print("💾 Expenses saved successfully!")


def load_expenses():
    if not os.path.exists(EXPENSE_FILE):
        return

    with open(EXPENSE_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)


# 5. Interactive Menu

def display_menu():
    print("""
========= Personal Expense Tracker =========
1. Add Expense
2. View Expenses
3. Track Budget
4. Save Expenses
5. Exit
============================================
""")


def main():
    load_expenses()

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            track_budget()
        elif choice == "4":
            save_expenses()
        elif choice == "5":
            save_expenses()
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()