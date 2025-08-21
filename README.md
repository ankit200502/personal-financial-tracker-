Personal Finance Tracker
This is a command-line application built in Python to help users track their income, expenses, and financial goals. The tool provides a simple and effective way to manage personal finances by recording transactions, generating reports, and visualizing spending habits.

Features
Transaction Management: Add, view, and manage financial transactions, categorizing them as either income or expense.

Data Persistence: All transaction data is saved to a file (transactions.pkl) using Python's pickle module, so your records are preserved between sessions.

Sorting and Filtering: Easily sort transactions by date or amount and filter expenses to find those over a specific value.

Balance Calculation: The application automatically calculates and displays your current balance based on all recorded income and expenses.

ASCII Bar Chart: A bonus feature that provides a visual representation of your monthly spending, rendered as a simple bar chart directly in the terminal.

How to Run
Save the Code: Save the provided Python code into a file named finance_tracker.py.

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the following command:

Bash

python finance_tracker.py
Follow the Menu: The application will present a menu with options to add transactions, view data, and perform other actions. Simply enter the number corresponding to your desired action and press Enter.

Sample Output
Here is a sample of what the program's output looks like when you interact with it.

--- Personal Finance Tracker Menu ---
1. Add a new transaction
2. View all transactions
3. Get current balance
4. Search for transactions
5. Filter expenses over a certain amount
6. Sort transactions
7. View monthly spending chart
8. Exit
Enter your choice: 1
Enter type (income/expense): income
Enter category: Salary
Enter amount: 3000
Enter date (YYYY-MM-DD): 2025-08-01
Enter description: Monthly paycheck
Data saved successfully.

--- Personal Finance Tracker Menu ---
1. Add a new transaction
2. View all transactions
3. Get current balance
4. Search for transactions
5. Filter expenses over a certain amount
6. Sort transactions
7. View monthly spending chart
8. Exit
Enter your choice: 1
Enter type (income/expense): expense
Enter category: Groceries
Enter amount: 150.50
Enter date (YYYY-MM-DD): 2025-08-05
Enter description: Weekly groceries
Data saved successfully.

--- Personal Finance Tracker Menu ---
1. Add a new transaction
2. View all transactions
3. Get current balance
4. Search for transactions
5. Filter expenses over a certain amount
6. Sort transactions
7. View monthly spending chart
8. Exit
Enter your choice: 2

--- All Transactions ---
1. Type: Income | Category: Salary | Amount: 3000.00 | Date: 2025-08-01 | Desc: Monthly paycheck
2. Type: Expense | Category: Groceries | Amount: 150.50 | Date: 2025-08-05 | Desc: Weekly groceries

--- Personal Finance Tracker Menu ---
1. Add a new transaction
2. View all transactions
3. Get current balance
4. Search for transactions
5. Filter expenses over a certain amount
6. Sort transactions
7. View monthly spending chart
8. Exit
Enter your choice: 3

Your current balance is: $2849.50

--- Personal Finance Tracker Menu ---
1. Add a new transaction
2. View all transactions
3. Get current balance
4. Search for transactions
5. Filter expenses over a certain amount
6. Sort transactions
7. View monthly spending chart
8. Exit
Enter your choice: 7

--- Monthly Spending Bar Chart ---
2025-08: $  150.50 |████████████████████████████████████████████████████|
