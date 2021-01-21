# create a list
list=["Mango","Apple","Banana","Cherry"]
print(list[3])

#update values in list
list[3]="Grapes"
print(list)

#Adding values to the list
list.append("Watermelon")
print(list)

#Removing elements from list
list.remove("Apple")
print(list)

#find length of list
mac=len(list)
print(mac)

#How to print values in one by one from list using for loop

for i in list:
    print(i)

# Concatinate two list
list2=["Rose","lilly"]
concate=list+list2
print(concate)

#using zip() function
x=zip(list,list2)
print(tuple(x))