lowlimit=5
uplimit=50

for num in range(5,50+1):
    if(num>1):                       #5>1
        for i in range(2,num):       #2,5
            if(num%i==0):            #5%2==0

                break
            else:
                print(num,end=" ")
                break