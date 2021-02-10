from re import *
acc=(input("enter phonenumber"))
# rule='kl\d{2}[a-zA-Z]{2}\d{4}'
# rule='(91)?\d{10}'# phone number
rule=''
matcher=fullmatch(rule,acc)
if match==None:
    print("in valid")
else:
    print("vali")