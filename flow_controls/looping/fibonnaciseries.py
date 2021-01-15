num1=int(input("enter your number:"))
a=0
b=1
count=0
if(count>0):
    print("Enter positive number:")
else:
    print("fibonnaci series is:")
    while(count<=num1):
       # print(a)
        c=a+b
        a=b
        b=c
        count += 1

        print(c)

