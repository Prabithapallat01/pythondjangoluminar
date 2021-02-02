f=open("students","r")
stud={}
for lines in f:
    id,name,total,course=lines.rstrip("\n").split(",")
    if id not in stud:
        stud[id]={"id":id,"name":name,"total":total,"course":course}
print(stud)
def print_students_data(**kwargs):
    id=kwargs["id"]
    if id in stud:
        print(stud[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(stud[id][prop])
    else:
        print("does not exist:")
print_students_data(id="1002",prop="course")
