# Candy Machine in GUI

from tkinter import *
import tkinter.messagebox as mb
from CandyMachine import Dispenser
from CandyMachine import CashRegister


root = Tk()
root.title("Candy Machine")
root.geometry('700x550')

Label(root, text="WELCOME TO MICA'S CANDY MACHINE", font=("Verdana", 15, "bold"), bg='pink3', fg='black').pack(side=TOP, fill=X)

main_frame = Frame(root, bg='pink')
main_frame.place(relx=0, relheight=1, y=30, relwidth=1)
Label(main_frame, text='What would you like to do?', font=("Verdana", 12), bg='pink', fg='black').place(relx=0.33, rely=0.1)

numCandy = 0
numChip = 0
numGum = 0
numCookie = 0
cash_register = 0
customer_money = IntVar()

def buyCandy():
    global candy
    candy = Toplevel()
    candy.title("Buy a Candy")
    candy.geometry('700x400')

    candy_frame = Frame(candy, bg='pink')
    candy_frame.place(relx=0, relheight=1, y=0, relwidth=1)
    Label(candy_frame, text='To buy a Candy, please insert 30 cents:', font=("Verdana", 12), bg='pink', fg='black').place(relx=0.1, rely=0.1)

    Button(candy_frame, text='Proceed', font=("Verdana", 12), width=10, command=getCandy).place(relx=0.1, rely=0.4)
    Button(candy_frame, text='Cancel', font=("Verdana", 12), width=10, command=candy.destroy).place(relx=0.1, rely=0.5)

    candy_entry = Entry(candy_frame, width=45, font=("Verdana", 15), textvariable=customer_money)
    candy_entry.place(relx=0.1, rely=0.2)
    reset()

def getCandy():
    global cash_register, candy, numCandy
    Product = Dispenser()
    Cost = CashRegister(cash_register)
    specific_number = numCandy
    specific_cost = 30
    Product.Dispenser(specific_number, specific_cost)
    numberOfProduct = Product.getCount()
    costOfProduct = Product.getProductCost()
    

    if numberOfProduct == 0:
        mb.showinfo('Oops!', 'This product is sold out')
        Product.makeSale()
        numberOfProduct = Product.getCount()
        numCandy = numberOfProduct
        cash_register = Cost.CashRegister(0)
        cash_register = Cost.acceptAmount(cash_register)
        candy.destroy()
    else:
        money = customer_money.get()
        amount = money
        if money < costOfProduct:
            mb.showinfo('Insufficient Money', 'Please insert sufficient money')
            candy.destroy()
            buyCandy()
        else:
            amount = Cost.acceptAmount(amount)
            currentBal = Cost.currentBalance()
            Product.makeSale()
            numberOfProduct = Product.getCount()
            cashIn = Cost.CashRegister(specific_cost)
            change = amount - specific_cost
            mb.showinfo('Balance', f'The current balance is {currentBal} cents')
            mb.showinfo('Sold!', f'The candy machine now have {numberOfProduct} candiies left\nYour change is {change} cents\nThank You and Enjoy Eating!')

            numCandy = numberOfProduct
            cash_register = cashIn
            candy.destroy()

def buyChips():
    global chips
    chips = Toplevel()
    chips.title("Buy a Chip")
    chips.geometry('700x400')

    chips_frame = Frame(chips, bg='pink')
    chips_frame.place(relx=0, relheight=1, y=0, relwidth=1)
    Label(chips_frame, text='To buy a Chip, please insert 85 cents:', font=("Verdana", 12), bg='pink', fg='black').place(relx=0.1, rely=0.1)

    Button(chips_frame, text='Proceed', font=("Verdana", 12), width=10, command=getChips).place(relx=0.1, rely=0.4)
    Button(chips_frame, text='Cancel', font=("Verdana", 12), width=10, command=chips.destroy).place(relx=0.1, rely=0.5)

    chips_entry = Entry(chips_frame, width=45, font=("Verdana", 15), textvariable=customer_money)
    chips_entry.place(relx=0.1, rely=0.2)
    reset()

def getChips():
    global cash_register, chips, numChip
    Product = Dispenser()
    Cost = CashRegister(cash_register)
    specific_number = numChip
    specific_cost = 85
    Product.Dispenser(specific_number, specific_cost)
    numberOfProduct = Product.getCount()
    costOfProduct = Product.getProductCost()
    

    if numberOfProduct == 0:
        mb.showinfo('Oops!', 'This product is sold out')
        Product.makeSale()
        numberOfProduct = Product.getCount()
        numChip = numberOfProduct
        cash_register = Cost.CashRegister(0)
        cash_register = Cost.acceptAmount(cash_register)
        chips.destroy()
    else:
        money = customer_money.get()
        amount = money
        if money < costOfProduct:
            mb.showinfo('Insufficient Money', 'Please insert sufficient money')
            chips.destroy()
            buyChips()
        else:
            amount = Cost.acceptAmount(amount)
            currentBal = Cost.currentBalance()
            Product.makeSale()
            numberOfProduct = Product.getCount()
            cashIn = Cost.CashRegister(specific_cost)
            change = amount - specific_cost
            mb.showinfo('Balance', f'The current balance is {currentBal} cents')
            mb.showinfo('Sold', f'The candy machine now have {numberOfProduct} chips left\nYour change is {change} cents\nThank You and Enjoy Eating!')

            numChip = numberOfProduct
            cash_register = cashIn
            chips.destroy()

def buyGum():
    global gum
    gum = Toplevel()
    gum.title("Buy a Gum")
    gum.geometry('700x400')

    gum_frame = Frame(gum, bg='pink')
    gum_frame.place(relx=0, relheight=1, y=0, relwidth=1)
    Label(gum_frame, text='To buy a Gum, please insert 40 cents:', font=("Verdana", 12), bg='pink', fg='black').place(relx=0.1, rely=0.1)

    Button(gum_frame, text='Proceed', font=("Verdana", 12), width=10, command=getGum).place(relx=0.1, rely=0.4)
    Button(gum_frame, text='Cancel', font=("Verdana", 12), width=10, command=gum.destroy).place(relx=0.1, rely=0.5)

    gum_entry = Entry(gum_frame, width=45, font=("Verdana", 15), textvariable=customer_money)
    gum_entry.place(relx=0.1, rely=0.2)
    reset()

def getGum():
    global cash_register, gum, numGum
    Product = Dispenser()
    Cost = CashRegister(cash_register)
    specific_number = numGum
    specific_cost = 40
    Product.Dispenser(specific_number, specific_cost)
    numberOfProduct = Product.getCount()
    costOfProduct = Product.getProductCost()
    

    if numberOfProduct == 0:
        mb.showinfo('Oops!', 'This product is sold out')
        Product.makeSale()
        numberOfProduct = Product.getCount()
        numGum = numberOfProduct
        cash_register = Cost.CashRegister(0)
        cash_register = Cost.acceptAmount(cash_register)
        gum.destroy()
    else:
        money = customer_money.get()
        amount = money
        if money < costOfProduct:
            mb.showinfo('Insufficient Money', 'Please insert sufficient money')
            gum.destroy()
            buyGum()
        else:
            amount = Cost.acceptAmount(amount)
            currentBal = Cost.currentBalance()
            Product.makeSale()
            numberOfProduct = Product.getCount()
            cashIn = Cost.CashRegister(specific_cost)
            change = amount - specific_cost
            mb.showinfo('Balance', f'The current balance is {currentBal} cents')
            mb.showinfo('Sold!', f'The candy machine now have {numberOfProduct} gums left\nYour change is {change} cents\nThank You and Enjoy Eating!')

            numGum = numberOfProduct
            cash_register = cashIn
            gum.destroy()

def buyCookie():
    global cookie
    cookie = Toplevel()
    cookie.title("Buy a Cookie")
    cookie.geometry('700x400')

    cookie_frame = Frame(cookie, bg='pink')
    cookie_frame.place(relx=0, relheight=1, y=0, relwidth=1)
    Label(cookie_frame, text='To buy a Cookie, please insert 100 cents:', font=("Verdana", 12), bg='pink', fg='black').place(relx=0.1, rely=0.1)

    Button(cookie_frame, text='Proceed', font=("Verdana", 12), width=10, command=getCookie).place(relx=0.1, rely=0.4)
    Button(cookie_frame, text='Cancel', font=("Verdana", 12), width=10, command=cookie.destroy).place(relx=0.1, rely=0.5)

    cookie_entry = Entry(cookie_frame, width=45, font=("Verdana", 15), textvariable=customer_money)
    cookie_entry.place(relx=0.1, rely=0.2)
    reset()

def getCookie():
    global cash_register, cookie, numCookie
    Product = Dispenser()
    Cost = CashRegister(cash_register)
    specific_number = numCookie
    specific_cost = 100
    Product.Dispenser(specific_number, specific_cost)
    numberOfProduct = Product.getCount()
    costOfProduct = Product.getProductCost()
    

    if numberOfProduct == 0:
        mb.showinfo('Oops!', 'This product is sold out')
        Product.makeSale()
        numberOfProduct = Product.getCount()
        numCookie = numberOfProduct
        cash_register = Cost.CashRegister(0)
        cash_register = Cost.acceptAmount(cash_register)
        cookie.destroy()
    else:
        money = customer_money.get()
        amount = money
        if money < costOfProduct:
            mb.showinfo('Insufficient Money', 'Please insert sufficient money')
            cookie.destroy()
            buyCookie()
        else:
            amount = Cost.acceptAmount(amount)
            currentBal = Cost.currentBalance()
            Product.makeSale()
            numberOfProduct = Product.getCount()
            cashIn = Cost.CashRegister(specific_cost)
            change = amount - specific_cost
            mb.showinfo('Balance', f'The current balance is {currentBal} cents')
            mb.showinfo('Sold!', f'The candy machine now have {numberOfProduct} cookies left\nYour change is {change} cents\nThank You and Enjoy Eating!')

            numCookie = numberOfProduct
            cash_register = cashIn
            cookie.destroy()

def viewBalance():
    global cash_register
    if cash_register == 0:
        Cost = CashRegister()
        cash_register = Cost.CashRegister(0)
    mb.showinfo('Cash Register', f'The cash register have a balance of {cash_register} cents')

def reset():
    customer_money.set('')

def exit():
    root.destroy()

Button(main_frame, text='Buy a Candy', font=("Verdana", 12), width=30, command=buyCandy).place(relx=0.28, rely=0.2)
Button(main_frame, text='Buy a Chip', font=("Verdana", 12), width=30, command=buyChips).place(relx=0.28, rely=0.3)
Button(main_frame, text='Buy a Gum', font=("Verdana", 12), width=30, command=buyGum).place(relx=0.28, rely=0.4)
Button(main_frame, text='Buy a Cookie', font=("Verdana", 12), width=30, command=buyCookie).place(relx=0.28, rely=0.5)
Button(main_frame, text='View Balance', font=("Verdana", 12), width=30, command=viewBalance).place(relx=0.28, rely=0.6)
Button(main_frame, text='Exit', font=("Verdana", 12), width=30, command=exit).place(relx=0.28, rely=0.7)

root.update()

root.mainloop()