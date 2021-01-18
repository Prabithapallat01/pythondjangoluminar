lst=[3,45,1,2,47,23]
lst.sort()
low=0
flag=0
upp=len(lst)-1
element=int(input("Enter elemet for search:"))
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
            upp=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if flag==0:
    print("Elmnt not found")
else:
    print("elnmt found")