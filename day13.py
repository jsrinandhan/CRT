'''
l,r,a=[5,7,14,20,25],[1,8,7,9,17],[]
m,n=len(l),len(r)
i,j,k=0,0,0
while i<m and j<n:
    if l[i]<=r[j]:
        a.append(l[i])
        i+=1
    else:
        a.append(r[j])
        j+=1
while i<m:
    a.append(l[i])
    i+=1
while j<n:
    a.append(r[j])
    j+=1
print(*a)
#'''
#Merge Sort
#'''
def merge(l,r):
    z=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            z.append(l[i])
            i+=1
        else:
            z.append(r[j])
            j+=1
    z.extend(l[i:])
    z.extend(r[j:])
def merge
#'''