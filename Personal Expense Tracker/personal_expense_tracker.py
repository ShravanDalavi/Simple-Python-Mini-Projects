import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Define the CSV file path
CSV_FILE = 'expenses.csv'

# Initialize the CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])

def add_expense(date, category, amount, description):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def get_user_input():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")
    return date, category, amount, description

def view_expenses():
    df = pd.read_csv(CSV_FILE)
    if df.empty:
        print("No expenses recorded.")
    else:
        print(df)

def analyze_expenses():
    df = pd.read_csv(CSV_FILE)
    if df.empty:
        print("No expenses to analyze.")
    else:
        summary = df.groupby('Category')['Amount'].sum().reset_index()
        print("Expense Summary by Category:")
        print(summary)

def visualize_expenses():
    df = pd.read_csv(CSV_FILE)
    if df.empty:
        print("No expenses to visualize.")
    else:
        summary = df.groupby('Category')['Amount'].sum()
        summary.plot(kind='bar', title='Expenses by Category')
        plt.xlabel('Category')
        plt.ylabel('Total Amount')
        plt.show()

def main_menu():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Visualize Expenses")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            date, category, amount, description = get_user_input()
            add_expense(date, category, amount, description)
            print("Expense added successfully!")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            analyze_expenses()
        elif choice == '4':
            visualize_expenses()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
