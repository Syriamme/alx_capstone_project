from flask import Flask, render_template, request, jsonify, redirect
from models import Expense, Income
from database import session

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
    
    return jsonify(response_data)

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

if __name__ == '__main__':
    app.run(debug=True)
