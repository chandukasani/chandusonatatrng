def myfile():
    try:
        c = open('chndu.txt', 'r')
        print(c.read())
    except(FileNotFoundError):
        return ('not exists')
emp=myfile()
print(emp)