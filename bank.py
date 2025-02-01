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

acc1 = Account(0, 1001)

root = Tk()

def withdraw():
    dep_label.pack_forget()
    dep_ent.pack_forget()
    balance.pack_forget()
    dep_sub.pack_forget()

    wth_label.pack(pady=5)
    wth_ent.pack(pady=5)
    wth_sub.pack(pady=5)

def deposit():
    wth_label.pack_forget()
    wth_ent.pack_forget()
    balance.pack_forget()
    wth_sub.pack_forget()

    dep_label.pack(pady=5)
    dep_ent.pack(pady=5)
    dep_sub.pack(pady=5)

def viewbalance():
    dep_label.pack_forget()
    dep_ent.pack_forget()
    wth_label.pack_forget()
    wth_ent.pack_forget()
    wth_sub.pack_forget()
    dep_sub.pack_forget()

    balance.pack(pady=5)

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

root.geometry("600x300")
root.resizable(FALSE,FALSE)
root.config(bg="#949F77")
hd = Label(text= ("Banks of Kazakhistan").upper(), bg="#949F77",fg="#1E2F2B", font="Unispace_Bold 18 bold underline").pack(pady=15)

depositmoney = IntVar()
withdrawmoney = IntVar()

wth_btn = Button(text="Withdraw",bg="#f4fdaf",fg= "#756B42",font="cooper 12", command=withdraw).pack(pady=5)
wth_label = Label(text="Enter Withdraw amount: ",font="terminal 10", bg="#949F77")
wth_ent = Entry(textvariable=withdrawmoney)
wth_sub = Button(text="Submit",bg="#f4fdaf",fg= "#756B42",font="cooper 12", command=wthsubmit)
Event()

dep_btn = Button(text="Deposit",bg="#f4fdaf",fg= "#756B42",font="cooper 12", command=deposit).pack(pady=5)
dep_label = Label(text="Enter Deposit amount: ",font="terminal 10 ", bg="#949F77")
dep_ent = Entry(textvariable=depositmoney)
dep_sub = Button(text="Submit",bg="#f4fdaf",fg= "#756B42",font="cooper 12",command=depsubmit)

viewbtn = Button(text="View Balance",bg="#f4fdaf",fg= "#756B42",font="cooper 12", command=viewbalance).pack(pady=5)
balance = Label(text= "Total Balance = ₹"+str(acc1.balance), font="terminal 14 ", bg="#949F77")

wth_ent.bind("<Return>", lambda event: wthsubmit())
dep_ent.bind("<Return>", lambda event: depsubmit())



root.mainloop()
