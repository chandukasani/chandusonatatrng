num1=10
num2=20
num3=3
if(num1>num2) and (num1>num3):
    print('num1 is highest')
elif(num2>num3):
    print('num2 is highest')
else:
    print('num3 is highest')



p1=input()
p2=input()
if(p1==p2):
    print('no result')
elif(p1=='rock' and p2=='scissor')or(p1=='paper' and p2=='rock')or(p1=='scissor' and p2=='paper'):
    print('p1 wins')
else:
    print('p2 wins')

n=int(input())
print (100-n)




n=int(input('enter the age:'))
if(n==0):
    print('you are not born')
elif(n==100):
    print('you age was 100Years')
else:
    x=100-n
    print(x,"years need to complete 100 years")

