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
print("Before Rotation:",lst)
d=3
n=6
def rotation(lst,d):
    for i in range(0,d):
        temp=lst[0]           #TEMP=1
        for j in range(0,n-1):  #((0,5)j=0,               j=1       j=2        j=3         j=4
            lst[j]=lst[j+1]   #  lst[0]=lst[1],  lst[0]=2  lst[1]=3  lst[2]=4   lst[3]=5  lst[4]=6
        lst[n-1]=temp
    return lst
rotatedlist=rotation(lst,d)
print("Before Rotation:",rotatedlist)





