'''
def f(l,e):
    if len(l)==0:
        l.append(e)
        return
    t=l.pop(-1)
    f(l,e)
    l.append(t)
    return l
l=list(map(int,input().split()))
e=int(input())
print(f(l,e))
#'''
'''
def f(l):
    if len(l)==1:
        l.pop()
        return
    t=l.pop(-1)
    f(l)
    l.append(t)
    return l
l=list(map(int,input().split()))
print(f(l))
#'''
'''
def f(l,e):
    if len(l)==0 or l[-1]<e:
        l.append(e)
        return
    t=l.pop(-1)
    f(l,e)
    l.append(t)
    return l
l,e=list(map(int,input().split())),int(input())
print(f(l,e))
#'''
'''
m=[]
def f(i,o):
    if len(i)==0:
        m.append(o)
        return
    op1=o+i[0]
    op2=o
    i=i[1::]
    f(i,op1)
    f(i,op2)
    return m
print(f('abc',''))
#'''
#'''
m=[]
def f(s,t):
    if len(s)==0:
        m.append(t)
        return
    if not s[0].isalpha():
        t=t+s[0]
        s=s[1::]
    op1=t+s[0].upper()
    op2=t+s[0]
    s=s[1::]
    f(s,op1)
    f(s,op2)
    return m
print(f('a1#b@c',''))
#'''