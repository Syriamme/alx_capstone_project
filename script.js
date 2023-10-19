/*
// Event listener for input in the expense amount field
const expenseerror = document.getElementById("error-message");

expenseAmountInput.addEventListener("input", function () {
    const newAmount = parseFloat(expenseAmountInput.value);
    if (isNaN(newAmount) || newAmount <= 0) {
        expenseerror.textContent = "Invalid amount";
    } else {
        expenseerror.textContent = "";
    }
});

// Event listener for the "Add Expense" button

const expensebtnerror = document.getElementById("error-message");
const addExpenseButton = document.getElementById("add-expense-button");

addExpenseButton.addEventListener("click", function (event) {
    event.preventDefault();
    const expenseDate = document.getElementById("expense-date").value;
    const expenseDescription = document.getElementById("expense-description").value;
    const expenseCategory = document.getElementById("expense-category").value;
    const expenseAmount = parseFloat(document.getElementById("expense-amount").value);

    if (!expenseDate || !expenseDescription || !expenseCategory || isNaN(expenseAmount) || expenseAmount <= 0) {
        expensebtnerror.textContent = "Please fill in all fields";
    } else {
        expensebtnerror.textContent = "";
        $.ajax({
            type: 'POST',
            url: '/add_expense',
            data: $('#expense-form').serialize(),
            success: function(response) {
                console.log(response);
                $('#expense-form')[0].reset();
            },
            error: function(error) {
                console.error(error);
            }
        });
    }
});

// Event listener for input in the income amount field
const incomeAmountInput = document.getElementById("income-amount");
const incomeerror = document.getElementById("error-message");

incomeAmountInput.addEventListener("input", function () {
    const newincome = parseFloat(incomeAmountInput.value);
    if (isNaN(newincome) || newincome <= 0) {
        incomeerror.textContent = "Invalid amount";
    } else {
        incomeerror.textContent = "";
    }
});

// Event listener for the "Add Income" button
const incomebtnerror = document.getElementById("error-message");
const addIncomeButton = document.getElementById("add-income-button");

addIncomeButton.addEventListener("click", function (event) {
    event.preventDefault();
    const incomeDate = document.getElementById("income-date").value;
    const incomeDescription = document.getElementById("income-description").value;
    const incomeCategory = document.getElementById("income-category").value;
    const incomeAmount = parseFloat(document.getElementById("income-amount").value);

    if (!incomeDate || !incomeDescription || !incomeCategory || isNaN(incomeAmount) || incomeAmount <= 0) {
        incomebtnerror.textContent = "Please fill in all fields";
    } else {
        incomebtnerror.textContent = "";
        $.ajax({
            type: 'POST',
            url: '/add_income',
            data: $('#income-form').serialize(),
            success: function(response) {
                console.log(response);
                $('#income-form')[0].reset();
            },
            error: function(error) {
                console.error(error);
            }
        });
    }
});
*/