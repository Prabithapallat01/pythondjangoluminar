class Compute:
    def area(self,x=None,y=None):
        if x!=None and y!=None:
            return x*y
        elif(x!=None):
            return x*x
        else:
            return 0
obj=Compute()
print("Area value=",obj.area())
print("Area value=",obj.area(12))
print("Area value=",obj.area(24,24))