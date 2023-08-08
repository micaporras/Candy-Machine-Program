class CandyMachine:
    pass

class CashRegister:
    def __init__(self, cashOnHand=500):
        self.cashOnHand = cashOnHand
        self.cashOnRegister = 0
        self.AmountIn = 0
    
    def CashRegister(self, cashIn):
        cashIn = int(cashIn)
        if self.cashOnHand <= 0:
            self.cashOnHand = 500
        self.cashOnHand = cashIn + int(self.cashOnHand)
        return self.cashOnHand
    
    def acceptAmount(self, AmountIn):
        AmountIn = int(AmountIn)
        self.cashOnRegister = AmountIn + int(self.cashOnHand)
        self.AmountIn = AmountIn
        return self.AmountIn


    def currentBalance(self):
        return self.cashOnRegister

class Dispenser:
    def __init__(self, numberOfItems=50, cost=50):
        self.numberOfItems = numberOfItems
        self.cost = cost
    
    def Dispenser(self, setNoOfItems, setCost):
        setNoOfItems = int(setNoOfItems)
        setCost = int(setCost)
        if setNoOfItems < 0:
            setNoOfItems = 50
        if setCost <= 0:
            setCost = 50
        self.numberOfItems = setNoOfItems
        self.cost = setCost

    def getCount(self):
        return self.numberOfItems
    
    def getProductCost(self):
        return self.cost
    
    def makeSale(self):
        self.numberOfItems = self.numberOfItems - 1