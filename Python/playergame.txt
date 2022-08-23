p1=input()
p2=input()
if (p1 == p2):
    print('no result')
elif (p1 == 'rock' and p2 == 'scissor') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissor' and p2 == 'paper'):
    print('p1 wins')
elif (p1 == 'scissor' and p2 == 'rock') or (p1 == 'rock' and p2 == 'paper') or (p1 == 'paper' and p2 == 'scissor'):
    print('p2 wins')
else:
     print('provide crct one')


