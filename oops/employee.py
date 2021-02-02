# class Employee:
#     def set_Employee(self,eid,ename,desig,salary):
#         self.eid=eid
#         self.ename=ename
#         self.desig=desig
#         self.salary=salary
#     def get_Employee(self):
#         print(self.eid,",",self.ename,",",self.desig,",",self.salary)
# obj=Employee()
# obj.set_Employee(1001,"Aravindh","wee",20000)
# obj.get_Employee()
class Employee:
    def __init__(self,eid,ename,salary):
        self.eid=eid
        self.ename=ename
        self.salary=salary
    def getEmployee(self):
        print(self.eid, ",", self.ename, ",", self.salary)
obj=Employee(1001,"Aravindh",2000)
obj.getEmployee()
