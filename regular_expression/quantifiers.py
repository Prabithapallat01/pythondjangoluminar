from  re import *

# pattern="a+"  #any number of "a" excluding  zero number vof "a"
# pattern="a*"    #any number of "a" including zero number of "a"
# pattern="a?"      #occurence of all "a" including zero number of "a"
pattern="a(2,4)"
matcher=finditer(pattern,"asaaadf-=nsgbA1234@#")
for match in matcher:
    print(match.start(),"-->",match.group())

