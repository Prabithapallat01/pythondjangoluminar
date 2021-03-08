from re import *
mob_number=input("enter your phone number:")
rule="(91)?\d{10}"
matcher=fullmatch(rule,mob_number)
if matcher==None:
    print("invalid phone number:")
else:
    print("valid phone number:")