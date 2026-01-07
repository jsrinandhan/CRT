'''
m,n=map(int,input().split())
li,s=[[int(input()) for _ in range(n)] for _ in range(m)],[0]*n
print(li)
for row in li:
    for j in range(n):
        s[j]+=row[j]
mv=max(s)
print(s.index(mv))
#'''
#Diagonal difference
#'''
m=int(int(input()))
li=[[int(input()) for _ in range(m)] for _ in range(m)]
s1,s2=0,0
for r in range(m):
    for c in range(m):
        if r==c:
            s1+=li[r][c]
        if r+c==m-1:
            s2+=li[r][c]
print(abs(s1-s2))
#'''