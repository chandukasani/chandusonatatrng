def plyrgame(p1,p2):
    if (p1 == p2):
        return 'tie'
    elif (p1 == 'rock' and p2 == 'scissor') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissor' and p2 == 'paper'):
        return p1 + ' wins'
    elif (p1 == 'scissor' and p2 == 'rock') or (p1 == 'rock' and p2 == 'paper') or (p1 == 'paper' and p2 == 'scissor'):
        return p2 + ' wins'
    else:
        return 'invalid input'


p1=input('enter:')
p2=input('enter:')
sel=plyrgame(p1,p2)
print(sel)


