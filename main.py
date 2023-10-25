from flask import Flask, render_template, request, jsonify, redirect, Response
from models import Expense, Income
from database import session
import csv
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for adding an expense
@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense_date = request.form.get('expense-date')
    expense_description = request.form.get('expense-description')
    expense_category = request.form.get('expense-category')
    expense_amount = float(request.form.get('expense-amount'))
    
    new_expense = Expense(
        expense_date=expense_date,
        expense_description=expense_description,
        expense_category=expense_category,
        expense_amount=expense_amount
    )
    
    session.add(new_expense)
    session.commit()
    
    response_data = {
        'message': 'Expense added successfully',
    }
    
    return jsonify(response_data), 200

# Route for adding income
@app.route('/add_income', methods=['POST'])
def add_income():
    income_date = request.form.get('income-date')
    income_description = request.form.get('income-description')
    income_amount = float(request.form.get('income-amount'))
    
    new_income = Income(
        income_date=income_date,
        income_description=income_description,
        income_amount=income_amount
    )
    
    session.add(new_income)
    session.commit()
    
    response_data = {
        'message': 'Income added successfully',
    }
    
# Route for deleting income
@app.route('/dashboard/delete_income/<int:income_id>', methods=['POST'])
def delete_income(income_id):
    income = session.query(Income).filter_by(id=income_id).first()

    if income:
        session.delete(income)
        session.commit()
        response_data = {
            'message': 'Income deleted successfully',
        }
    else:
        response_data = {
            'message': 'Income not found',
        }

    return jsonify(response_data)

# Route to get transactions
@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    expenses = session.query(Expense).all()
    incomes = session.query(Income).all()

    expense_data = [
        {
            'id': expense.id,
            'date': expense.expense_date,
            'description': expense.expense_description,
            'category': expense.expense_category,
            'amount': expense.expense_amount,
            'type': 'expense'
        }
        for expense in expenses
    ]

    income_data = [
        {
            'id': income.id,
            'date': income.income_date,
            'description': income.income_description,
            'amount': income.income_amount,
            'type': 'income'
        }
        for income in incomes
    ]
    
    transactions = expense_data + income_data

    return jsonify(transactions)

# Route to display the transactions in an HTML template
@app.route('/dashboard/view_transactions', methods=['GET'])
def view_transactions():
    expenses = session.query(Expense).all()
    incomes = session.query(Income).all()
    
    return render_template('transactions.html', incomes=incomes, expenses=expenses)

#Route to display the charts
@app.route('/dashboard/reports')
def reports():
    return render_template('reports.html')

# Route for deleting a transaction by ID
@app.route('/delete_transaction/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    expense = Expense.get_transaction_by_id(session, transaction_id)
    income = Income.get_transaction_by_id(session, transaction_id)

    if expense:
        session.delete(expense)
        session.commit()
        response_data = {
            'message': 'Expense deleted successfully',
        }
    elif income:
        session.delete(income)
        session.commit()
        response_data = {
            'message': 'Income deleted successfully',
        }
    else:
        response_data = {
            'message': 'Transaction not found',
        }

    return jsonify(response_data)

# Route for updating a transaction
@app.route('/update_transaction/<int:transaction_id>', methods=['POST'])
def update_transaction(transaction_id):
    expense = session.query(Expense).filter_by(id=transaction_id).first()
    income = session.query(Income).filter_by(id=transaction_id).first()

    if expense:
        expense.expense_date = request.form.get('expense-date')
        expense.expense_description = request.form.get('expense-description')
        expense.expense_category = request.form.get('expense-category')
        expense.expense_amount = float(request.form.get('expense-amount'))
        session.commit()
        response_data = {
            'message': 'Expense updated successfully',
        }
    elif income:
        income.income_date = request.form.get('income-date')
        income.income_description = request.form.get('income-description')
        income.income_amount = float(request.form.get('income-amount'))
        session.commit()
        response_data = {
            'message': 'Income updated successfully',
        }
    else:
        response_data = {
            'message': 'Transaction not found',
        }

    return jsonify(response_data)

# Route to fetch all expense categories
@app.route('/get_expense_categories', methods=['GET'])
def get_expense_categories():
    categories = session.query(Expense.expense_category).distinct().all()
    category_names = [category[0] for category in categories]
    return jsonify(category_names)

# Route to download all transactions
@app.route('/download_all_transactions', methods=['GET'])
def download_all_transactions():
    transaction_type = request.args.get('type')

    if transaction_type == 'income':
        transactions = session.query(Income).all()
        filename = 'all_income_transactions.csv'
    elif transaction_type == 'expense':
        transactions = session.query(Expense).all()
        filename = 'all_expense_transactions.csv'
    else:
        return 'Invalid transaction type', 400

    if not transactions:
        return 'No transactions found', 404

    # a CSV string
    output = StringIO()
    writer = csv.writer(output)
    
    if transaction_type == 'income':
        writer.writerow(['Date', 'Description', 'Amount'])
        for transaction in transactions:
            writer.writerow([transaction.income_date, transaction.income_description, transaction.income_amount])
    else:
        writer.writerow(['Date', 'Description', 'Category', 'Amount'])
        for transaction in transactions:
            writer.writerow([transaction.expense_date, transaction.expense_description, transaction.expense_category, transaction.expense_amount])

    # a Flask Response with the CSV data
    response = Response(output.getvalue(), mimetype="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    
    return response
#Route for login
@app.route('/login')
def login():
    return render_template('login.html')

#Route for sigunp
@app.route('/signup')
def signup():
    return render_template('signup.html')

#Route for settings
@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
