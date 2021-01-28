#Question 5: Remove 10, 20, 30 elements from a following set at once
#set1 = {10, 20, 30, 40, 50}

set1={10,20,30,40,50}
set1.difference_update({10,20,30})
print(set1)