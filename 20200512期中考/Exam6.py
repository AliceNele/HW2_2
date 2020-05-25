class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def getBalance(self):
        return self.balance
    

class FundAccount(BankAccount):
    def __init__(self,name):
        
        BankAccount.__init__(self,name)
        self.amount = 0
        
        
        
    def buy(self, NAV, amount):       
        if self.balance - NAV*amount <0:
            print("餘額不足")
        else:
            self.balance = self.balance - NAV*amount
            self.amount = self.amount + amount
            
        
    
    def sell(self, NAV, amount):
        if self.amount < amount :
            print("持有單位數不足")
        else:
            self.balance = self.balance +  NAV*amount
            self.amount = self.amount - amount
        
        
    
    def getFundBalance(self, NAV):
        return NAV*self.amount

    

Tim = FundAccount("Tim")
Tim.deposit(1000) # 存入1000元
Tim.buy(10, 50) # 買進 50 單位, 每單位 10元
Tim.sell(100, 10) # 賣出 10 單位, 每單位 100元
Tim.withdraw(200) # 提款 200元
print("Bank Account: %.2f; Fund Account: %.2f" % (Tim.getBalance(), Tim.getFundBalance(80)))

