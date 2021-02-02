size=int(input("Enter the size:"))# 2
top=0
stk=[]
n=1
def push():
    item=int(input("Enter the item:"))#20,34
    global top
    if top<size:#  0<2   1<2
        stk.insert(top,item)#  0,20    1,34
        top+=1
    else:
        print(top)
        print("stack is overflow:")
def pop():
    global top
    top-=1
    if top<0: #2<0
        print("stack is empty:")
    else:
        print(stk[top], "poped out:")
def display():
    for i in range(0,top):
        print(stk[i])
while(n!=0):
    option=int(input("Enter the potion press 1)PUSH 2)POP 3)DISPLAY   :"))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    n=int(input("Do you want to continue press 0 for exit:"))
