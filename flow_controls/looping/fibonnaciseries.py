# FIBONNACII SERIES:



num1=int(input("enter your number:"))  #5
a=0
b=1
count=0
if(num1<=0):                           #5<0
    print("Enter positive number:")
else:
    print("fibonnaci series is:")
    while(count<num1):                  
        print(a,end=" ")                # 0,    1       1     ..........................
        # print(b)                        
        c=a+b                           # c=1  c=2      c=3
        a=b                             # a=1   a=1     a=2
        b=c                             # b=1   b=2     b=3
        count += 1

    

