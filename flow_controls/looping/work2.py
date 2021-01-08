#1**2=1

num=int(input("Enter the number:"))               #2
lowlimit=int(input("Enter the lower limit:"))     #1
uplimit=int(input("Emter the upper limit:"))      #10

for i in range(1,uplimit):                        #(1,10)
    n=(i**num)                                    #n=(1**2)=1      n=4                n=9                n=16
    #print(n)
    #for i in range(lowlimit,uplimit):             #(1,10)
    if(n>=lowlimit) & (n<=uplimit):           #(1>=1)&(1<=10)   (4>=1 & 4<=10 )     (9>=1 & 9<=10)     (16>=1 & 16<=10)
        print(i,end=" ")                       #1                 4                        9               false

