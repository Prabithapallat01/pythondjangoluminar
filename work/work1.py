# #  [1,2,3,4,5,6] [4,5,6,1,2,3]
# #lst=[1,2,3,4,5,6]
# def leftRotate(lst, d, n):
#     for i in range(d):
#         leftRotatebyOne(lst, n)
#
#
# # Function to left Rotate arr[] of size n by 1*/
# def leftRotatebyOne(lst, n):
#     temp = lst[0]
#     for i in range(n - 1):
#         lst[i] = lst[i + 1]
#     lst[n - 1] = temp
#
#
# # utility function to print an array */
# def printlist(lst, size):
#     for i in range(size):
#         print("% d" % lst[i], end=" ")
#
#
# # Driver program to test above functions */
# lst= [1, 2, 3, 4, 5, 6, ]
# leftRotate(lst, 3, 6)
# printlist(lst,6)







lst=[1,2,3,4,5,6]
d=3
n=6
for i in range(0,d):
    temp=lst[0]           #TEMP=1
    for j in range(0,n-1):  # j=0  1
        lst[j]=lst[j+1]   #  2,  3,4,
    lst[n-1]=temp
for  i in range(0,n):
    print(lst[i],end=" ") #   4,5,6,1,2,3