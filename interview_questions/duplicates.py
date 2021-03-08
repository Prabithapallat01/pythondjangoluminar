lst1 =  [3, 1, 5, 1, 10, 3, 5, 10]
# create an empty set
duplicates = set()
# loop through elements and find matches
for i in lst1:
    if i not in duplicates:#3 not in dupli
        duplicates.add(i)
# show data
print(lst1)
print(duplicates)