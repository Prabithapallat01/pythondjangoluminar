employee={1000:{"id":1000,"name":"leena","salary":20000,"exp":1},
          1001:{"id": 1001, "name": "james", "salary": 20500, "exp":2},
          1003:{"id":1002,"name":"malavika","salary":28000,"exp":4},
          1003:{"id":1003,"name":"krithi","salary":34000,"exp":5},
          1004:{"id":1004,"name":"miya","salary":342000,"exp":6}}
# def print_employee(id):
#     if id in employee:
#         print(employee[id]["name"])
#
# print_employee(id=1003)


# print employee[1001]

# if 1001 in employee:
#     print(employee[1001]["name"])
# else:
#     print("does not exist:")
#
# #print salary 1003
#
# if 1003 in employee:
#     print(employee[1003]["salary"])
# else:
#     pass

def print_employee(**kwargs):
    print(kwargs)
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
        else:
            pass

    else:
        print("does not exist")


print_employee(id=1003,prop="exp")