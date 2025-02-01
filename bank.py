class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def credit(self, money):
        self.balance += money

    def debit(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print("Insufficient Funds")

    def getbal(self):
        print("Total Balance: ₹",self.balance)

acc1 = Account(0, 1001)
while True:
    choice = int(input("Enter your choice: Withdraw(1)   Deposit(2)     View Balance(3)\n"))
    match(choice):
        case 1:
            acc1.debit(int(input("Enter amount to withdraw: ₹")))
            print("Done!\nTotal Updated Balance: ₹",acc1.balance)
        case 2:
            acc1.credit(int(input("Enter amount to be deposited: ₹")))
            print("Done!\nTotal Updated Balance: ₹",acc1.balance)
        case 3:
            acc1.getbal()