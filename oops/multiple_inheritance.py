class Father:
    fathername=""
    def father(self):
        print(self.fathername)
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
class child(Father,Mother):
    def name(self):
        print("father:",self.fathername)
        print("mother:",self.mothername)
obj=child()
obj.Father("Sivadasan")
obj.Mother("Prameela")
