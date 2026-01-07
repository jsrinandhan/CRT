#print(*[(x,y) for x in [-1,0,1] for y in [-1,0,1] if x!=0 or y!=0])
#Find number of Islands in a matrix using BFS
'''
def connected_islands_bfs(map):
    if not map:
        return 0
    
    r,c=len(map),len(map[0])
    visited=[[0]*c for _ in range(r)]
    count=0
    rows=[-1, -1, -1, 0, 0, 1, 1, 1]
    cols=[-1, 0, 1, -1, 1, -1, 0, 1]
    q=[]
    for i in range(r):
        for j in range(c):
            if map[i][j]==1 and not visited[i][j]:
                q.append((i,j))
                visited[i][j]=1
                while q:
                    cr,cc=q.pop(0)
                    for k in range(len(rows)):
                        nr=cr+rows[k]
                        nc=cc+cols[k]
                        if (nr>=0 and nr<r) and (nc>=0 and nc<c) and map[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc]=1
                            q.append((nc, nc))
                count+=1
    return count


r=int(input())
map=[[map(int,input().split())] for _ in range(r)]
print(connected_islands_bfs(map))
#'''
#Find number of different color Islands in a matrix using BFS
'''
def connected_islands_bfs(grid):
    if not grid:
        return 0
    r,c=len(grid), len(grid[0])
    visited=[[0]*c for _ in range(r)]
    count=0
    rows=[-1,-1,-1,0,0,1,1,1]
    cols=[-1,0,1,-1,1,-1,0,1]
    for i in range(r):
        for j in range(c):
            if grid[i][j]!=0 and not visited[i][j]:
                count+=1
                land=grid[i][j]
                queue=[]
                queue.append((i,j))
                visited[i][j]=1
                while queue:
                    cr,cc=queue.pop(0)  
                    for k in range(8):
                        nr=cr+rows[k]
                        nc=cc+cols[k]
                        if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc] and grid[nr][nc] == land:
                            visited[nr][nc] = 1
                            queue.append((nr,nc))  
    return count

r=int(input())
map=[[map(int,input().split())] for _ in range(r)]
print(connected_islands_bfs(map))

#'''
#Find the number of days to all oranges to rot
'''
def orangesRotting(map):
    r,c=len(map),len(map[0])
    q=[]
    dir=[(x,y) for x in [-1,0,1] for y in [-1,0,1] if x==0 or y==0 and x!=y]
    f=0
    for i in range(r):
        for j in range(c):
            if map[i][j]==2:
                q.append((i, j))
            elif map[i][j]==1:
                f+=1
    d=0
    while q and f>0:
        for i in range(len(q)):
            cr,cc=q.pop(0)
            for x,y in dir:
                nr=cr+x
                nc=cc+y
                if 0<=nr<r and 0<=nc<c and map[nr][nc]==1:
                    map[nr][nc]=2
                    f-=1
                    q.append((nr, nc))
        d+=1
    return d if f==0 else -1

r=int(input())
map=[list(map(int,input().split())) for _ in range(r)]
print(orangesRotting(map))
#'''
'''
def prims_algo(adj):
    vis=[False]*len(adj)
    queue=[(0,0,-1)]
    path=[]
    c=0
    while queue:
        queue.sort()
        wt,node,parent=queue.pop(0)
        if not vis[node]:
            vis[node]=True
            for nxt,w in adj[node]:
                if not vis[nxt]:
                    queue.append((w,nxt,node))
            path.append((parent,node))
            c+=wt
    print(c) 
    print(path)     
m=int(input())
l=[list(map(int,input().split())) for _ in range(m)]
adj={}
for i in range(m):
    adj[i]=[]
    for j in range(m):
        if l[i][j]>0:
            if i in adj.keys():
                adj[i].append((j,l[i][j]))
print(adj)
prims_algo(adj)
#'''
'''
class Solution:
    def union_(self, a, b, par, rank1):
        pa = self.find(a, par)
        pb = self.find(b, par)
        if pa == pb:
            return
        if rank1[pa] < rank1[pb]:
            par[pa] = pb
        elif rank1[pa] > rank1[pb]:
            par[pb] = pa
        else:
            par[pb] = pa
            rank1[pa] += 1
    def isConnected(self, x, y, par, rank1):
        return self.find(x, par) == self.find(y, par)
    def find(self, x, par):
        if par[x] != x:
            par[x] = self.find(par[x], par)
        return par[x]  
#'''
#Minimum Spanning Tree using Kruskal's Algorithm
#'''
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
l=[list(map(int,input().split())) for _ in range(m)]
adj={}
for i in range(m):
    adj[i]=[]
    for j in range(m):
        if l[i][j]>0:
            adj[i].append((j,l[i][j]))
krushkal_algo(adj)
#'''