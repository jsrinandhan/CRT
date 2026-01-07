#3. Check the cycle in the given graph
'''
def check(adj):
    vis=[False]*len(adj)
    queue=[(0,-1)]
    while queue:
        n,p=queue.pop(0)
        if not vis[n]:
            vis[n]=True
            for i in adj[n]:
                if not vis[i]:
                    queue.append((i,n))
                elif i!=p:
                    print('Cycle Detected')
                    return
    print('Cycle Not Found')
m=int(input())
li=[list(map(int,input().split())) for _ in range(m)]
adj={}
for i in range(m):
    adj[i]=[]
    for j in range(m):
        if li[i][j]>0:
            adj[i].append(j)
check(adj)
#'''

#2. Find the shortest path from 2 to 3
'''
def shortest_path(g,so,dt):
    vis=[[False]*len(g) for _ in range(len(g))]
    queue=[(so,0,[so])]
    vis[so[0]][so[1]]=True
    dir=[(-1,0),(0,1),(1,0),(0,-1)]
    while queue:
        n,d,p=queue.pop(0)
        if n==dt:
            print(*p)
            print(d)
            return
        for nn in dir:
            x,y=n[0]+nn[0],n[1]+nn[1]
            if 0<=x<len(g) and 0<=y<len(g) and vis[x][y]==False and g[x][y]!=0:
                queue.append(((x,y),d+1,p+[(x,y)]))
                vis[x][y]=True
    print('No Path')
        

m=int(input())
g=[list(map(int,input().split())) for _ in range(m)]
so=(0,0)
for i in range(m):
    for j in range(m):
        if g[i][j]==2:
            so=(i,j)
        if g[i][j]==3:
            dt=(i,j)
shortest_path(g,so,dt)
#'''

#1. Find the min cost spanning tree using krushkal's algorithm
def find(i,p):
    if p[i]!=i:
        p[i]=find(p[i],p)
    return p[i]

def union(i,j,p,r):
    x=find(i,p)
    y=find(j,p)
    if x!=y:
        if r[x]<r[y]:
            p[x]=y
        elif r[x]>r[y]:
            p[y]=x
        else:
            p[y]=x
            r[x]+=1

def krushkal_algo(adj):
    p=[i for i in range(len(adj))]
    r=[0]*len(adj)
    edges=[]
    for i in adj:
        for j,w in adj[i]:
            edges.append((w,i,j))
    edges.sort()
    mst=[]
    c=0
    for w,i,j in edges:
        if find(i,p)!=find(j,p):
            union(i,j,p,r)
            c+=w
            mst.append((i,j,w))
    print(c,mst)
    
m=int(input())
g=[list(map(int,input().split())) for _ in range(m)]
adj={}
for i in range(m):
    adj[i]=[]
    for j in range(m):
        if g[i][j]>0:
            adj[i].append((j,g[i][j]))
krushkal_algo(adj)