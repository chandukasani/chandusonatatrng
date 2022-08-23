def pal(n):
    if (n == n[::-1]):
        return 'palindrome'
    else:
        return 'not a palindrome'

s=input("enter a number")
r=pal(s)
print(r)

