class Bank:
    def balance_enq(self):
        print("inside blnace")
    def withdral(self):
        print("inside blnace2")
    def __deposite(self):
        print("inside blnace3")
class Atm(Bank):
    print("pass")
atm=Atm()
atm.balance_enq()
atm.withdral()
atm._Bank__deposite()