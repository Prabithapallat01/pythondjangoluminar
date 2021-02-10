class Employee:
    def __init__(self,eid,ename,desig,exp,salary):
        self.eid=eid
        self.ename = ename
        self.desig = desig
        self.exp= exp
        self.salary= salary
    def print_emp(self):
        print(self.eid,self.ename ,self.desig,self.exp,self.salary)
    def __str__(self):
        self.ename
f=open("employee.txt","r")
