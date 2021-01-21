students_names={"alan","aleena","ram","leena","jins","jimmy","jhon","Neena","Mega"}
failed_stud={"Mega","leena","ram"}
diff=students_names.difference(failed_stud)
print("passed students:",diff)
inter=students_names.intersection(failed_stud)
print("failed students:",inter)