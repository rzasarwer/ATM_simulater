import time
print("please insert your card")
time.sleep(5)
pin = 1234
balance = 10000.0
transaction_history = []

while True:
    print("......WELCOME.......")

    try:
        choice = int(input("Enter your choice: \n 1. Account Balance Inquiry \n 2. Cash Withdrawal \n 3. Cash Deposit \n 4. PIN Change \n 5. Transaction History \n 6. Exit:..."))

        if choice == 1:
            try:
                input_pin = int(input("Enter your PIN: "))
                if input_pin == pin:
                    print(f"Your current balance is: {balance}")
                    transaction_history.append("Checked balance")
                else:
                    print("Incorrect PIN!")
            except ValueError:
                print("Invalid input! Please enter a numeric PIN.")

        elif choice == 2:
            try:
                input_pin = int(input("Enter your PIN: "))
                if input_pin == pin:
                    try:
                        amount = float(input("Enter the amount to withdraw: "))
                        if amount > balance:
                            print("Insufficient funds!")
                        else:
                            balance -= amount
                            print(f"You have withdrawn {amount}. Your new balance is: {balance}")
                            transaction_history.append(f"Withdrew {amount}")
                    except ValueError:
                        print("Invalid input! Please enter a numeric amount.")
                else:
                    print("Incorrect PIN!")
            except ValueError:
                print("Invalid input! Please enter a numeric PIN.")

        elif choice == 3:
            try:
                input_pin = int(input("Enter your PIN: "))
                if input_pin == pin:
                    try:
                        amount = float(input("Enter the amount to deposit: "))
                        balance += amount
                        print(f"You have deposited {amount}. Your new balance is: {balance}")
                        transaction_history.append(f"Deposited {amount}")
                    except ValueError:
                        print("Invalid input! Please enter a numeric amount.")
                else:
                    print("Incorrect PIN!")
            except ValueError:
                print("Invalid input! Please enter a numeric PIN.")

        elif choice == 4:
            try:
                old_pin = int(input("Enter your old PIN: "))
                if old_pin == pin:
                    try:
                        new_pin = int(input("Enter your new PIN: "))
                        pin = new_pin
                        print("Your PIN has been changed successfully.")
                        transaction_history.append("Changed PIN")
                    except ValueError:
                        print("Invalid input! Please enter a numeric PIN.")
                else:
                    print("Incorrect old PIN!")
            except ValueError:
                print("Invalid input! Please enter a numeric PIN.")

        elif choice == 5:
            try:
                input_pin = int(input("Enter your PIN: "))
                if input_pin == pin:
                    if not transaction_history:
                        print("No transactions yet.")
                    else:
                        print("Transaction history:")
                        for transaction in transaction_history:
                            print(transaction)
                else:
                    print("Incorrect PIN!")
            except ValueError:
                print("Invalid input! Please enter a numeric PIN.")

        elif choice == 6:
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

    except ValueError:
        print("Invalid input! Please enter a numeric choice.")
