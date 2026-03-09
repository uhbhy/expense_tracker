💰 Personal Expense Tracker

A simple command-line based Personal Expense Tracker built with Python that allows users to log daily expenses, categorize spending, track monthly budgets, and persist data using CSV file handling.

📌 Features

✅ Add daily expenses

✅ Categorize expenses (Food, Travel, Shopping, etc.)

✅ Track spending against a monthly budget

✅ Automatic CSV file saving

✅ Load previously saved expenses on startup

✅ Input validation for date and amount

✅ Clean interactive menu-driven interface


📂 Project Structure
expense_tracker_project/
│
├── expense_tracker.py
├── expenses.csv   (auto-created after saving)
└── README.md


🧾 How It Works
1. Add Expense

You will be prompted to enter:

-Date (YYYY-MM-DD)

-Category

-Amount

-Description

-Expenses are stored as dictionaries in memory and written to expenses.csv.

2. View Expenses

Displays all stored expenses in a formatted output.

3. Track Budget

-Set a monthly budget

-Calculates total expenses

-Displays:

--Remaining balance  Or 
--budget exceeded warning

4. Save & Load

-Expenses are saved to expenses.csv

-Automatically loads previous records on startup

📊 Example CSV Format
date,category,amount,description
2026-03-01,Food,250,Lunch
2026-03-02,Travel,500,Cab ride


🔒 Input Validation

-Date validated using datetime.strptime

-Amount validated as positive float

-Incomplete entries are skipped during display

🎯 Learning Objectives Achieved

This project demonstrates:

-File handling (CSV read/write)

-Modular function design

-Data validation

-Loop-based menu systems

-Basic financial tracking logic