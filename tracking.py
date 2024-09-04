import csv
from datetime import datetime

class PersonalFinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, transaction_type, description=""):
        transaction = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'category': category,
            'type': transaction_type,  # "income" or "expense"
            'description': description
        }
        self.transactions.append(transaction)
        print("Transaction added successfully!")

    def view_summary(self):
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = total_income - total_expenses
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")

    def export_data(self, filename="transactions.csv"):
        keys = self.transactions[0].keys()
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.transactions)
        print(f"Data exported successfully to {filename}!")

    def import_data(self, filename="transactions.csv"):
        with open(filename, newline='') as input_file:
            reader = csv.DictReader(input_file)
            self.transactions = list(reader)
        print(f"Data imported successfully from {filename}!")

# Example Usage
tracker = PersonalFinanceTracker()

# Add income
tracker.add_transaction(5000, 'Salary', 'income', 'August Salary')

# Add expense
tracker.add_transaction(1500, 'Rent', 'expense', 'Monthly Rent')

# View summary
tracker.view_summary()

# Export data
tracker.export_data()

# Import data
tracker.import_data()
