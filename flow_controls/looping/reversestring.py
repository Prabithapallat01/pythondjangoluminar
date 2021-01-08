
name=input("Enter the name:")
length=len(name)-1
reverse=" "
while(length>0):
    reverse+=name[length]
    length-=1
print(reverse)
