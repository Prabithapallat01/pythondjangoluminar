pattern="ABACCABBBEEE"
# find first recursive word
dict={}

for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
for key,value in dict.items():
    print(key,",",value)
data=sorted(dict,key=dict.get)
print(data)