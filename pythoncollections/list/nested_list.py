# Given a nested list extend it with adding
# sub list ["h", "i", "j"] in a such a way that it will look like the following list
# lst1=["a", "b", ["c", ["d","e",["f","g"],"k"],"l"],"m","n"]
# lst2=["h","i","j"]
# lst1[2][].extend(lst2)
# print(lst1)
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]

list1[2][1][2].extend(list2)
print(list1)
