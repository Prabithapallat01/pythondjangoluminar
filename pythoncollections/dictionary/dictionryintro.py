#value stored in dictionary we stored in key
#here key must be unique
expenses={"janu20":30000,"feb20":45000,"march20":90000,"apri20l":56000}

#check june20 in expenses
print("march20" in expenses)

#adding new value
#june20=29000
expenses["june20"]=29000
print(expenses)
expenses["march20"]-=500
print(expenses)


