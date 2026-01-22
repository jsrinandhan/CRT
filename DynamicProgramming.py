# Factorial, fibonacci series, prime numbers
'''
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

def fib(n):
    if n==1:
        return 0
    if n==2 or n==3:
        return 1
    return fib(n-1)+fib(n-2)

def check(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def prime(n):
    if n==0:
        return 0
    c,num=0,1
    while c!=n:
        num+=1
        if check(num):
            c+=1
    return num

n=int(input())
s1,s2,s3=0,0,0
while n>0:
    r=n%10
    s1+=fact(r)
    s2+=fib(r)
    s3+=prime(r)
    n=n//10
print(s1,s2,s3)
#'''

# Factorial using Dynamic Programming
'''
def factorial(n,fact):
    if n==0 or n==1:
        return 1
    if fact[n]!=-1:
        return fact[n]
    fact[n]=n*factorial(n-1,fact)
    return fact[n]

fact=[-1]*100
n=int(input())
s=0
while n>0:
    r=n%10
    if fact[r]!=-1:
        s+=fact[r]
    else:
        s+=factorial(r,fact)
    n//=10
print(s)
#'''

'''
def stairs(n,st):
    if n==0 or n==1:
        return 1
    if st[n]!=-1:
        return st[n]
    st[n]=stairs(n-1,st)+stairs(n-2,st)
    return st[n]

st=[-1]*20
n=int(input())
#'''

# Fractional Knapsack without using recursion
'''
n=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
cap=int(input())
prwt=list(zip([pr[i]/wt[i] for i in range(n)],wt))
prwt.sort(reverse=True)
s,i=0,0
while i<len(prwt) and cap>0:
    if cap>=prwt[i][1]:
        s+=prwt[i][0]*prwt[i][1]
        cap-=prwt[i][1]
    else:
        s+=cap*prwt[i][0]
        break
    i+=1
print(s)

#'''

'''
n=int(input())
li=list(list(map(int,input().split())) for _ in range(n))
li.sort(key=lambda x:x[1],reverse=True)
cap=int(input())
s,i=0,0
while i<len(li) and cap>0:
    if cap>=li[i][1]:
        cap-=li[i][1]
        s+=li[i][0]
    i+=1
print(s)
#'''

'''
def knapsack(cap,n,wt,pr):
    if n>=len(wt) or cap<=0:
        return 0
    incl,excl=0,0
    if cap>=wt[n]:
        incl=pr[n]+knapsack(cap-wt[n],n+1,wt,pr)
    excl=knapsack(cap,n+1,wt,pr)   
    return max(incl,excl)

m=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
cop=int(input())
print(knapsack(cop,0,wt,pr))
#'''

'''
def knapsack(cap,n,wt,pr):
    if n>=len(wt) or cap<=0:
        return 0
    if cap<wt[n]:
        return knapsack(cap,n+1,wt,pr)   
    return max(pr[n]+knapsack(cap-wt[n],n+1,wt,pr),knapsack(cap,n+1,wt,pr))

wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
cop=int(input())
print(knapsack(cop,0,wt,pr))
#'''


#knapsack tabulation
'''
def knapsack_tab(W,wt,val,n):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(W+1):
            if wt[i-1]<=w:
                dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]
W=int(input())
n=int(input())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
print(knapsack_tab(W,wt,val,n))
#'''

'''
def max_nonadj(li,n,dp):
    if n>=len(li):
        return 0
    if dp[n]!=-1:
        return dp[n]
    incl=li[n]+max_nonadj(li,n+2,dp)
    excl=max_nonadj(li,n+1,dp)
    dp[n]=max(incl,excl)
    return dp[n]

li=list(map(int,input().split()))
n=len(li)
dp=[-1]*n
dp[n-1]=li[n-1]
print(max_nonadj(li,0,dp))
#'''

'''
li=list(map(int,input().split()))
n=len(li)
c,p1,p2=0,li[0],0
for i in range(1,n):
    c=max(p1,li[i]+p2)
    p2,p1=p1,c
print(max(p1,c))
#'''

'''
def check(li,n,tar):
    if tar==0:
        return True
    if n>=len(li) or tar<0:
        return False
    incl=False
    if li[n]<=tar:
        incl=check(li,n+1,tar-li[n])
    excl=check(li,n+1,tar)
    return incl or excl

li=list(map(int,input().split()))
tar=int(input())
print(check(li,0,tar))
#'''

#Tabulation Method
'''
li=list(map(int,input().split()))
tar=int(input())
dp=[[False]*(tar+1) for _ in range(len(li)+1)]
for i in range(1,len(li)+1):
    dp[i][0]=True
    for j in range(1,tar+1):
        if li[i-1]<=j:
            dp[i][j]=dp[i-1][j-li[i-1]] or dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]
print(dp[len(li)][tar])
#'''

'''
def check(li,n,tar):
    if tar==0:
        return True
    if n>=len(li) or tar<0:
        return False
    incl=False
    if li[n]<=tar:
        incl=check(li,n+1,tar-li[n])
    excl=check(li,n+1,tar)
    return incl or excl

li=list(map(int,input().split()))
tar=sum(li)
if tar%2==0:
    print(check(li,0,tar//2))
else:
    print(False)
#'''

#In how many ways we get the target sum from the given array
'''
def check(li,n,tar):
    if tar==0:
        return 1
    if n>=len(li) or tar<0:
        return 0
    incl=check(li,n+1,tar-li[n])
    excl=check(li,n+1,tar)
    return incl+excl

def check_dp(li,n,tar,dp):
    if tar==0:
        return 1
    if n>=len(li):
        return 0
    if dp[n]!=-1:
        return dp[n]
    incl=0
    if li[n]<=tar:
        incl=check(li,n+1,tar-li[n],dp)
    excl=check(li,n+1,tar,dp)
    dp[n]=incl+excl
    return dp[n]

li=list(map(int,input().split()))
tar=int(input())
print(check(li,0,tar))
dp=[-1]*len(li)
print(check_dp(li,0,tar,dp),dp)
#'''

'''
def check(wts,pro,n,s):
    if n>=len(wts) or s<=0:
        return 0
    incl=0
    if wts[n]<=s:
        incl=pro[n]+check(wts,pro,n+1,s-wts[n])
    excl=check(wts,pro,n+1,s)
    return max(incl,excl)

def check_dp(wts,pro,n,s,dp):
    if n>=len(wts) or s<=0:
        return 0
    if dp[n][s]!=0:
        return dp[n][s]
    incl=0
    if wts[n]<=s:
        incl=pro[n]+check_dp(wts,pro,n+1,s-wts[n],dp)
    excl=check_dp(wts,pro,n+1,s,dp)
    dp[n][s]=max(incl,excl)
    return dp[n][s]

wts=list(map(int,input().split()))
pro=list(map(int,input().split()))
cap=int(input())
print(check(wts,pro,0,cap))
dp=[[0]*(cap+1) for _ in range(len(wts)+1)]
print(check_dp(wts,pro,0,cap,dp),dp)
#'''

'''
wts=list(map(int,input().split()))
pro=list(map(int,input().split()))
cap=int(input())
dp=[[0]*(cap+1) for _ in range(len(wts)+1)]
dp[0][0]=0
for i in range(1,len(wts)+1):
    dp[i][0]=0
    for j in range(1,cap+1):
        if wts[i-1]<=j:
            dp[i][j]=max(pro[i-1]+dp[i-1][j-wts[i-1]],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
print(dp)
#'''