class BankAccount:
    def __init__(self, account_no, balance=0.0):
        self.account_no = account_no
        self.balance = balance
    def deposit(self,amount):
        if amount >= 0:
            print(f"depositedrs{amount}.new balance:rs{self.balance}")
        else:
            print("deposit amount must be positive")
    
    def withdrawl(self,amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"withdrawn rs{amount}. remaining balance: rs{self.balance}")
            else:
                print("insufficient balance")
        else: 
               print("withdrawl amount must be positive.")

    def check_balance(self):
        print(f"account number: {self.account_no}")
        print(f"current balance: {self.balance}")

#user_input
account_no = input("Enter Account Number:")
initial_balance = float(input("Enter Initial Balance:"))

account = BankAccount(account_no, initial_balance)

while True:
    print("/n1. Deposit")
    ()

