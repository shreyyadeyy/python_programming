class BankAccount:
    def __init__(self,account_no,balance=0.0):
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
account=BankAccount("sbi2007, 10000")
account.deposit(500)
account.withdrawl(200)

