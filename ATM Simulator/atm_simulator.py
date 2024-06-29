class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"${amount:.2f} has been deposited. Your new balance is: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn. Your new balance is: ${self.balance:.2f}")

def atm_menu():
    atm = ATM(initial_balance=1000)  # Initial balance set to $1000 for demonstration

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            try:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == 3:
            try:
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    atm_menu()
