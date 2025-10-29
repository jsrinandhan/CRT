'''
l,k=list(map(int,input().split(","))),int(input())
for i in range(len(l)-k+1):
    s=0
    for j in range(i,i+k):
        s+=l[j]
    print(s,end=" ")
print()
i,s=0,0
for j in range(len(l)):
    s+=l[j]
    if j-i+1==k:
        print(s,end=" ")
        s,i=s-l[i],i+1
#'''

'''
l,k=list(map(int,input().split(","))),int(input())
max,min,mas,mis,i,s=0,sum(l),0,0,0,0
for j in range(len(l)):
    s+=l[j]
    if j-i+1==k:
        print(s,end=" ")
        if max<s:
            max,mas=s,i
        if min>s:
            min,mis=s,i
        s,i=s-l[i],i+1
    j+=1
print()
print('Maximum Sum:',max)
print('Minimum Sum:',min)
print(*[l[i] for i in range(mas,mas+k)])
print(*[l[i] for i in range(mis,mis+k)])
#'''

'''
s,k=input().lower(),int(input())
i,ch=0,""
for j in range(len(s)):
    ch+=s[j]
    if j-i+1==k:
        if len(set(ch))==k:
            print(ch,end=" ")
        i,ch=i+1,ch[1:]
    j+=1
#'''

'''
s,k=input().lower(),int(input())
d,i=dict(),0
for j in range(len(s)):
    if s[j] in d:
        d[s[j]]+=1
    else:
        d[s[j]]=1
    if j-i+1==k:
        if len(d)==k:
            print(s[i:j+1],end=" ")
        d[s[i]]-=1
        if d[s[i]]==0:
            d.pop(s[i])
        i+=1
#'''