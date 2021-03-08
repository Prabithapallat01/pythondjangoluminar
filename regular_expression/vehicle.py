from re import *
re=(input("enter Registration number:"))
rule='kl\d{2}[a-zA-Z]{2}\d{4}'
matcher=fullmatch(rule,re)
if matcher==None:
    print("in valid")
else:
    print("vali")