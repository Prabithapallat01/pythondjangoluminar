class Person:
    def setPerson(self,name,age):
        self.name=name
        self.age=age
    def printPerson(self):
        print("name=",self.name)
        print("age=",self.age)
obj=Person()
obj.setPerson("annie",29)
obj.printPerson()


obj1=Person()
obj1.setPerson("maya",34)
obj1.printPerson()