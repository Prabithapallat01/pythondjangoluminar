f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    if(state=="Telengana"):
       state="Telangana"
    confirmed_case=int(data[8])
    if state not in dict:
        dict[state]=confirmed_case
    else:
        dict[state]=confirmed_case

for k,v  in dict.items():
    print(k,"=======>",v)
data=sorted(dict,key=dict.get,reverse=True)
print(data)
print(data[0],"=",dict.get(data[0]))
