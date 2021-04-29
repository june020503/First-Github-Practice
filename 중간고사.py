'''
a, b=input().split()
a, b=float(a), float(b)

x=0
for i in range(10):
    x+=a*b**i
    
print("%f" %x)
'''

'''
h1, m1, s1=input().split(':')
h1, m1, s1=int(h1), int(m1), int(s1)
h2, m2, s2=input().split(':')
h2, m2, s2=int(h2), int(m2), int(s2)

if h1>h2:
    if s1>=s2:
        s=s1-s2
    else:
        s=60+s1-s2
        m1-=1

    if m1>=m2:
        m=m1-m2
    else:
        m=m1-m2+60
        h1-=1

    h=h1-h2

elif h2>h1:
    if s2>=s1:
        s=s2-s1
    else:
        s=60+s2-s1
        m2-=1

    if m2>=m1:
        m=m2-m1
    else:
        m=m2-m1+60
        h2-=1

    h=h2-h1

else:
    h=0
    if m1>m2:
        if s1>=s2:
            s=s1-s2
        else:
            s=60+s1-s2
            m1-=1
        m=m1-m2
        
    
    elif m1<m2:
        if s2>=s1:
            s=s2-s1
        else:
            s=60+s2-s1
            m2-=1
        m=m2-m1

    else:
        m=0
        s=abs(s1-s2)
        
print("{:02d}:{:02d}:{:02d}".format(h, m, s))
'''

'''
a=int(input())
a1=a//100
a2=(a%100)//10
a3=a%10

if a1>a2:
    if a1>a3:
        max_=a1
        if a2>a3:
            middle_=a2
            min_=a3
        else:
            middle_=a3
            min_=a2
    else:
        max_=a3
        middle_=a1
        min_=a2
else:
    if a2>a3:
        max_=a2
        if a1>a3:
            middle_=a1
            min_=a3
        else:
            middle_=a3
            min_=a1
    else:
        max_=a3
        middle_=a2
        min_=a1
        
x=100*max_+10*middle_+min_
y=100*min_+10*middle_+max_

print(x-y)
'''

'''
a=int(input())
x=''
for i in range(1, a+1):
    x='*'*(i*2-1)
    print(x.center(2*a-1))
for i in range(a-1,0,-1):
    x='*'*(i*2-1)
    print(x.center(2*a-1))
'''  
