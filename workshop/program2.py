num=input("Enter the number:")
i=1
data=0
pattern=""
while(i<=int(num)):
    res=num*i
    pattern=pattern+"+"+res
    data+= int(res)
    i+=1

pattern=pattern.lstrip("+")
print(pattern)
