# To create Multiplication table

num = int(input("Which multiplication table do you want?"))
limit = int(input("Enter the limit:"))
i = 1
while (i <= limit):
    print(num, "*", i, "=", (num * i))
    i += 1
