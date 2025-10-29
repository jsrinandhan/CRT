'''
n=int(input())
for i in range(1,n+1):
    print(2**i,end=" ")
#'''

'''
a,n=5,int(input())
for i in range(n):
    print(a,end=" ")
    a+=2
#'''

'''
a,n=65,int(input())
for i in range(n):
    print(a+i,end=" ")
#'''

'''
a,n=97,int(input())
for i in range(n):
    print(a,end=" ")
    a+=2
#'''

'''
n=int(input())
for i in range(n):
    print('* $ @')
#'''

'''
n=int(input())
for i in range(n):
    print(chr(65+i),chr(90-i))
#'''

'''
n=int(input())
for i in range(n):
    print(chr(97+i),chr(65+i))
#'''

'''
n,m=map(int,input().split(","))
for i in range(n):
    print("* "*m,)
#'''

'''
n,m=map(int,input().split(","))
for i in range(n*2):
    for j in range(m):
        if i%2==0:
            print("$ @",end=" ")
        else:
            print("*",j+1,end=" ")
    print()
#'''

'''
n,m=map(int,input().split(","))
for i in range(n):
    for j in range(m):
        print((m*i)+(j+1),end=" ")
    print()
#'''

'''
n=int(input())
for i in range(n):
    for j in range(n+1):
        if i+j<n:
            print("*",end=" ")
        else:
            print("@",end=" ")
    print()
#'''

#'''
n=int(input())
for i in range(1,n+1):
    print(i,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()
for i in range(n,0,-1):
    print(i,end=" ")
    for j in range(1,n-i+2):
        print(j,end=" ")
    print()
print()
for i in range(1,n+1):
    print(i,end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print()
for i in range(n,0,-1):
    print(i,end=" ")
    for j in range(n-i+1,0,-1):
        print(j,end=" ")
    print()
print()
for i in range(1,n+1):
    print(i,end=" ")
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print()
print()
for i in range(1,n+1):
    print(i,end=" ")
    for j in range(n-i+1,n+1):
        print(j,end=" ")
    print()
print()
for i in range(n,0,-1):
    print(i,end=" ")
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()
print()
for i in range(n,0,-1):
    print(i,end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
    print()
print()