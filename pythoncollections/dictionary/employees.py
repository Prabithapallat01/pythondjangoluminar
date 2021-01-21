employees={"id":12,"ename":"latha","exp":2,"salary":30000}
if("salary" in employees):
    print("salary")

#name

if("ename"in employees):
    print("ename")

#add gender
if("gender" in employees):
    print("exist")
else:
    employees["gender"]="female"
print(employees)

#if any employees salary is <35000 and add500

if(employees["salary"]<=35000):
    employees["salary"]+=500
print(employees)