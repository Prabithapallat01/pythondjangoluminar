# #print the following pattern
# #1
# #1 2
# #1 2 3
# #1 2 3 4
# #1 2 3 4 5
#
#
#
#
#
#
#
# for i in range(1,5+1):      #(1,5+1)
#     for j in range(1,i+1):   # (1,1+1)
#         print(i,end=" ")
#     print()
#
#Task Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 8, print Weird
# If n is even and greater than 20, print Not Weird
n=int(input("n:"))
if n%2==0 and (n in range(2,5) or n>20):
    print("not weired")
else:
    print("weired")
