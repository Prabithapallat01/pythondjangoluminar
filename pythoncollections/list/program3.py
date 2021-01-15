lst=[10,11,12,13,14,15,16,17]
evenlst=list()
oddlst=list()
for num in lst:
    if num%2==0:
       evenlst.append(num)
    else:
        oddlst.append(num)
print(evenlst)
print(oddlst)
total=sum(evenlst)
total1=sum(oddlst)
print(total)
print(total1)