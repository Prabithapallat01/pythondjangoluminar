#To print multiplication table


limit=int(input("Enter bthe limit:"))
num=int(input("Enter bthe table:"))

for i in range(1,limit+1):
    print(i,"*",num,"=",(num*i))