class Students:
    def getstudents(self):
        self.rol =(input("Rol     :"))
        self.name =(input("Name    :"))
        self.gender=(input("Gender  :"))
class Test(Students):
    def getmarks(self):
        self.studClass  = input("Class     :")
        print("Enter your marks:")
        self.biology=int(input("biology    :"))
        self.chemistry  = int(input("chemistry :"))
        self.maths      = int(input("maths :"))
        self.english    = int(input("english :"))

class Marks(Test):
    def display(self):

        print("\n\nname   :",self.name)
        print("class  :", self.studClass)
        print("rol    :",self.rol)
        print("gender :",self.gender)
        print("Total  =",self.biology+self.chemistry+self.maths+self.english)
m=Marks()
m.getstudents()
m.getmarks()
m.display()

