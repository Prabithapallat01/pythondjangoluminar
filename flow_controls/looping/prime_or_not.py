# To print given number is prime or not

num=int(input("Enter the number:")) #5           4
flg=0
if(num==1):
    print("not Prime:")
else:
    for i in range(2,num):             # (2,5)       (2,4)
        if(num%i==0):                  # (5%2==0)    (4%2==0)
            flg=flg+1                                 #flg=1
            break
        else:
            flg=0                       #flg=0
    if flg==0:
        print("Prime")
    else:
         print("Not prime:")