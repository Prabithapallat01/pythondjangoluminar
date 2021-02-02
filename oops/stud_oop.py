class Students:
    def set_Students(self,name,Course,rol):
        self.name=name
        self.course=Course
        self.rol=rol
    def print_Students(self):
        # print("name=",self.name)
        # print("Course=",self.course)
        # print("age=",self.age)
        print(self.name,",",self.course,",",self.rol)
obj=Students()
obj.set_Students("Aleena","MCA",27)
obj.print_Students()

obj1=Students()
obj1.set_Students("Maya","MCA",20)
obj1.print_Students()
