def leapYear(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year=int(input("enter year"))
if(leapYear(year)):
    print(year,"this year is leap year:")
else:
    print(year, "this year is not leap year")
