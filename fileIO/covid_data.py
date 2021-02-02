f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    curved=data[6]
    death=data[7]
    confirmed=data[8]
    if state not in dict:
        dict[state]={"state":state,"curved":curved,"death":death,"confirmed":confirmed}
    else:
        dict[state] = {"state": state, "curved": curved,"death":death,"confirmed": confirmed}
print(dict)
def print_data(**kwargs):
    print(kwargs)
    state = kwargs["state"]
    if state in dict:

        print(dict[state]["state"])
    else:
        print("state does not exists:")
print_data(state="kerala")










# def print_data(**kwargs):
#
#     state=kwargs["state"]
#
#
# #     if state in covid:
#         print(covid[state]["state"])
#         # if "prop" in kwargs:
#         #     prop = kwargs["prop"]
#         #     print(covid[state][prop])
#
#     else:
#         pass
#
# print_data(state="kerala")

