# to print even numbers from lower limit to upper limit:

lolimit=int(input("Enter the lower limit:"))
uplimit=int(input("enter the upper limit:"))
#i=lolimit
while(lolimit<=uplimit):
    if(lolimit%2==0):
        print(lolimit)
    lolimit+=1