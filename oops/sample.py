class Stud:
    def __init__(self,name,rol,course,total):
        self.name=name
        self.rol=rol
        self.course=course
        self.total=total
    def __str__(self):
        return self.name

obj=Stud("pranhha",12,"bca",199)
obj1=Stud("maya",13,"mca",898)
obj2=Stud("Neha",14,"django",111)
obj3=Stud("Neena",11,"django",788)
lst=[]
lst.append(obj)
lst.append(obj1)
lst.append(obj2)
lst.append(obj3)
total=0
print(lst)
for stud in lst:
    if stud.course=="django":
        total+=stud.total
print(total)



