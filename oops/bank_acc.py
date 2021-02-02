from datetime import datetime
class Bank:
    def create_acc(self,accno,pname,min_blnce,bankname):
        self.account_number=accno
        self.person_name = pname
        self.balnce = min_blnce
        self.bank_name = bankname
    def Deposite(self,amount):
        self.balnce+=amount
        print("Your account",self.account_number,"has been creadited with amount",amount,"on",datetime.today(),"available balance",self.balnce)
    def withdrawal(self,amount):
        if self.balnce>amount:
            self.balnce-=amount
            print("Your account", self.account_number, "has been debited with amount", amount,"on", datetime.today(),
                  "available balance",self.balnce)
        else:
            print("Transaction with error code")
    def BalanceEnq(self):
        print(self.balnce)
obj=Bank()
obj.create_acc(1203948,"Devis",20000,"SBI")
obj.Deposite(20000)
obj.withdrawal(1000)
obj.BalanceEnq()

