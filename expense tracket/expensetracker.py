import pandas as pd
import matplotlib.pyplot as PageLayout
from datetime import datetime


#File to store data
EXPENSE_FILE = "expenses.csv"

#initializie CSV file if it does not exist
try:
    pd.read_csv(EXPENSE_FILE)
except FileNotFoundError:
    pd.DataFrame(columns=["Date","Amount","Category"]).to_csv(EXPENSE_FILE, index=False)    


def add_expense(amount, category ,date=None):
    """Add a new expense to the file."""
    date = date or datetime.now().strftime("%Y-%m-%d")
    expense = pd.DataFrame([[date,amount,category]], columns=["Date","Amount","category"])
    expense.to_csv(EXPENSE_FILE,mode='a',header=False, index=False)
    print("Expense added successfully!")  

def view_expenses(month=None, category=None):
    """"view expenses, optionally filtered by month and/or category."""
    data = pd.read_csv(EXPENSE_FILE)
    if month:
        data = data[data['Date'].str.startswith(month)]
    if category:
        data = data[data['Category'] == category]
    print("\nExpenses")
    print(data)
    return data    


def generate_report(month=None):
    """Generate a bar and pie chart for the selecting month"""
    data = view_expenses(month)
    if data.empty:
        print("No data to display for  the given month")
        return
    
    category_data = data.groupby('Category')['Amount'].sum()


    #bar chart
    category_data.plot(kind='bar',title='Expense by category',color='skyblue', figsize=(8,5))
    PageLayout.ylabel("Amount")
    PageLayout.xlabel("Category")
    PageLayout.tight_layout()
    PageLayout.show()

    category_data.plot(kind='pie', title='Expense Distribution', autopct='%1.1f%%', figsize=(6, 6))
    PageLayout.ylabel("")  # Hide y-label for pie chart
    PageLayout.tight_layout()
    PageLayout.show()

def main():
    """Main menu for the expense tracker app."""
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
            add_expense(amount, category, date)
        elif choice == "2":
            month = input("Enter the month (YYYY-MM) to filter or leave blank: ")
            category = input("Enter the category to filter or leave blank: ")
            view_expenses(month, category)
        elif choice == "3":
            month = input("Enter the month (YYYY-MM) to filter or leave blank: ")
            generate_report(month)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()