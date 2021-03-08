# a,k first character must be an alphabet b/w a,k
# second must be a digit divisible by 3
# folloewd by any no.of character


from re import *

var_name=input("enter name:")
rule="[a-k][369][a-zA-Z0-9] "
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid:")
else:
    print("valid")