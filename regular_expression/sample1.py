# check for either "a" or "b" 
from re import *
pattern="[a-z]"
matcher=finditer(pattern,"abc -@hgb")
for match in matcher:
    print(match.start())
    print(match.group())
