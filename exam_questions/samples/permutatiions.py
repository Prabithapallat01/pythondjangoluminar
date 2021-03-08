# from itertools import permutations
# strg=input("enter string:")
# permutations=[''.join(p) for p in permutations(strg)]
# print(str(permutations))
from itertools import *
S, k = input().split()
for i in permutations(sorted(S),int(k)):
    print("".join(i))