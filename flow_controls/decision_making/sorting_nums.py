a=int(input("Enter the nums:"))
b=int(input())
c=int(input())
a1=min(a,b,c)      # a1=min( 45, 100,78)***** min=45
a3=max(a,b,c)      #a3= max(45,100,78)  *****max=100
a2=(a+b+c)-a1-a3    #(45+100+78)-45-100       223-45-100
print("Number in sorted order is:",a1,a2,a3)
if(a>b)&(a>c):

    if(b>c):
        print(b, "Second largest number:")
    elif(c>b):
        print(c, "Second largest number:")
    elif(b==c):
        print(b,c, "Second largest number:")
if(b>a)&(b>c):

    if(a>c):
        print(a, "Second largest number:")
    elif(c>a):
        print(c, "Second largest number:")
    elif(a==c):
        print(a,c, "Second largest number:")
if(c>a)&(c>b):
    if(a>b):
        print(a, "Second largest number:")
    elif(b>a):
        print(b, "Second largest number:")





