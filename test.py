'''
a=int(input())
if a%2==0:
    print("It is an even number.")
else:
    print("It is an odd number.")
'''

'''
a=int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")
    for i in range(a, 0, -1):
        if i%4==0 and i%100!=0 or i%400==0:
            print(f"{i} is a leap year.")
            break
'''


a=int(input())
x='*'
for i in range(a):
    print(x.center(2*a-1))
    x+='**'


'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or n-1-i==j:
            print('*', end='')
        elif i==0 or i==n-1 or j==0 or j==n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
