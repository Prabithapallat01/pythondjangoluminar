from functools import reduce
lst=[10,11,12,13,14,15]
# sum=reduce(lambda num1,num2:num1+num2,lst)
# print(sum)

# highest value in list
# highesr_val=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
# print(highesr_val)


#lowest value in list:

lowest_val=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(lowest_val)