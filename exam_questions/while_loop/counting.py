# Given a number count the total number of digits in a number


n=int(input("enter the number:"))
count=0
while n!=0:
    n//=10
    count+=1
print(count)