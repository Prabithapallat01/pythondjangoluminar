lst=[3,45,1,2,47,23]                  #[3,45,1,2,47,23]
lst.sort()                             #[1,2,3,23,45,47]
low=0                                  #low=0
flag=0                                 #flag=0
upp=len(lst)-1                         #upp=6-1=5
element=int(input("Enter elemet for search:"))   #47
while(low<=upp):                              #(0<5)
    mid=(low+upp)//2                          #mid=5//2=
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