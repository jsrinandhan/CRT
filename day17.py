#Count the number of Extra edges
'''
def find(n,p):
    while n!=p[n]:
        n=p[n]
    return n

def union(p,s,n,m):
    pn=find(n,p)
    pm=find(m,p)
    if pn==pm:
        return False
    if s[pn]<=s[pm]:
        p[pn]=pm
        s[pm]+=s[pn]
    else:
        p[pm]=pn
        s[pn]+=s[pm]
    return True

v=int(input())
p=[i for i in range(v)]
s=[1]*v
ee=0
for _ in range(int(input())):
    n,m=map(int,input().split())
    if not union(p,s,n,m):
        ee+=1
noc=len(set(p))
if noc<=ee+1:
    print('Connection Possible')
else:
    print('Connection Not Possible')
#'''

#Bellman Ford Algorithm for Single Source Shortest Path and Cycle Detection
'''
v=int(input())
edges=[list(map(int,input().split())) for _ in range(int(input()))]
d=[float('inf')]*v
d[int(input())]=0
for _ in range(v-1):
    for u,v,w in edges:
        if d[u]+w<d[v] and d[u]!=float('inf'):
            d[v]=d[u]+w
print(d)
for u,v,w in edges:
    if d[u]+w<d[v] and d[u]!=float('inf'):
        print('Cycle Detected')
        break
else:
    print('Cycle Not Detected')
#'''

#Dijkstra Algorithm for All Pair Shortest Path and Cycle Detection
'''
v=int(input())
mat=[list(map(int,input().split())) for _ in range(v)]
dis=[[float('inf')]*v for _ in range(v)]
for i in range(v):
    dis[i][i]=0
edges=[]
for i in range(v):
    for j in range(v):
        if mat[i][j]!=0:
            edges.append((i,j,mat[i][j]))
for n,m,w in edges:
    dis[n][m]=w
for i in range(v):
    for n,m,w in edges:
        if dis[n][m]>dis[n][i]+dis[i][m] and dis[n][i]!=float('inf') and dis[i][m]!=float('inf') and i!=m and i!=n:
            dis[n][m]=dis[n][i]+dis[i][m]
print(dis)
for n,m,w in edges:
    if dis[n][m]>dis[n][i]+dis[i][m]:
        print('Cycle Detected')
        break
else:
    print('Cycle Not Detected')
#'''

#Dijkstra Algorithm for All Pair shortest path without using extra matrix
'''
v,e=int(input()),int(input())
edges=[list(map(int,input().split())) for _ in range(e)]
for via in range(v):
    for n,m,w in edges:
        edges[n*v+m][2]=min(edges[n*v+via][2]+edges[via*v+m][2],edges[n*v+m][2])
#'''

#Find Number of Strongly Connected Component usind kosaraju's algorithm
'''
v,e=int(input()),int(input())
edges=[list(map(int,input().split())) for _ in range(e)]
adj=[[] for _ in range(v)]  
for n,m,w in edges:
    adj[n].append((m,w))
vis=[False]*v
low=[0]*v
stack=[]
scc=0
def dfs(n):
    vis[n]=True
    low[n]=n
    for m,w in adj[n]:
        if not vis[m]:
            dfs(m)
            low[n]=min(low[n],low[m])
        elif m in stack:
            low[n]=min(low[n],low[m])
    if low[n]==n:
        scc+=1
        while stack:
            m=stack.pop()
            if low[m]==n:
                break
for i in range(v):
    if not vis[i]:
        dfs(i)
print(scc)
#'''