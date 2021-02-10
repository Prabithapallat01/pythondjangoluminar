#will check lower_case "a" to "z"

#pre_define set

from re import *

# pattern="[a-z]"

# pattern="[A-Z]"

# pattern="[^0-9]"# except 0 to 9

pattern="[^a-zA-Z0-9]"
matcher=finditer(pattern,"abcAS_@123bfgd")
for match in matcher:
    print(match.start())
    print(match.group())