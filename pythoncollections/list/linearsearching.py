list=int(input("enter the elements:"))
elment=int(input("Enter element you want to search:"))
length=len(list)
flag=0
cnt=0
for i in range(0,length-1):
    if(elment==list[i]):
        flag+=1
        break
    else:
         pass
         cnt+1
if flag==0:
    print("elmnt not found")
else:
    print("elmnt not found")
