a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
chandu=[]
for i in range(len(a)):
    if a[i] in b:
        chandu.append(a[i])
chandu=set(chandu)
print (chandu)