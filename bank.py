from tkinter import *
from tkinter import messagebox

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

acc1 = Account(1000, 1001)

root = Tk()

def withdraw():
    dep_label.pack_forget()
    dep_ent.pack_forget()
    balance.pack_forget()
    dep_sub.pack_forget()

    wth_label.pack()
    wth_ent.pack()
    wth_sub.pack()

def deposit():
    wth_label.pack_forget()
    wth_ent.pack_forget()
    balance.pack_forget()
    wth_sub.pack_forget()

    dep_label.pack()
    dep_ent.pack()
    dep_sub.pack()

def viewbalance():
    dep_label.pack_forget()
    dep_ent.pack_forget()
    wth_label.pack_forget()
    wth_ent.pack_forget()
    wth_sub.pack_forget()
    dep_sub.pack_forget()

    balance.pack()

def wthsubmit():
    w = withdrawmoney.get()
    if w>acc1.balance:
        messagebox.showerror("Poor Ass", message="Insufficient Funds")
    else:
        acc1.debit(w)
        messagebox.showinfo("Done", message="₹"+str(w)+" Withdrawn")
        balance.config(text="Total Balance = ₹" + str(acc1.balance))
def depsubmit():
    d = depositmoney.get()  
    acc1.credit(d)
    messagebox.showinfo("Done", message="₹"+str(d)+" Deposited")
    balance.config(text="Total Balance = ₹" + str(acc1.balance))

root.title("BANKING APP")

root.geometry("600x600")
hd = Label(text= ("Banks of Kazakhistan").upper(), font="Roboto 18 bold").pack(pady=15)

depositmoney = IntVar()
withdrawmoney = IntVar()

wth_btn = Button(text="Withdraw", command=withdraw).pack(pady=5)
wth_label = Label(text="Enter Withdraw amount: ")
wth_ent = Entry(textvariable=withdrawmoney)
wth_sub = Button(text="Submit", command=wthsubmit)

dep_btn = Button(text="Deposit", command=deposit).pack(pady=5)
dep_label = Label(text="Enter Deposit amount: ")
dep_ent = Entry(textvariable=depositmoney)
dep_sub = Button(text="Submit", command=depsubmit)

viewbtn = Button(text="View Balance", command=viewbalance).pack(pady=5)
balance = Label(text= "Total Balance = ₹"+str(acc1.balance), font="Roboto 14 bold")



root.mainloop()
