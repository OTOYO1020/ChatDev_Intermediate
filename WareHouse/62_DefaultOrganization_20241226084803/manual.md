# BudgetPlanner User Manual

## Introduction

BudgetPlanner is a software application designed to help individuals manage their personal finances effectively. It provides a user-friendly interface and various features to assist users in budgeting, tracking expenses, and achieving their financial goals.

## Main Functions

1. **Hello World**: The application provides a simple "Hello, World!" message to ensure that the server is running properly.

2. **Welcome Message**: Users are greeted with a welcome message upon accessing the application.

3. **Deposit to Budget**: Users can deposit a specified amount to a budget by providing the budget ID and the deposit amount.

4. **Withdraw from Budget**: Users can withdraw a specified amount from a budget by providing the budget ID and the withdrawal amount.

## Installation

To install and run BudgetPlanner, follow these steps:

1. Ensure that you have Java Development Kit (JDK) installed on your system.

2. Download the BudgetPlanner source code from the provided repository.

3. Open a terminal or command prompt and navigate to the directory containing the downloaded source code.

4. Compile the Java files by running the following command:

   ```
   javac *.java
   ```

5. Run the application by executing the following command:

   ```
   java MainApplication
   ```

6. The application will start running on a local server. You can access it by opening a web browser and entering the following URL:

   ```
   http://localhost:8080/app
   ```

## Usage

Once you have the BudgetPlanner application running, you can use the following endpoints to interact with it:

1. **Hello World**: Access the "Hello, World!" message by visiting the following URL:

   ```
   http://localhost:8080/app/hello
   ```

2. **Welcome Message**: Access the welcome message by visiting the following URL:

   ```
   http://localhost:8080/app/message
   ```

3. **Deposit to Budget**: Deposit a specified amount to a budget by sending a POST request to the following URL:

   ```
   http://localhost:8080/app/budget/deposit
   ```

   Parameters:
   - budgetId: The ID of the budget to deposit to.
   - amount: The amount to deposit.

4. **Withdraw from Budget**: Withdraw a specified amount from a budget by sending a POST request to the following URL:

   ```
   http://localhost:8080/app/budget/withdraw
   ```

   Parameters:
   - budgetId: The ID of the budget to withdraw from.
   - amount: The amount to withdraw.

## Conclusion

BudgetPlanner is a powerful tool for managing personal finances. With its user-friendly interface and essential features, users can effectively budget, track expenses, and achieve their financial goals. Follow the installation and usage instructions provided in this manual to get started with BudgetPlanner.