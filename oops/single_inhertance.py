# Create Parent class:
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def display(self):
        #print(str(self.fname)+str(self.lname))
        print(self.fname, self.lname)

# Create Child class:
class Child(Person):
    pass
obj=Child("Prabitha","Pallat")
obj.display()