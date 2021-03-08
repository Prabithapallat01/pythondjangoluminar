# write a python program to count the no.of vowels in a string


str=input("Enter the string:")
vowels=0
for i in str:
    if(i=='a'or i=='e'or i=='o'or i=='i'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
            vowels+=1
print("number of vpwels are:")
print(vowels)