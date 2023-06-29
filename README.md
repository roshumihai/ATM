# ATM App
This repository contains the code for an ATM (Automated Teller Machine) application written in Python. The application allows users to create bank accounts, manage their balances, and perform transactions such as deposits and withdrawals.

# Prerequisites
Before running the ATM app, ensure that you have the following:

Python 3.x installed on your machine.
The json module, which is included in the Python standard library.
Getting Started
Follow the instructions below to run the ATM app:

Clone this repository to your local machine or download the code as a ZIP file.

Open a terminal or command prompt and navigate to the directory where you have cloned or extracted the repository.

Run the following command to execute the ATM app: python atm_app.py

# Features
The ATM app provides the following features:

Account Creation: Users can create a new bank account by entering their username and initial deposit amount.

Authentication: Users need to enter their PIN (Personal Identification Number) to access their accounts.

Balance Inquiry: Users can check their account balance.

Deposit: Users can add funds to their accounts.

Withdrawal: Users can withdraw funds from their accounts, provided they have sufficient balance.

PIN Management: Users can view or change their PIN.

# Usage
When prompted, enter your username. If the username doesn't exist, you will be given an option to create a new account.

If you choose to create a new account, you will need to provide a username, initial deposit amount, and set a PIN for your account.

Once you have logged in, you can select options from the menu by entering the corresponding numbers or keywords.

If you choose to perform a transaction (deposit or withdrawal), you will be prompted to enter the amount.

For PIN management, you can choose to view your PIN or change it by entering the old and new PINs.

To quit the ATM app, enter 'q' or 'quit' at any menu prompt.

# Data Persistence
Account information, including usernames, balances, and PINs, is stored in a JSON file named bank_account.json. This file is automatically created and updated as accounts are created or modified.

# Note
This ATM app is a simple implementation and should not be used for real-world banking operations. It serves as a demonstration of basic Python programming concepts.

Please exercise caution while entering your PIN or any sensitive information in this app.
