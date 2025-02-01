from tkinter import *
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


root = Tk()

def withdraw():
    dep_label.pack_forget()
    dep_ent.pack_forget()
    wth_label.pack()
    wth_ent.pack()
def deposit():
    wth_label.pack_forget()
    wth_ent.pack_forget()
    dep_label.pack()
    dep_ent.pack()
def viewbalance():
    balance.pack()
    
root.title("BANKING APP")

root.geometry("600x600")
hd = Label(text= "Banks of Kazakhistan", font="Roboto 18 bold").pack(pady=15)

wth_btn = Button(text="Withdraw", command=withdraw).pack(pady=5)
wth_label = Label(text="Enter Withdraw amount: ")
wth_ent = Entry()
wth_sub = Button(text="Submit")

dep_btn = Button(text="Deposit", command=deposit).pack(pady=5)
dep_label = Label(text="Enter Deposit amount: ")
dep_ent = Entry()
dep_sub = Button(text="Submit")

viewbtn = Button(text="View Balance", command=viewbalance).pack(pady=5)
balance = Label(text= "₹")



root.mainloop()

# acc1 = Account(0, 1001)
# while True:
#     choice = int(input("Enter your choice: Withdraw(1)   Deposit(2)     View Balance(3)      Exit(4)\n"))
#     match(choice):
#         case 1:
#             acc1.debit(int(input("Enter amount to withdraw: ₹")))
#             print("Done!\nTotal Updated Balance: ₹",acc1.balance)
#         case 2:
#             acc1.credit(int(input("Enter amount to be deposited: ₹")))
#             print("Done!\nTotal Updated Balance: ₹",acc1.balance)
#         case 3:
#             acc1.getbal()

#         case 4:
#             break