from re import *
pattern="ab"

matcher=finditer(pattern,"abababaaababa")
for match in matcher:
    print(match.start())
    print(match.group())





