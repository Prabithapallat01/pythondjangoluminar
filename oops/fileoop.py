#print employee details whose designation developer
#highest salary in developer

class Employee:
    def __init__(self,eid,ename,desig,exp,sal):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.exp=exp
        self.sal=sal
    def __str__(self):
            return self.ename
f=open("employee.txt","r")
emplst=[]
sallst=[]

for lines in f:
    eid,ename,desig,exp,sal=lines.rstrip("\n").split(",")
    emplst.append(Employee(eid,ename,desig,exp,sal))

for employee in emplst:
    sallst.append(employee.sal)
minimum=min(sallst)
for employee in emplst:
    if (desig=="Developer") and (sal==minimum):
        print(employee)
