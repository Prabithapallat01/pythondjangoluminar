lst=[1,2,3,5]
low=0
upp=len(lst)-1
elmnt=int(input("Enter elments:"))
while(low<upp):
    tot=lst(low)+lst(upp)
    if(elmnt==tot):
        print(lst(low),lst(upp))
        break
    elif(elmnt>tot):
        low+=1
    else:
        upp-=1