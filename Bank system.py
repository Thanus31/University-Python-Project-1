class BankAccount:
    def __init__(self, account_number, initial_balance = 0):
        # Constructor to initialize account number and balance
        self.account_number = account_number
        self.balance = initial_balance
        

    def deposite(self, amount):
        # Method to deposit money into the account
        if amount <= 0:
            print("Invalid amount. deposite amount must be positive.")
            return False
        else:
            self.balance += amount
            print(f"Deposited Rs.{amount} in to account {self.account_number}.")
            return True
    
    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount <= 0:
            print("Invalid amount.wthdrawal amount must be positive.")
            return False
        elif self.balance < amount:
            print("Insufficient balance.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrew Rs.{amount} from from account {self.account_number}")
            return True
    
    def check_balance(self):
        # Method to check the balance of the account
        print(f"Account {self.account_number} balance: Rs. {self.balance}")

    def transfer(self, target_account, amount):
        # Method to transfer money from one account to another
        if not isinstance(target_account, BankAccount):
            print("Invalid target account.")
            return False
        elif amount <= 0:
            print("Invalid amount. transfer amount must be positive.")
            return False
        elif self.balance < amount:
            print("Insufficiant balance.")
            return False
        else:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred Rs.{amount} from {self.account_number} to account {target_account.account_number}.")
            return True
    
def main():
    accounts = {}
    while True:
        print("\nWelcome to our bank management system.")
        print("\nPress 1 to Create new account")
        print("Press 2 to Deposite")
        print("Press 3 to Withdraw")
        print("Press 4 to Check Balance")
        print("Press 5 to Transfer")
        print("Press 6 to Exit")
        option = input("Enter your choice: ")

        if option == '1':
            # Create a new account
            account_number = input("Enter a account number (Use an account number of your choice): ")
            initial_deposite = float(input("Enter initial deposite amount: "))
            create_account(accounts, account_number, initial_deposite)

        elif option == '2':
            # Deposite money
            account_number = input("Enter your account number: ")
            amount = float(input("Enter your deposite balance: "))
            account = get_account(accounts, account_number)
            if account:
                account.deposite(amount)

        elif option == '3':
            # Withdraw money
            account_number = input("Enter your account number: ")
            amount = float(input("Enter your withdrawal amount: "))
            account = get_account(accounts, account_number)
            if account:
                account.withdraw(amount)

        elif option == '4':
            # Check balance
            account_number = input("Enter your account number: ")
            account = get_account(accounts, account_number)
            if account:
                account.check_balance()

        elif option == '5':
            # Transefer money
            from_account = input("Enter your account number: ")
            to_account = input("Enter recipient's account number: ")
            amount = float(input("Enter transfer amount: "))
            from_acc = get_account(accounts, from_account)
            to_acc = get_account(accounts, to_account)
            if from_acc and to_acc:
                from_acc.transfer(to_acc, amount)

        elif option == '6':
            # Exit
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

def create_account(accounts, account_number, initial_deposite):
    # Function to create a new account
    if account_number in accounts:
        print("This account already exists in our bank.")
        return None
    elif initial_deposite < 0:
        print("Invalid deposite.")
        return None
    else:
        account = BankAccount(account_number, initial_deposite)
        accounts[account_number] = account
        print(f"Account {account_number} created with initial balance Rs.{initial_deposite}.")
        return account

def get_account(accounts, account_number):
    # Function to get an account from the dictionary of accounts
    if account_number not in accounts:
        print("This account does not exist in our bank.")
        return None
    else:
        return accounts[account_number]


if __name__ == "__main__":
    main()