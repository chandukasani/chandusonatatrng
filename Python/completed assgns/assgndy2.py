def sumoftwonums(no1=10,no2=30,no3=40):
    if (no1 > no2) and (no1 > no3):
       return no1
    elif (no2 > no3):
        return no2
    else:
        return no3

sum=sumoftwonums(23,34,4)
print(sum,'is highest one')