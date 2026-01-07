#Binnary Search
#Iterative
'''
#l=list(map(int,input().split(',')))
#k=int(input())
l=[1,2,3,4,5,6,7,8,9]
k=4
s,e=0,len(l)-1
while s<=e:
    mid=(s+e)//2
    if l[mid]==k:
        print(f'{k} Element found at {mid+1} index')
        break
    elif l[mid]>k:
        e=mid-1
    else:
        s=mid+1
else:
    print(f'{k} Element not found')
#'''
#Recursions
'''
def bs(s,e,l,k):
    if s>=e:
        return -1
    mid=(s+e)//2
    if l[mid]==k:
        return mid+1
    elif l[mid]>k:
        return bs(s,mid-1,l,k)
    else:
        return bs(mid+1,e,l,k)
def lower_bond(s,e,l,k):
    if s<=e:
        mid=(s+e)//2
        if l[mid]>=k:
            return lower_bond(s,mid-1,l,k)
        elif l[mid]<k:
            return lower_bond(mid+1,e,l,k)
    return l[s]
def upper_bond(s,e,l,k):
    if s<=e:
        mid=(s+e)//2
        if l[mid]>k:
            return upper_bond(mid+1,e,l,k)
        elif l[mid]>k:
            return upper_bond(s,mid-1,l,k)
    return l[s]


l=list(map(int,input().split(',')))
k=int(input())
i=bs(0,len(l)-1,l,k)
if i==-1:
    print(f'{k} Element not found')
else:
    print(f'{k} Element found at {i} index')
print(lower_bond(0,len(l)-1,l,k))
print(upper_bond(0,len(l)-1,l,k))
#'''
'''
n=int(input())
s,e,a=0,n,-1
while s<=e:
    m=(s+e)//2
    if m**2==n:
        a=m
        break
    elif m**2<n:
        a=m
        s=m+1
    else:
        e=m-1
print(a)
#'''

'''
def koko_eating_bananas(piles,k):
    s,e=max(piles),sum(piles)
    while s<e:
        m=(s+e)//2
        h=0
        for i in piles:
            h+=i//m
            if h>k:
                break
        if h<=k:
            e=m
        else:
            s=m+1
    return s
piles=list(map(int,input().split(',')))
k=int(input())
print(koko_eating_bananas(piles,k))
#'''

#'''
def leetcode_1482(bloomDay,m,k):
    s,e=max(bloomDay),sum(bloomDay)
    while s<e:
        m=(s+e)//2
        h=0
        for i in bloomDay:
            h+=i//m
            if h>m:
                break
        if h<=m:
            e=m
        else:
            s=m+1
    return s
    
#'''