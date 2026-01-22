'''
def check(c,t,i):
    if t==0:
        return 1
    if i>=len(c):
        return 0
    incl,excl=0,0
    if c[i]<=t:
        incl=check(c,t-c[i],i)
    excl=check(c,t,i+1)
    return incl+excl

def check_dp(c,t,i,dp):
    if t==0:
        return 1
    if i>=len(c):
        return 0
    if dp[i][t]!=-1:
        return dp[i][t]
    incl,excl=0,0
    if c[i]<=t:
        incl=check_dp(c,t-c[i],i,dp)
    excl=check_dp(c,t,i+1,dp)
    dp[i][t]=incl+excl
    return dp[i][t]

c,t=list(map(int,input().split())),int(input())
print(check(c,t,0))
dp=[[-1]*(t+1) for _ in range(len(c)+1)]
print(check_dp(c,t,0,dp),dp)
#'''

'''
def check(li,tar,i):
    if tar==0:
        return 0
    if tar<0 or i==len(li):
        return 9999
    incl=1+check(li,tar-li[i],i)
    excl=check(li,tar,i+1)
    return min(incl,excl)

def check_dp(li,tar,i,dp):
    if tar==0:
        return 0
    if tar<0 or i==len(li):
        return 9999
    if dp[i][tar]!=-1:
        return dp[i][tar]
    incl=1+check_dp(li,tar-li[i],i,dp)
    excl=check_dp(li,tar,i+1,dp)
    dp[i][tar]=min(incl,excl)
    return dp[i][tar]

li,tar=list(map(int,input().split())),int(input())
print(check(li,tar,0))
dp=[[-1]*(tar+1) for _ in range(len(li)+1)]
#'''

'''
def generate(st,i,k):
    if i==len(st):
        print(k)
        return
    generate(st,i+1,k+st[i])
    generate(st,i+1,k)

st=input()
print(generate(st,0,''))
#'''

'''
def sub(s1,s2,i,j):
    if i==0 or j==0:
        return 0
    if s1[i-1]==s2[j-1]:
        return 1+sub(s1,s2,i-1,j-1)
    return max(sub(s1,s2,i,j-1),sub(s1,s2,i-1,j))

def sub_dp(s1,s2,i,j,dp):
    if i==0 or j==0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if s1[i-1]==s2[j-1]:
        return 1+sub_dp(s1,s2,i-1,j-1,dp)
    dp[i][j]=max(sub_dp(s1,s2,i,j-1,dp),sub_dp(s1,s2,i-1,j,dp))
    return dp[i][j]

s1,s2=input(),input()
print(sub(s1,s2,len(s1),len(s2)))
dp=[[-1]*(len(s1)+1) for _ in range(len(s2)+1)]
print(sub_dp(s1,s2,len(s1),len(s2),dp),dp)
dpt=[[-1]*(len(s1)+1) for _ in range(len(s2)+1)]
for i in range(len(s1)+1):
    for j in range(len(s2)+1):
        if i==0 or j==0:
            dpt[j][i]=0
        elif s1[i-1]==s2[j-1]:
            dpt[j][i]=1+dpt[j-1][i-1]
        else:
            dpt[j][i]=max(dpt[j-1][i],dpt[j][i-1])
print(dpt[len(s2)][len(s1)],dpt)
#'''

'''
def check(s,i,j):
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False
    return check(s,i+1,j-1)
s=input()
print(check(s,0,len(s)-1))
#'''

#Longest Palindrom Subsequence
'''
def check(s,i,j):
    if i>=j:
        return 0
    if s[i]==s[j]:
        return 2+check(s,i+1,j-1)
    return max(check(s,i+1,j),check(s,i,j-1))

def check_dp(s,i,j,dp):
    if i>=j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i]==s[j]:
        return 2+check_dp(s,i+1,j-1,dp)
    dp[i][j]=max(check_dp(s,i+1,j,dp),check_dp(s,i,j-1,dp))
    return dp[i][j]

s=input()
print(check(s,0,len(s)-1))
dp=[[-1]*(len(s)+1) for _ in range(len(s)+1)]
print(check_dp(s,0,len(s)-1,dp),dp)
dpt=[[-1]*(len(s)+1) for _ in range(len(s)+1)]
for i in range(len(s)-1,-1,-1):
    for j in range(len(s)+1):
        if i==0 or j==0:
            dpt[i][j]=0
        elif s[i]==s[j]:
            dpt[i][j]=2+dpt[i+1][j-1]
        else:
            dpt[i][j]=max(dpt[i+1][j],dpt[i][j-1])
print(dpt[-1][-1],dpt)
#'''

#Minimum no of insertion or deletion to convert s1 to s2
'''
def sub(s1,s2,i,j):
    if i==0 or j==0:
        return 0
    if s1[i-1]==s2[j-1]:
        return 1+sub(s1,s2,i-1,j-1)
    return max(sub(s1,s2,i,j-1),sub(s1,s2,i-1,j))

s1,s2=input(),input()
n=sub(s1,s2,len(s1),len(s2))
print(len(s1)-n+len(s2)-n)
#'''

#Minimum no of insertion to convert string into palindrome
'''
def convert(s,i,j):
    if i>j:
        return 0
    if i==j:
        return 1
    if s[i]==s[j]:
        return 2+convert(s,i+1,j-1)
    return max(convert(s,i+1,j),convert(s,i,j-1))

s=input()
n=convert(s,0,len(s)-1)
print(len(s)-n)
#'''

#Print longest sub sequence palindrome string
'''
s = input()
n = len(s)
dp=[[-1]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j]:
            dp[i][j] = 2 + dp[i+1][j-1]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
i, j = 0, n-1
left, right = [], []
while i <= j:
    if s[i] == s[j]:
        if i == j:
            left.append(s[i])
        else:
            left.append(s[i])
            right.append(s[j])
        i += 1
        j -= 1
    elif dp[i+1][j] > dp[i][j-1]:
        i += 1
    else:
        j -= 1
print("".join(left + right[::-1]))
print(dp[0][n-1])
#'''

#print small super sequence from s1 and s2
'''
def super(s1,s2,i,j):
    if i<0:
        return s2[:j+1]
    if j<0:
        return s1[:i+1]
    if s1[i]==s2[j]:
        return super(s1,s2,i-1,j-1)+s1[i]
    return min(super(s1,s2,i-1,j)+s1[i],super(s1,s2,i,j-1)+s2[j])

def super_dp(s1,s2,i,j,dp):
    if i<0:
        return s2[:j+1]
    if j<0:
        return s1[:i+1]
    if dp[i][j]!=-1:
        return dp[i][j]
    if s1[i]==s2[j]:
        dp[i][j]=super_dp(s1,s2,i-1,j-1,dp)+s1[i]
    else:
        dp[i][j]=min(super_dp(s1,s2,i-1,j,dp)+s1[i],super_dp(s1,s2,i,j-1,dp)+s2[j])
    return dp[i][j]

s1,s2=input(),input()
print(super(s1,s2,len(s1)-1,len(s2)-1))
dp=[[-1]*(len(s2)+1) for _ in range(len(s1)+1)]
print(super_dp(s1,s2,len(s1)-1,len(s2)-1,dp),dp)
#'''

'''
def sub(s1,s2,i,j):
    if i==0 or j==0:
        return ''
    if s1[i-1]==s2[j-1]:
        return sub(s1,s2,i-1,j-1)+s1[i-1]
    return max(sub(s1,s2,i,j-1)+s1[i-1],sub(s1,s2,i-1,j)+s2[j-1])

s1,s2=input(),input()
ss=sub(s1,s2,len(s1),len(s2))
sup,i,j,k='',0,0,0
while k<len(ss):
    if s1[i]==ss[k] and s2[j]==ss[k]:
        sup+=ss[k]
        i,j,k=i+1,j+1,k+1
    elif s1[i]==ss[k]:
        sup+=s2[j]
        j=j+1
    else:
        sup+=s1[i]
        i=i+1
sup+=s1[i:]
sup+=s2[j:]
print(sup)
#'''

#How many times a string is present as sub sequence in another string
'''
s1,s2=input(),input()
def check(i,j):
    if j==len(s2):
        return 1
    if i==len(s1):
        return 0
    if s1[i]==s2[j]:
        return check(i+1,j+1)+check(i+1,j)
    return check(i+1,j)
print(check(0,0))

dp=[[-1]*len(s2) for _ in range(len(s1))]
def check_dp(i,j):
    if j==len(s2):
        return 1
    if i==len(s1):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if s1[i]==s2[j]:
        dp[i][j]=check_dp(i+1,j+1)+check_dp(i+1,j)
    else:
        dp[i][j]=check_dp(i+1,j)
    return dp[i][j]
print(check_dp(0,0),dp)
#'''

#How many edits are required to convert s1 to s2
'''
s1,s2=input(),input()
def check(i,j):
    if j<0 or i<0:
        return 0
    if s1[i]==s2[j]:
        return check(i-1,j-1)
    else:
        return min(check(i,j-1),check(i-1,j),check(i-1,j-1))+1
print(check(len(s1)-1,len(s2)-1))
#'''

#Wildcard pattern matching
'''
s1,s2=input(),input()
def check(i,j):
    if i<0 and j<0:
        return True
    if i<0:
        return False
    if s1[i]==s2[j] or s1[i]=='?':
        return check(i-1,j-1)
    if s1[i]=='*':
        return check(i-1,j) or check(i,j-1)
    return False
print(check(len(s1)-1,len(s2)-1))
#'''

#Longest sub sequence of a integer array in 
#'''
s=list(map(int,input().split()))
n=len(s)
def check(i,pr):
    if i==n:
        return 0
    incl,excl=0,0
    if s[i]>pr:
        incl=check(i+1,s[i])+1
    excl=check(i+1,pr)
    return max(incl,excl)
print(check(0,-1))
dp=[1]*n
par=[[] for _ in range(n)]
def bp(i):
    if not par[i]:
        return [[s[i]]]
    p=[]
    for p in par[i]:
        for seq in bp(p):
            p.append(seq + [s[i]])
    return p
def check_dp(s,n):
    for i in range(1,n):
        for j in range(i):
            if s[i]>s[j]:
                if dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    par[i]=[j]
                elif dp[j]+1==dp[i]:
                    par[i].append(j)
    ml=max(dp)
    all_lis=[]
    for i in range(n):
        if dp[i]==ml:
            all_lis.extend(bp(i))
    return ml,len(all_lis),all_lis
print(check_dp(s,n))
#'''