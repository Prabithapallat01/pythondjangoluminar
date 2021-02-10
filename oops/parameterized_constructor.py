class Sample:
    a=0
    b=0
    #c=0
    def __init__(self,a,b):
        self.first_number=a
        self.second_number=b
    def calculate(self):
       self.c=((self.first_number)+(self.second_number))
    def display(self):
        print("first number ="+str(self.first_number))
        print("second number="+str(self.second_number))
        print("Addition of two numbers ="+str(self.c))
obj=Sample(2000,3444)
obj.calculate()
obj.display()