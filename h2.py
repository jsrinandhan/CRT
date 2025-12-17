#1
'''
n,s=int(input()),0
for i in range(1,n+1):
    s+=(2*i)
print(s)
#'''

#2
'''
n,s=int(input()),0
for i in range(1,n+1):
    s+=((2*i)+1)
print(s)
#'''

#3
'''
n,s=int(input()),1
for i in range(2,n+1):
    s=s+i if i%2==0 else s-i
print(s)
#'''

#4
'''
n,s=int(input()),0
for i in range(1,n+1):
    s+=(i**3)
print(s)
#'''

#5
'''
n,s=int(input()),0
for i in range(1,n+1):
    s+=(i**3)
print(s)
#'''

#6
'''
n,s=int(input()),0
for i in range(1,n+1):
    a=1
    for j in range(2,i+1):
        a*=j
    s+=a
print(s)
#'''

#7
'''
n,s=int(input()),0
for i in range(1,n+1):
    s+=(i*((i+1)**2))
print(s)
#'''

#8
'''
n,x,s=int(input()),int(input()),0
for i in range(n):
    t=x**((2*i)+1)
    s=s+t if i%2==0 else s-t
print(s)
#'''

#9
'''
n,s=int(input()),0.0
for i in range(2,n+2):
    s+=(i/(i+1))
print(s)
#'''

#10
'''
n,s=int(input()),0.0
for i in range(1,n+1):
    t=2*i
    s+=(t/((t+1)**2))
print(s)
#'''

#11
'''
n,s=int(input()),0.0
for i in range(2,n+1):
    a=1
    for j in range(2,i+1):
        a*=j
    s+=(a/(i-1))
print(s)
#'''

#12
'''
n,s=int(input()),0.0
for i in range(2,n+2):
    nu,d=1,1
    for j in range(2,(i**2)+1):
        nu*=j
    for j in range(2,i+1):
        d*=j
    s+=(nu/d)
print(s)
#'''

#13
'''
n,x,s=int(input()),int(input()),0.0
for i in range(1,n+1):
    s+=((x**i)/(i+1))
print(s)
#'''

#14
'''
n,x,s=int(input()),int(input()),0.0
for i in range(2,n+2):
    s+=((x**i)/i)
print(s)
#'''

#15
'''
n,x,s=int(input()),int(input()),0.0
for i in range(1,n+1):
    a=1
    for j in range(2,x+i+1):
        a*=j
    s+=(a/i)
print(s)
#'''

#16
'''
n,s=int(input()),0.0
for i in range(1,n+1):
    z=(2*i)-1
    a=1
    for j in range(2,z+1):
        a*=j
    s+=(a/(a*(z+1)))
print(s)
#'''

#17
'''
n,x,s=int(input()),int(input()),0.0
for i in range(n):
    a=1
    for j in range(2,x+i+1):
        a*=j
    s+=(a/(10+(5*i)))
print(s)
#'''

#18
'''
n,s=int(input()),1
for i in range(2,n+2):
    a=0
    for j in range(1,i+1):
        a+=j
    s*=a
print(s)
#'''

#19 
'''
n,x,s=int(input()),int(input()),1.0
for j in range(2,x+1):
    s*=j
for i in range(2,n+1):
    t,a=((x**(i-1))//i),1
    for j in range(2,t+1):
        a*=j
    s=s-a if i%2==0 else s+a
print(s)
#'''

#20
'''
n,s=int(input()),0.0
for i in range(2,n+2):
    nu,d=0,1
    for j in range(1,i+1):
        nu,d=nu+j,d*j
    s+=(nu/d)
print(s)
#'''