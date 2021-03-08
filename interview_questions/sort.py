# without using  sort function


lst=[21,23,2,4,56,78,22,43]
new_lst=[]
while lst:
    minimum=lst[0]
    for i in lst:
        if i<minimum:
            minimum=i
    new_lst.append(minimum)
    lst.remove(minimum)

print(new_lst)