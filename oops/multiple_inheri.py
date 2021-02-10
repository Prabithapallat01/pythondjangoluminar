class Parent:
    def m1(self):
        print("inside parent ")

class Child:
    def m1(self):
        print("inside child")
class Sub_child(Parent,Child):
    def m3(self):
        print("inside")
obj=Sub_child()
obj.m3()
obj.m1()
