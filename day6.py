#1. COUNT FREQUENCY OF NUMBERS IN A LIST
'''
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
x=set(l)
for i in x:
    print(i,l.count(i),sep='-')
'''

#2. COUNT FREQUENCY OF NUMBERS IN A LIST and find most repeated number
'''
n=int(input())
ma,maxel=0,0
l=[]
for i in range(n):
    l.append(int(input()))
x=set(l)
for i in x:
    print(i,l.count(i),sep='-')
    y=l.count(i)
    if(y>ma):
        ma=y
        maxel=i
print('most repeated number:',maxel)
'''        

#3. print missing elements b/w max and min elements in a list
'''
n=int(input())
ma,mi=0,999
l=[]
for i in range(n):
    l.append(int(input()))
x=set(l)
for i in x:
    if(ma<i):
        ma=i
    if(mi>i):
        mi=i
for i in range(mi,ma+1):
    if(i not in l):
        print(i,end=' ')

'''

#4. 1 input and different outputs     
# i/p:[5,6,5,3,4,8,5,6]   
# o/p 1:[1, 1, 2, 1, 1, 1, 3, 2]
# o/p 2:[3, 2, 2, 1, 1, 1, 1, 1]
# o/p 3:[3, 2, 3, 1, 1, 1, 3, 2]
'''
n=int(input())
l,op1,op2,op3=[],[],[],[],[]
for i in range(n):
    l.append(int(input()))
for i in range(len(l)-1,-1,-1):
    count=1
    for j in range(i-1,-1,-1):
        if(l[i]==l[j]):
            count+=1
    l1.insert(0,count)
print(l1)
for i in range(0,len(l)):
    count=1
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            count+=1
    l1.append(count)
print(l1)
for i in range(0,len(l)):
    count=0
    for j in range(0,len(l)):
        if(l[i]==l[j]):
            count+=1
    l1.append(count)
print(l1)
'''



#5.ROTATE LEFT
#i/p:[5,4,6,36,23,12,17,25]   n=1 o/p:[25, 5, 4, 6, 36, 23, 12, 17] ; n=2 o/p:[17, 25, 5, 4, 6, 36, 23, 12]
'''
l=eval(input())
n=int(input())
for i in range(n):
    y=l.pop()
    l.insert(0,y)
print(l)
'''
#6.#ROTATE RIGHT
'''
l=eval(input())
n=int(input())
for i in range(n):
    y=l.pop(0)
    l.append(y)
print(l)
'''

#7. Rotate right or left b/w two indices in particular list (right=R,left=L in t1):
'''
l=eval(input())
s1,s2=map(int,input().split())
t1=input()
if(t1=='L'):
    t=l[s2]
    for i in range(s2,s1,-1):
        l[i]=l[i-1]
    l[s1]=t
elif(t1=='R'):
    t=l[s1]
    for i in range(s1,s2):
        l[i]=l[i+1]
    l[s2]=t
print(l)
//method 2
l=eval(input())
s1,s2=map(int,input().split())
t1=input()
if(t1=='L' or t1=='l'):
        y=l.pop(s2)
        l.insert(s1,y)
elif(t1=='R' t1=='r'):
        y=l.pop(s1)
        l.insert(s2,y)
print(l)
'''