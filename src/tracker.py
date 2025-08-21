import pickle
import os
from datetime import datetime

# --- Data Structure ---
class Transaction:
    """Represents a single financial transaction."""
    def __init__(self, type, category, amount, date, description):
        self.type = type  # 'income' or 'expense'
        self.category = category
        self.amount = float(amount)
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description

# --- Main Application Logic ---
class FinanceTracker:
    """Manages all financial transactions, including CRUD operations and data persistence."""
    def __init__(self, filename='transactions.pkl'):
        self.filename = filename
        self.transactions = []
        self.load_data()

    def load_data(self):
        """Loads transaction data from a file using pickle."""
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                self.transactions = pickle.load(f)
            print("Data loaded successfully.")
        else:
            print("No saved data found. Starting with a new tracker.")

    def save_data(self):
        """Saves transaction data to a file using pickle."""
        with open(self.filename, 'wb') as f:
            pickle.dump(self.transactions, f)
        print("Data saved successfully.")

    def add_transaction(self, type, category, amount, date, description):
        """Adds a new transaction to the tracker."""
        try:
            new_transaction = Transaction(type, category, amount, date, description)
            self.transactions.append(new_transaction)
            self.save_data()
        except ValueError as e:
            print(f"Error adding transaction: {e}. Ensure amount is a number and date is in YYYY-MM-DD format.")

    def view_all_transactions(self):
        """Prints all transactions in the tracker."""
        if not self.transactions:
            print("No transactions to display.")
            return
        
        print("\n--- All Transactions ---")
        for i, t in enumerate(self.transactions, 1):
            print(f"{i}. Type: {t.type.capitalize():<7} | Category: {t.category:<10} | Amount: ${t.amount:7.2f} | Date: {t.date.strftime('%Y-%m-%d')} | Desc: {t.description}")

    def get_balance(self):
        """Calculates the current balance (income - expenses)."""
        total_income = sum(t.amount for t in self.transactions if t.type == 'income')
        total_expenses = sum(t.amount for t in self.transactions if t.type == 'expense')
        return total_income - total_expenses

    def search_transactions(self, query):
        """Searches for transactions by description or category."""
        results = [t for t in self.transactions if query.lower() in t.description.lower() or query.lower() in t.category.lower()]
        return results

    def filter_by_amount(self, min_amount, transaction_type='expense'):
        """Filters transactions of a specific type that are above a certain amount."""
        return [t for t in self.transactions if t.type == transaction_type and t.amount >= min_amount]

    def sort_transactions(self, key='date', reverse=False):
        """Sorts transactions by a specified key (e.g., date, amount)."""
        try:
            self.transactions.sort(key=lambda t: getattr(t, key), reverse=reverse)
            print("Transactions sorted successfully.")
        except AttributeError:
            print(f"Error: Cannot sort by key '{key}'. Valid keys are 'date', 'amount', 'type', 'category', 'description'.")

    def generate_spending_chart(self):
        """Generates an ASCII bar chart for monthly spending."""
        monthly_expenses = {}
        for t in self.transactions:
            if t.type == 'expense':
                month_year = t.date.strftime('%Y-%m')
                monthly_expenses[month_year] = monthly_expenses.get(month_year, 0) + t.amount

        if not monthly_expenses:
            print("No expenses recorded to generate a chart.")
            return

        print("\n--- Monthly Spending Bar Chart ---")
        max_amount = max(monthly_expenses.values())
        bar_width = 50

        for month, amount in sorted(monthly_expenses.items()):
            bar_length = int((amount / max_amount) * bar_width)
            bar = '█' * bar_length
            print(f"{month}: ${amount:7.2f} |{bar}|")

# --- User Interface ---
def main_menu():
    """Provides a simple command-line interface for the user."""
    tracker = FinanceTracker()
    while True:
        print("\n--- Personal Finance Tracker Menu ---")
        print("1. Add a new transaction")
        print("2. View all transactions")
        print("3. Get current balance")
        print("4. Search for transactions")
        print("5. Filter expenses over a certain amount")
        print("6. Sort transactions")
        print("7. View monthly spending chart")
        print("8. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            type = input("Enter type (income/expense): ").lower()
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            tracker.add_transaction(type, category, amount, date, description)

        elif choice == '2':
            tracker.view_all_transactions()

        elif choice == '3':
            balance = tracker.get_balance()
            print(f"\nYour current balance is: ${balance:.2f}")

        elif choice == '4':
            query = input("Enter search query (e.g., 'rent', 'groceries'): ")
            results = tracker.search_transactions(query)
            if results:
                print("\n--- Search Results ---")
                for t in results:
                    print(f"Type: {t.type.capitalize()}, Amount: ${t.amount:.2f}, Desc: {t.description}")
            else:
                print("No transactions found matching your query.")

        elif choice == '5':
            try:
                min_amount = float(input("Enter minimum amount to filter expenses by: "))
                filtered_list = tracker.filter_by_amount(min_amount)
                if filtered_list:
                    print(f"\n--- Expenses over ${min_amount:.2f} ---")
                    for t in filtered_list:
                        print(f"Category: {t.category}, Amount: ${t.amount:.2f}, Date: {t.date.strftime('%Y-%m-%d')}")
                else:
                    print("No expenses found above that amount.")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '6':
            key = input("Sort by (date, amount, type, category, description): ").lower()
            reverse = input("Reverse order? (yes/no): ").lower() == 'yes'
            tracker.sort_transactions(key, reverse)
            tracker.view_all_transactions()

        elif choice == '7':
            tracker.generate_spending_chart()

        elif choice == '8':
            print("Exiting. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
