students=[[10,"ajay","bca",250],
[11,"vjay","bca",240],
[12,"sibin","bca",220],
[13,"dino","mca",200],
[14,"tom","bca",180],
[15,"jain","bca",250],

]
mtotal,btotal=0,0
for stud in students:
    if stud[2]=="bca":
        btotal+=stud[3]
    else:
        mtotal += stud[3]
print("mca total=",mtotal)
print("bca total=",btotal)
