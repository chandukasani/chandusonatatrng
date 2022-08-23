def birth(n):
    if (n == 0):
        return 'you need 100 years to complete'
    elif (n == 100):
        return 'you are 100 years old'
    else:
        x = 100 - n
        return x

n=int(input('enter the age:'))
age=birth(n)
print(age)

