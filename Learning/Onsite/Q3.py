"""
Practice Question: Bank Account Class Design
Scenario: You are asked to design a simple bank account system using Object-Oriented Programming principles.

Requirements:
BankAccount Class:

Attributes:
account_number (String): A unique identifier for the account.
account_holder_name (String): The name of the account holder.
balance (Float): The current balance in the account.
Methods:

deposit(amount: float): Deposits a certain amount into the account. If the amount is negative, raise an exception with a relevant error message.
withdraw(amount: float): Withdraws a certain amount from the account. If the withdrawal exceeds the current balance, raise an exception.
get_balance(): Returns the current balance of the account.
transfer_to(account: BankAccount, amount: float): Transfers a certain amount from this account to another BankAccount. If the amount exceeds the balance, raise an exception.
Additional Requirements:

Include exception handling where applicable.
Implement a class method create_account() to initialize a new BankAccount object.

Bonus: Implement an Account subclass called SavingAccount that inherits from BankAccount, with an additional feature:

An interest rate (interest_rate).
A method to calculate and add interest to the balance, based on the current balance.
"""

class BankAccount:

    def __init__(self, account_number: str, account_holder_name: str, balance: float):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance


    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError('amount to be deposit cannot be negative')

        self.account_number += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError('amount %f is more than available balance', amount)

        self.balance -= amount