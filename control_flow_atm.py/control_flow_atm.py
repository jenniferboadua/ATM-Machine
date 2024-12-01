# ATM Machine Program

# Initial setup
balance = 5000  # Initial balance
pin = 1234  # Default PIN
attempts = 3  # Number of PIN attempts allowed
total_deposits = 0  # Track total deposits
total_withdrawals = 0  # Track total withdrawals

# User authentication
while attempts > 0:
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        break
    else:
        attempts -= 1
        print("Incorrect PIN. Attempts remaining:", attempts)

if attempts == 0:
    print("Too many incorrect attempts. Access blocked.")
    exit()

# Main menu
while True:
    print("\n1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option: ")

    # Option 1: Check balance
    if choice == "1":
        print("Your balance is:", balance)

    # Option 2: Deposit funds
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            total_deposits += amount
            print("Deposit successful. New balance:", balance)
        else:
            print("Invalid amount. Please enter a positive number.")

    # Option 3: Withdraw funds
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            total_withdrawals += amount
            print("Withdrawal successful. New balance:", balance)
        elif amount > balance:
            print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive number.")

    # Option 4: Change PIN
    elif choice == "4":
        current_pin = int(input("Enter current PIN: "))
        if current_pin == pin:
            new_pin = int(input("Enter new 4-digit PIN: "))
            confirm_pin = int(input("Confirm new PIN: "))
            if new_pin == confirm_pin and 1000 <= new_pin <= 9999:
                pin = new_pin
                print("PIN changed successfully.")
            else:
                print("PINs did not match or invalid PIN format.")
        else:
            print("Incorrect current PIN.")

    # Option 5: Exit
    elif choice == "5":
        print("\nSummary of this session:")
        print("Total deposits made:", total_deposits)
        print("Total withdrawals made:", total_withdrawals)
        print("Thank you for using the ATM. Have a great day!")
        break

    # Invalid choice handling
    else:
        print("Invalid choice. Please try again.")