f=open("movies.csv","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    movies=data[1]
    years=data[2]
    if(movies not in dict):
        dict[movies]=years
    else:
        dict[movies] = years

for k,v in dict.items():
    print(k,"==========>",v)
print("maximum movies")
data=sorted(dict,key=dict.get,reverse=True)
print(data)
print(data[1],"=",dict.get(data[1]))
