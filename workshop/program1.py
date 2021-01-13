n= int(input("Enter the rows:"))
for i in range(1,n+1):
    for j in range(1,2*n):
        if((i==n)|((i+j)==n+1)|((j-i)==n-1)):
            print("*",end="")
        else:
            print(end=" ")
    print()

