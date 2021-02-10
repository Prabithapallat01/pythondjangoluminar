lst=[10,2,34,56]
pos=int(input("enter the position:"))
num1=int(input())
num2=int(input())

try:
    res= num1/num2
    print(res)
    print(lst[pos])
except Exception as e:
    print(e.args)
