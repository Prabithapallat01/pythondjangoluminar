words="ABCABCCEEEEEABBCEEEE"

dict={}
for ch in words:
    if(ch not in dict):
        dict[ch]=1
    else:
        dict[ch]+=1

for k,v in dict.items():
    print(k,",",v)
    
data=sorted(dict,key=dict.get,reverse=True)
print(data)
