# Candy Machine in COMMAND LINE INTERFACE

from CandyMachine import Dispenser
from CandyMachine import CashRegister

def showSelection():
    print("**** Welcome to Mica's Candy Shop ****")
    productList = ["candies", "chips", "gum", "cookies"]
    numCandy = 0
    numChip = 0
    numGum = 0
    numCookie = 0
    cash_register = 0

    while True:
        select = input("The Candy Machine sells the following products:\nA.Candies\nB.Chips\nC.Gum\n"
        "D.Cookies\n1.View Balance\n2.Exit\nWhat would you like to buy?:")
        if select == "A":
            cash, candy = sellProduct(numCandy, 30, productList[0], cash_register)
            numCandy = candy
            cash_register = cash
            print("-------------------------------------------------")
        if select == "B":
            cash, chip = sellProduct(numChip, 85, productList[1], cash_register)
            numChip = chip
            cash_register = cash
            print("-------------------------------------------------")
        if select == "C":
            cash, gum = sellProduct(numGum, 40, productList[2], cash_register)
            numGum = gum
            cash_register = cash
            print("-------------------------------------------------")
        if select == "D":
            cash, cookie = sellProduct(numCookie, 100, productList[3], cash_register)
            numCookie = cookie
            cash_register = cash
            print("-------------------------------------------------")
        if select == "1":
            if cash_register == 0:
                cash_register = 500
            print(f"The cash register's balance is {cash_register} cents")
            print("-------------------------------------------------")
        if select == "2":
            break
    print("Thank You! Come Again!")
    print("-------------------------------------------------")

def sellProduct(specific_number: int, specific_cost: int, product: str, cash_register: int):
    Product = Dispenser()
    Cost = CashRegister(cash_register)
    Product.Dispenser(specific_number, specific_cost)
    numberOfProduct = Product.getCount()
    costOfProduct = Product.getProductCost()
    product = product

    if numberOfProduct == 0:
        print("This product is sold out")
        Product.makeSale()
        numberOfProduct = Product.getCount()
        cash_register = Cost.CashRegister(0)
        cash_register = Cost.acceptAmount(cash_register)
        return cash_register, numberOfProduct
    else:
        print(f"We currently have {numberOfProduct} {product} in the machine and each cost {costOfProduct} cents")
        money = int(input("Insert money here: "))
        if money < costOfProduct:
            while money < costOfProduct:
                if money >= costOfProduct:
                    return money
                add = int(input("Insufficient Money\nPlease insert additional money:"))
                money = money + add
                amount = money
        else:
            amount = money
        amount = Cost.acceptAmount(amount)
        currentBal = Cost.currentBalance()
        print(f"The cash register's current balance is {currentBal}")
        Product.makeSale()
        numberOfProduct = Product.getCount()
        cashIn = Cost.CashRegister(specific_cost)
        change = amount - specific_cost
        print(f"Your change is {change} cents\nThank You and Enjoy Eating!")
        
        return cashIn, numberOfProduct
       
def Program():
    showSelection()

Program()