#Write a Python Program to Check Common Letters in Two Input Strings?


s1= input("Enter the first string:")
s2= input("Enter bthe second string:")
lst=list(set(s1)&set(s2))
print("common letters are:")
for i in lst:
    print(i)