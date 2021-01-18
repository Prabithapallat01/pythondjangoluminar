lst=[2,5,6,7]
out=list()
total=sum(lst)
for num in lst:
    out.append(total-num)
print(out)