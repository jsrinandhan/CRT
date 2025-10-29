'''
m=[]
def s(n):
    c=0
    for i in n:
        c+=i
    return c
def f(l,t):
    if len(l)==0:
        m.append(s(t))
        return
print(f(list(map(int,input().split())),[]))
#'''

'''
m=[]
def f(op,cl,s):
    if op==0 and cl==0:
        m.append(s)
        return
    
    if op==cl:
        s=s+'('
        op-=1
    if op==0:
        while cl:
            s=s+')'
            cl=cl-1
        m.append(s)
        return
    f(op-1,cl,s+'(')
    f(op,cl-1,s+')')
    #Another Way
    if op>0:
        f(op-1,cl,s+'(')
    if cl>op:
        f(op,cl-1,s+')')
    return m
print(f(3,3,''))
#'''
'''
m=[]
def f(n,z,o,s):
    if n==0:
        if o>z:
            m.append(s)
        return
    f(n-1,z,o+1,s+'1')
    f(n-1,z+1,o,s+'0')
f(100,0,0,'')
print(m)
#'''

#Quick Sorting
'''
def q(l,s,e):
    pi=0
    while s>e:
        while l[s]<l[pi]:
            s+=1
        while l[e]>l[pi]:
            e-=1
        if s>e:
            l[pi],l[e]=l[e],l[pi]
        else:
            l[e],l[s]=l[s],l[e]
def qs(li,l,r):
    pi=q(li,l,r)
    return [qs(li[])]
#'''