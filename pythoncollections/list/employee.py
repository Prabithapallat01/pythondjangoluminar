employee=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","devolper",40000] ,
    [14,"jhoni","devolper",30000],
    [15,"sabir","devolper",40000],
    [16,"tino","devolper",40000],
    [17,"tomis","devolper",47000],
    [18,"jhonis","devolper",32000]
]
#total_amnt=0
#for emp in employee:
 #   total_amnt =total_amnt+emp[3]
#print("Total amount=",total_amnt)
#print highest salary
#salary_list=[]
#for emp in employee:
   # salary_list.append(emp[3])
#print(salary_list)
#high_salary=max(salary_list)
#print(high_salary)
#for emp in employee:
  #  if(emp[3]==high_salary):
   #  print(emp)
salary_list=[]
for emp in employee:
    salary_list.append(emp[3])
low_salary=min(salary_list)
for emp in employee:
    if((emp[2]=="devolper") & (emp[3]==low_salary)):
        print(emp)