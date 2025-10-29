#'''
l,ws=list(map(int,input().split(","))),int(input())
w=[]
for j in range(len(l)):
    w.append(l[j])
    if len(w)==ws:
        m=w[0]
        for v in w:
            m=v if v>m else m
        print(m,end=" ")
        w.pop(0)
#'''
#'''
l,ws=list(map(int,input().split(","))),int(input())
w=[]
for j in range(len(l)):
    w.append(l[j])
    if len(w)==ws:
        m=w[0]
        for v in w:
            m=v if v<m else m
        print(m,end=" ")
        w.pop(0)
#'''