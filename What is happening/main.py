#Gavin Pierce what is happening

class BankAccount:
    #Gives inistial amounts name and acount number
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
#name of user and mount added
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
# name of user and amount remove
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
#balance of acnount
    def get_balance(self):
        return self.balance
#creats acount with details pretaing to
def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)
#gives user options om what they want to do.
def main():
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        #has them chose what they will do.
        choice = input("Enter your choice (1-5): ")
        #what will happen if they chose option one
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
       #this will happen is uesr choose 2 3 4 
        elif choice in ['2', '3', '4']:
            #has them enter acount number
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                # if they chose 2 it will have them deposite a amount of money
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                        #happens if they input a invalid varible
                    else:
                        print("Invalid deposit amount.")
                        #happens if they chose option three
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        #will happen if they input a valid number
                        print(f"Withdrawn ${amount:.2f} successfully!")
                        #will happen if they give a invalide number or they atempt to take more then they have
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else: #give curent amount of money
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:#if anount is not there
                print("Account not found.")
        #closes program
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        #if a invalid number is used
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()