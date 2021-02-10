from re import *
#pattern="\s"# check for space
#pattern="\d"   #check for digit
# pattern="\D" #except digit
# pattern="\w"  #check for all words except special characters
pattern="\W" #check for except words


matcher=finditer(pattern,"adsgbhnbj@_-0k,sjh lk")
for match in matcher:
    print(match.start(),"-->",(match.group()))
