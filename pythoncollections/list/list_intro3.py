#Given a two Python list.
# Iterate both lists simultaneously such that list1 should display
# item in original order and list2 in reverse order
lst1=[200,345,122,678,234]
lst2=[500,344,800,100,300]
for x, y in zip(lst1,lst2[::-1]):
    print(x,y)