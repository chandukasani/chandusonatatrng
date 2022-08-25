d1={'chandu':'21-12-2000','priya':'27-08-2000','swathi':'03-09-2000','pavan':'25-10=2000','sandhya':'13-04-2001'}
print('we have these members birthday:')
for name in d1:
    print(name)
print('whos birthday u want:')
name=input()
if name in d1:
    print(name +'has a birthday on'+ dict[name])
else:
    print('we dont have '+ name +'birthday')