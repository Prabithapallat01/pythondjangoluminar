class Person:
    def hello(self,name=None):
        if name is not  None:
            print("hello" + str(name))
        else:
            print("hello")

obj=Person()
obj.hello("Ram")
obj.hello()

