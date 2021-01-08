from pip._vendor.six import print_

num=int(input("enter the number:"))
rev=0
#while(num!=0):      #123          12.3
    ##rint(digit,end="")
    #num=num//10
while(num!=0):
    digit=num%10
    rev=rev*10+rev
    num=num//10
print("rev=",rev)

#          1.23 digit = num % 10
