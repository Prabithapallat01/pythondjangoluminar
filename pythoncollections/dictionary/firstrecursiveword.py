pattern="ABACCABBBEEE"
# find first recursive character

dict={}

for ch in pattern:
    if(ch not in dict):
        dict[ch]=1
    else:
       print(ch,"it is first recursive character:")
       break
